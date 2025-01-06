#!/usr/bin/env python3

import argparse
import json
import os
import subprocess
import time

# Paths
CONFIG_FILE = os.path.expanduser("~/.pomodoro/config.json")
WORK_DONE_SOUND = os.path.expanduser("~/.pomodoro/work_done.wav")
BREAK_DONE_SOUND = os.path.expanduser("~/.pomodoro/break_done.wav")

# Default settings
DEFAULT_SETTINGS = {"work_minutes": 25, "break_minutes": 5, "cycles": 4}


# Load or create the config file
def load_settings():
    if not os.path.exists(CONFIG_FILE):
        os.makedirs(os.path.dirname(CONFIG_FILE), exist_ok=True)
        save_settings(DEFAULT_SETTINGS)
    with open(CONFIG_FILE, "r") as file:
        return json.load(file)


# Save settings to the config file
def save_settings(settings):
    with open(CONFIG_FILE, "w") as file:
        json.dump(settings, file, indent=4)


# Play sound using subprocess
def play_sound(sound_file):
    try:
        subprocess.run(
            ["aplay", sound_file],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            check=True,
        )
    except subprocess.CalledProcessError as e:
        print(f"Error playing sound: {e}")


# Countdown timer function
def countdown_timer(seconds, session_type):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02}:{secs:02}"
        print(f"\r{session_type} Timer: {timer}   ", end="", flush=True)
        time.sleep(1)
        seconds -= 1
    print()


# Pomodoro timer function
def pomodoro_timer(work_minutes, break_minutes, cycles):
    for cycle in range(1, cycles + 1):
        print(f"\nCycle {cycle} of {cycles}")
        print("Starting work session...")
        countdown_timer(work_minutes * 60, "Work")
        print("Work session complete! Take a break.")
        play_sound(WORK_DONE_SOUND)

        if cycle < cycles:
            print("Starting break session...")
            countdown_timer(break_minutes * 60, "Break")
            print("Break session complete! Back to work.")
            play_sound(BREAK_DONE_SOUND)

    print("\nAll cycles complete! Great job!")


# Main function
def main():
    parser = argparse.ArgumentParser(
        description="Terminal-based Pomodoro Timer with sound notifications."
    )
    parser.add_argument("--work", type=int, help="Work session duration in minutes")
    parser.add_argument(
        "--break_time", type=int, help="Break session duration in minutes"
    )
    parser.add_argument("--cycles", type=int, help="Number of cycles")
    parser.add_argument("--settings", action="store_true", help="Open settings menu")

    args = parser.parse_args()
    settings = load_settings()

    if args.settings:
        print("\nSettings Menu")
        print(f"Current Settings: {settings}")
        work_minutes = int(
            input("Enter work session duration in minutes: ")
            or settings["work_minutes"]
        )
        break_minutes = int(
            input("Enter break session duration in minutes: ")
            or settings["break_minutes"]
        )
        cycles = int(input("Enter number of cycles: ") or settings["cycles"])
        new_settings = {
            "work_minutes": work_minutes,
            "break_minutes": break_minutes,
            "cycles": cycles,
        }
        save_settings(new_settings)
        print("Settings saved!")
    else:
        work_minutes = args.work or settings["work_minutes"]
        break_minutes = args.break_time or settings["break_minutes"]
        cycles = args.cycles or settings["cycles"]
        pomodoro_timer(work_minutes, break_minutes, cycles)


if __name__ == "__main__":
    main()
