import subprocess
import sys

def install_packages():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    except subprocess.CalledProcessError as e:
        print(f"Error when installing the packages: {e}")
        sys.exit(1)

if __name__ == "__main__":
    install_packages()