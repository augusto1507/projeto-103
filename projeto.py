import time
import os
import shutil


from watchdog.observers import Observer

from watchdog.events import FileSystemEventHandler

#colar from dir e todir
from_dir = "C:/Users/jucel/OneDrive/Área de Trabalho/games guto/projeto 103"             
to_dir = "C:/Users/jucel/OneDrive/Área de Trabalho/games guto/projeto 103 2" 

dir_tree = {
    "Image_Files": ['.jpg', '.jpeg', '.png', '.gif', '.jfif'],
    "Video_Files": ['.mpg', '.mp2', '.mpeg', '.mpe', '.mpv', '.mp4', '.m4p', '.m4v', '.avi', '.mov'],
    "Document_Files": ['.ppt', '.xls', '.xlsx' '.csv', '.pdf', '.txt'],
    "Setup_Files": ['.exe', '.bin', '.cmd', '.msi', '.dmg', '.tpm']
}

# Classe Gerenciadora de movimentação Arquivos
class FileeventHandler(FileSystemEventHandler):
    
    def on_created(self,event):
        print(f"ola,{event.src_path}foi criado")

    def on_deleted(self, event):
        print(f"opa,alguem excluiu {event.src_path}")

    def on_modified(self, event):
        print(f"alguem modificou {event.src_path}")

    def on_moved(self, event):
        print(f"opa alguem moveu {event.src_path}")

# Inicialize a Classe Gerenciadora de Eventos
event_handler = FileeventHandler()

# Inicialize o Observer
observer = Observer()

observer.schedule(event_handler, from_dir, recursive=True)


observer.start()

try:
    while True:
        time.sleep(2)
        print("executando...")
except KeyboardInterrupt:
    print("interrompido!")
    observer.stop()