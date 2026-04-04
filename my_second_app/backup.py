import shutil
import time
import os

while True:
    files = os.listdir("data")

    for file in files:
        shutil.copy("data/" + file, "backup/" + file)

    print("Backup done")

    time.sleep(60)