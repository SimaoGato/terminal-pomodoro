#!/bin/bash

# Create the hidden directory in the user's home folder
mkdir -p ~/.pomodoro

# Copy the script and sound files to the hidden directory
cp pomodoro.py ~/.pomodoro/
cp work_done.wav ~/.pomodoro/
cp break_done.wav ~/.pomodoro/

# Create a symbolic link to make the 'pomodoro' command globally accessible
sudo ln -sf ~/.pomodoro/pomodoro.py /usr/local/bin/pomodoro

# Make the script executable
chmod +x ~/.pomodoro/pomodoro.py

echo "Pomodoro timer installed successfully!"
echo "Run 'pomodoro' to start the timer."
