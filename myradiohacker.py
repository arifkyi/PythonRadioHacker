import argparse
import os
import subprocess

def record():
    # Delete existing file if it exists
    if os.path.exists("myrec"):
        os.remove("myrec")
    # Run hackrf_transfer to record data
    subprocess.run(["hackrf_transfer", "-s", "8000000", "-f", "433918000", "-r", "myrec", "-b", "8000000"])

def play():
    # Run hackrf_transfer to play recorded data
    subprocess.run(["hackrf_transfer", "-s", "8000000", "-f", "433918000", "-t", "myrec", "-a", "1", "-x", "47", "-b", "8000000"])

# Parse command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("mode", choices=["r", "record", "p", "play"], help="Mode of operation: 'r' or 'record' to record data, 'p' or 'play' to play recorded data")
args = parser.parse_args()

# Dispatch based on mode
if args.mode in ["r", "record"]:
    record()
elif args.mode in ["p", "play"]:
    play()
else:
    print("Invalid mode. Please use 'r' or 'record' to record data, or 'p' or 'play' to play recorded data.")

