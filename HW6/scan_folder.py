from genericpath import exists
from os import mkdir, remove, rmdir, rename, listdir
from pathlib import Path
import shutil
import sys

path = None
if path is None:
    for arg in sys.argv[1:]:
        path = arg
path = Path(path)

i = 0
ather_expan = set()                                 # Список неизвестных расширений
all_expan = set()                                   # Список всех расширений
suffix_list = {
        "image" : [".jpeg", ".png", ".jpg", ".svg"],
        "video" : [".avi", ".mp4", ".mov", ".mkv"], 
        "doc": [".doc", ".docx", ".txt", ".pdf", ".xlsx", ".pptx"],
        "audio" : [".mp3", ".ogg", ".wav", ".amr"],
        "arh" : [".zip", ".gz", ".tar"],
        "new_folder" : ["archives" , "audios", "documents", "images", "videos", "x_files", "result_scan.txt"]
        }

adres_folder_list = {
            "image" : f"{path}/images",
            "video" : f"{path}/videos",
            "doc" : f"{path}/documents",
            "audio" : f"{path}/audios",
            "arh" : f"{path}/archives",
            "x_files" : f"{path}/x_files"
}


def normalize(name_file):                           # Транслитерация 
    cyryllic_name = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґwcqx0123456789"
    translition = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "f", "h", "ts", "ch", "sh", "sch", "", "y", "", "e", "yu", "ya", "je", "i", "ji", "g", "w", "c", "q", "x", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9")
    trans_tuple = {}
    file_name = ""
    for key, value in zip(cyryllic_name, translition): 
        trans_tuple[ord(key)] = value
        trans_tuple[ord(key.upper())] = value.upper()
    name = name_file.translate(trans_tuple)
    for symbol in name: 
        if symbol.lower() in translition: file_name += symbol; 
        else: file_name += "_"
    return file_name


def new_folders_create(path):                  # Создание папок и путей к ним
    folreds_list = listdir(path)
    required_folders = ["archives", "audios", "documents", "images", "videos", "x_files"]
    for folder in required_folders:
        if folder not in folreds_list:
            mkdir(path/folder) 
    if not "result_scan" in folreds_list:
        file = f"{path}/result_scan.txt"     # Создание файла результата
        open(file, "w").close


def remove_file(folder):
    i = 0
    adres_folder = None
    for type_file, file_exts in suffix_list.items():
        if (folder.suffix).lower() in file_exts: 
            adres_folder = type_file
            break
    if (folder.suffix).lower() in suffix_list["arh"]:
        new_name = (folder.name).split(".")
        new_name = normalize(str(new_name[:-1]))
        while exists(f"{adres_folder_list[adres_folder]}/{new_name}"):
            new_name = (folder.name).split(".")
            new_name = normalize(str(new_name[:-1]) + f"({i})")
            i += 1 
        shutil.unpack_archive(folder, f"{adres_folder_list[adres_folder]}/{new_name}")
        remove(folder)
    elif adres_folder is None:
        ather_expan.add(folder.suffix)      # Список неизвестных расширений
        new_name = folder.name
        while exists(f"{adres_folder_list['x_files']}/{new_name}"):
            new_name = (f"({i})" + str(folder.name))
            i += 1
        shutil.move(folder, f"{adres_folder_list['x_files']}/{new_name}")
    else:
        new_name = (folder.name).split(".")
        new_name = normalize(str(new_name[:-1])) + "." + new_name[-1]
        while exists(f"{adres_folder_list[adres_folder]}/{new_name}"):
            new_name = (folder.name).split(".")
            new_name = normalize(str(new_name[:-1])) + f"({i})" + "." + new_name[-1]
            i += 1
        shutil.move(folder, f"{adres_folder_list[adres_folder]}/{new_name}")


def scan_folder(path):         # Основное тело скрипта(сортировка и переименование)
    path = Path(path)
    for folder in path.iterdir():
        if folder.name in suffix_list["new_folder"]:
            continue                                # Исключение конечных папок сортировки
        if folder.is_dir(): 
            scan_folder(folder) 
            try:
                rmdir(folder)                       # Удаление и переименование файлов (Записать ошибку пустой папки)
            except OSError:
                rename(folder, (path/normalize(folder.name))) 
        elif folder.is_file():                      # Сортировка файлов
            all_expan.add(folder.suffix)        
            remove_file(folder)
    

def print_name_def(path):        # Вывод результатов
    
    archives_name = []            
    audios_name = []
    documents_name = []
    images_name = []
    videos_name = []
    x_files_name = []                

    archives_name.append("| {:<100} |".format("File in archives")) # Запись категорий в файл результатов
    audios_name.append("| {:<100} |".format("File in audios"))
    documents_name.append("| {:<100} |".format("File in documents"))
    images_name.append("| {:<100} |".format("File in images"))
    videos_name.append("| {:<100} |".format("File in videos"))
    x_files_name.append("| {:<100} |".format("File in x_files"))
    
    for type_file, folder_adr in adres_folder_list.items():
        for file in Path(adres_folder_list[type_file]).iterdir():
            if type_file == "image":
                archives_name.append("| {:^100} |".format(file.name))
            if type_file == "video":
                audios_name.append("| {:^100} |".format(file.name))
            if type_file == "doc":
                documents_name.append("| {:^100} |".format(file.name))
            if type_file == "audio":
                images_name.append("| {:^100} |".format(file.name))
            if type_file == "arh":
                videos_name.append("| {:^100} |".format(file.name))
            if type_file == "x_files":
                x_files_name.append("| {:^100} |".format(file.name))

    all_files_folder = [archives_name, audios_name, documents_name, images_name, videos_name, x_files_name]
    file = open(f"{path}/result_scan.txt")
    with open(f"{path}/result_scan.txt", "w") as file:      # Запись в файл результатов
        for item in all_files_folder:
            for res in item:
                file.write(f"{res}\n")
        file.write("| {:<100} |\n".format(f"Ather expanding"))
        file.write("| {:^100} |\n".format(f"{set(ather_expan)}"))
        file.write("| {:<100} |\n".format(f"All expanding"))
        file.write("| {:^100} |".format(f"{set(all_expan)}"))
    print("Chek your scan folder! You need 'result_scan.txt'")


def start_scan(path=None):                              # Функция запуска сортировки
    if path is None:
        for arg in sys.argv[1:]:
            path = arg
    path = Path(path)
    new_folders_create(path)
    scan_folder(path)
    print_name_def(path)

start_scan(path=None)                                   # Запуск сортировки

 















