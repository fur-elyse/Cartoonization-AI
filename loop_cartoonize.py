import subprocess
import sys

counter = 0

while counter < int(sys.argv[1]):
    print(counter)
    subprocess.run(["python", "cartoonize.py"])
    counter += 1