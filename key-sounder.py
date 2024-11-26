import os
import sys
import pygame
import threading
from pynput import keyboard
import pygetwindow as gw

# Check if the program is running as a bundled executable
if getattr(sys, 'frozen', False):
    # If the application is running as a PyInstaller bundle
    base_path = sys._MEIPASS
else:
    # If running normally (not as a bundle)
    base_path = os.path.abspath(".")

# Construct the path to the sound file
sound_path = os.path.join(base_path, 'sound.wav')

# Initialize pygame mixer for low-latency sound playback
pygame.mixer.init(frequency=384000, size=-16, channels=2, buffer=0)  # optimize buffer size for low latency
pygame.mixer.set_num_channels(128)

# Pre-load the sound to avoid delay during playback
sound = pygame.mixer.Sound(sound_path)

# To keep track of which keys are pressed
pressed_keys = set()

# Total number of keys pressed
total_keys_pressed = 0

# Initial volume
volume = 0.05  # Start at 5% volume

# Lock for safely modifying the volume in threads
volume_lock = threading.Lock()

def adjust_volume(increase):
    global volume
    with volume_lock:
        if increase:
            # Increase the volume but don't let it exceed 1.0
            volume = min(volume + 0.01, 1.0)
        else:
            # Decrease the volume but don't let it go below 0.0
            volume = max(volume - 0.01, 0.0)
        volume = round(volume, 2)
        sound.set_volume(volume)  # Apply the new volume
        print("Volume:", volume)

def volume_control():
    # Repeatedly adjust volume every 100ms if arrow keys are being held down
    while True:
        if "up" in pressed_keys and is_program_in_focus():
            adjust_volume(True)  # Increase volume
        if "down" in pressed_keys and is_program_in_focus():
            adjust_volume(False)  # Decrease volume
        threading.Event().wait(0.1)  # Wait 100ms

def play_sound():
    sound.set_volume(volume)  # Set current volume
    sound.play()  # Play sound immediately

def on_press(key):
    global total_keys_pressed
    try:
        k = key.char  # single-char keys
    except AttributeError:
        k = key.name  # other keys (e.g., 'esc')

    # Only respond to key press if it's not already in the pressed_keys set
    if k not in pressed_keys:
        if k in ['z', 'x']:  # keys of interest
            total_keys_pressed += 1
            print(f'Key pressed: {k} ({total_keys_pressed})')
            threading.Thread(target=play_sound, daemon=True).start()  # Play sound in background with low latency
            pressed_keys.add(k)  # Mark key as pressed

        if k == 'up' and is_program_in_focus():  # Increase volume on Arrow Up (only when in focus)
            pressed_keys.add(k)
        if k == 'down' and is_program_in_focus():  # Decrease volume on Arrow Down (only when in focus)
            pressed_keys.add(k)

        if k == 'esc' and is_program_in_focus():  # Stop listener when Escape key is pressed (only when in focus)
            return False  # Stop listener

def on_release(key):
    try:
        k = key.char
    except AttributeError:
        k = key.name

    # Remove key from pressed_keys when released
    if k in pressed_keys:
        pressed_keys.remove(k)

# Function to get the current program's window title dynamically
def get_program_window_title():
    try:
        for window in gw.getWindowsWithTitle(''):
            if window.title:  # Filter out windows without titles
                # Compare the file's executable name with the window title
                if sys.argv[0] in window.title or window.title.endswith(".py"):
                    return window.title
        return None
    except Exception as e:
        print(f"Error fetching window title: {e}")
        return None

# Function to check if the program's window is in focus
def is_program_in_focus():
    try:
        # Get the title of the currently focused window
        focused_window = gw.getActiveWindow()
        program_title = get_program_window_title()
        # Check if the active window is the same as the program's window
        return focused_window and program_title and program_title in focused_window.title
    except Exception as e:
        print(f"Error checking focus: {e}")
        return False  # In case of error, assume program is not in focus

# Set up the volume control thread
volume_thread = threading.Thread(target=volume_control, daemon=True)
volume_thread.start()

# Set up the listener
listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()  # Start the listener in a separate thread
listener.join()
