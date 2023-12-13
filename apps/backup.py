import os
import shutil
import datetime
import schedule
import time

source_dir = "D:\!PROGRAMOWANIE\Python\screens"
destination_dir = "D:\!BACKUP"

def copy_folder_todirectory(source, dest):
    today = datetime.date.today()
    dest_dir = os.path.join(dest, str(today))

    try:
        shutil.copytree(source, dest_dir)
        print(f"Folder copied to: {dest_dir}")
    except FileExistsError:
        print(f"Folder alteady exist in: {dest}")

schedule.every().day.at("09:20").do(lambda: copy_folder_todirectory(source_dir, destination_dir))

while True:
    schedule.run_pending()
    time.sleep(60)