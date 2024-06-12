import subprocess
import sys

def install_packages():
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    except subprocess.CalledProcessError as e:
        print(f"Error when installing the packages: {e}")
        sys.exit(1)

install_packages()

from ldif_reader import read_ldif
from csv_writer import write_csv

def main():
    # Interaktive Eingabe für die Pfade
    ldif_file_path = input("Please enter the path to the LDIF file: ")
    csv_file_path = input("BPlease enter the path and file name for the output CSV file: ")

    attributes, records = read_ldif(ldif_file_path)
    if not records:
        print("No valid data records found. Check the LDIF file.")
        return

    write_csv(csv_file_path, attributes, records)

if __name__ == "__main__":
    main()