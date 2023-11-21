import os
import shutil
import time
import random

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler



from_dir =  "C:/Users/Admin/Downloads"              
to_dir = "C:/Users/Admin/Downloads/newFolder" 


dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg']
}

class FileMovementHandler(FileSystemEventHandler):
    def on_created(self , event):
        root, ext = os.path.splitext(event.src_path)

        time.sleep(1)

        for key, value in dir_tree.items():
            time.sleep(1)
            if ext in value:
                fileName = os.path.basename(event.src_path)
               
                if os.path.exists(from_dir + '/' + key):
                    shutil.move(to_dir + '/' + fileName, to_dir + '/' + key + '/' + fileName)
                else:
                    os.makedirs(from_dir + '/' + key)
                    shutil.move(to_dir + '/' + fileName, to_dir + '/' + key + '/' + fileName)


# C:/Users/Admin/Downloads/abc.png
# C:/Users/Admin/Downloads/Image_Files/abc.png

event_handler = FileMovementHandler()

observer = Observer()

observer.schedule(event_handler , from_dir , recursive = True)
observer.start()



try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()


# ● on_any_event(): Called for all event handlers.
# ● on_created(): Called when a file or a directory is created.
# ● on_modified(): Called when a file or directory is modified.
# ● on_moved(): Called when a file or a directory is moved or renamed.
# ● on_deleted(): Called when a file or directory is deleted.

