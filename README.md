# Terminal Pomodoro Timer ⏰

A terminal-based Pomodoro Timer with sound notifications for Linux.

## 🚀 Features

- Work session timer with customizable duration.
- Break session timer with customizable duration.
- Sound notifications at the end of each session.

## 🛠️ Installation

**Use the following command for installation:**

```bash
git clone git@github.com:SimaoGato/terminal-pomodoro.git && cd terminal-pomodoro && chmod +x setup.sh && ./setup.sh
```

# ⚙️ Usage

- Start the timer with the default setting:

```bash
pomodoro
```

- Customize the timer (not persistent):

```bash
pomodoro --work 30 --break_time 10 --cycles 5
```

- Change the default settings (persistent):

```bash
pomodoro --settings
```

# 📦 Project Structure

```bash
terminal-pomodoro/
├── pomodoro.py       # The main Python script
├── setup.sh          # Installation script for Linux
├── work_done.wav     # Work session sound
├── break_done.wav    # Break session sound
└── README.md         # Documentation
```

# 📄 License

This project is licensed under the MIT License.
