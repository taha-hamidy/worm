import os
import platform
import sys

def shutdown():
    system = platform.system()
    if system == "Windows":
        # Windows shutdown command
        os.system("shutdown /s /t 0")  # https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/shutdown
    elif system == "Linux" or system == "Darwin":
        # Linux/macOS shutdown command (requires sudo on Linux)
        os.system("shutdown -h now")  # https://man7.org/linux/man-pages/man8/shutdown.1.html
    else:
        print("Unsupported OS")
        sys.exit(1)

if __name__ == "__main__":
    shutdown()