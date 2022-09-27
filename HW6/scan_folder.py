from genericpath import exists, isdir, isfile
from os import mkdir, remove, rmdir, rename, listdir, startfile
from pathlib import Path
import shutil
import sys

USER_PATH = ""                                      # Адрес чистки папки

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



def path_images(path):
    return f"{path}/images"
def path_videos(path):
    return f"{path}/videos"
def path_documents(path):
    return f"{path}/documents"
def path_audios(path):
    return f"{path}/audios"
def path_archives(path):
    return f"{path}/archives"
def path_x_files(path):
    return f"{path}/x_files"



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


adres_folder_list = {
            "image" : path_images,
            "video" : path_videos,
            "doc" : path_documents,
            "audio" : path_audios,
            "arh" : path_archives,
            "x_files" : path_x_files,
}
def remove_file(folder, path):
    i = 0
    adres_folder = None
    for type_file, file_exts in suffix_list.items():
        if (folder.suffix).lower() in file_exts: 
            adres_folder = type_file
            break
    if (folder.suffix).lower() in suffix_list["arh"]:
        new_name = (folder.name).split(".")
        new_name = normalize(str(new_name[:-1]))
        while exists(f"{adres_folder_list[adres_folder](path)}/{new_name}"):
            new_name = (folder.name).split(".")
            new_name = normalize(str(new_name[:-1]) + f"({i})")
            i += 1 
        shutil.unpack_archive(folder, f"{adres_folder_list[adres_folder](path)}/{new_name}")
        remove(folder)
    elif adres_folder is None:
        ather_expan.add(folder.suffix)      # Список неизвестных расширений
        new_name = folder.name
        while exists(f"{adres_folder_list['x_files'](path)}/{new_name}"):
            new_name = (f"({i})" + str(folder.name))
            i += 1
        shutil.move(folder, f"{adres_folder_list['x_files'](path)}/{new_name}")
    else:
        new_name = (folder.name).split(".")
        new_name = normalize(str(new_name[:-1])) + "." + new_name[-1]
        while exists(f"{adres_folder_list[adres_folder](path)}/{new_name}"):
            new_name = (folder.name).split(".")
            new_name = normalize(str(new_name[:-1])) + f"({i})" + "." + new_name[-1]
            i += 1
        shutil.move(folder, f"{adres_folder_list[adres_folder](path)}/{new_name}")


def scan_folder(path):         # Основное тело скрипта(сортировка и переименование)
    # path = Path(path)
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
            remove_file(folder, path)
    

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
        for file in Path(adres_folder_list[type_file](path)).iterdir():
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
    return "\n>>> Chek your scan folder or use menu options <<<"


def start_scan(path=None):    
    if USER_PATH == "": 
        return "\n>>>>>> WRITE FOLDER ADRESS!!! <<<<<<\n>>>>>> WRITE FOLDER ADRESS!!! <<<<<<\n>>>>>> WRITE FOLDER ADRESS!!! <<<<<<"                         # Функция запуска сортировки
    if path is None:
        for arg in sys.argv[1:]:
            path = arg
    path = Path(path)
    new_folders_create(path)
    scan_folder(path)
    print_name_def(path)

                                 # Запуск сортировки

def close(*_):
    return "\n>> Invalid chose"



def main():
    user_input = ""
    while user_input != 0:
        print_help()
        user_input = input(">>> 0: Exit to main menu.\n\n<< Chose you command: ")
        user_input = CLEAN_DICT.get(user_input, close)
        user_input = user_input(USER_PATH)
        if user_input != None:
            print(user_input)

def write_path(*_):
    global USER_PATH
    user_input = ""
    while user_input != "0":
        user_input = input("\n>>> 0: To enter the contact menu.\n\n<< Write folder adress to work whis it: ").strip()
        if user_input == "0":
            return
        if len(user_input.split(" ")) > 1 or isfile(user_input) == True or isdir(user_input) == False:
            return "\n>>> You write invalid folder adress <<<"
        USER_PATH = user_input
        return "\n>>> Adress folder added to work whith it <<<"


def print_help():
    i = 1
    a =["\nList of commands:\n"]
    for help_text in HELP_CLEAN_DICT.values():
        a.append("".join(f"> {i}) {help_text}\n"))
        i += 1

    print("".join(a))

def open_folder(path):
    try:
        startfile(path)
    except:
        return "\n>>> This folder don`t find! <<<"
    

def open_file(path):
    try:
        startfile(f"{path}\\result_scan.txt")
    except FileNotFoundError:
        return "\n>>> You don`t clean this folder! <<<"

HELP_CLEAN_DICT =   {
                    "write_path" : ">>> Chose folder to work whit it! <<<",
                    "start_scan" : "Start clean folder",
                    "open_folder" : "Open folder after clean",
                    "open_file" : "Open read file after clean",
                    }

CLEAN_DICT =    {
                "1" : write_path,
                "2" : start_scan,
                "3" : open_folder,
                "4" : open_file,
                }


def start_bot():
    main()

start_bot()
