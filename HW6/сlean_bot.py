from datetime import datetime
from genericpath import exists, isdir, isfile
from os import mkdir, remove, rmdir, listdir, rename
import os
from pathlib import Path
import shutil
import sys
import concurrent.futures


if sys.platform == "win32":
    from os import startfile

PATH_LIST = []
USER_PATH = ""
                                                    # Адрес чистки папки
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



def path_images():
    return f"{USER_PATH}\\images"
def path_videos():
    return f"{USER_PATH}\\videos"
def path_documents():
    return f"{USER_PATH}\\documents"
def path_audios():
    return f"{USER_PATH}\\audios"
def path_archives():
    return f"{USER_PATH}\\archives"
def path_x_files():
    return f"{USER_PATH}\\x_files"


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
    global PATH_LIST 
    for path_adr in adres_folder_list.values():
        PATH_LIST.append(path_adr())
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

def remove_file(file_list): 
    for file_path in file_list:
        i = 0
        file_name, file_suf = os.path.splitext(file_path)
        all_expan.add(file_suf)  
        file_name = f"{os.path.basename(file_name)}{file_suf}"
        adres_folder = None
        for type_file, file_exts in suffix_list.items():
            if (file_suf).lower() in file_exts: 
                adres_folder = type_file
                break
        
        folder = Path(file_path)
        executor = concurrent.futures.ThreadPoolExecutor(max_workers=4)
        if (file_suf).lower() in suffix_list["arh"]:
            new_name = (folder.name).split(".")
            new_name = normalize(str(new_name[:-1]))
            while exists(f"{adres_folder_list[adres_folder]()}/{new_name}"):
                
                new_name = (folder.name).split(".")
                new_name = normalize(str(new_name[:-1]) + f"({i})")
                i += 1 
            if os.stat(folder).st_size > 50000000:
                with executor:
                    executor.submit(shutil.unpack_archive, folder, f"{adres_folder_list[adres_folder]()}/{new_name}")
                with executor:
                    executor.submit(remove, folder)
            else:
                shutil.unpack_archive(folder, f"{adres_folder_list[adres_folder]()}/{new_name}")

        elif adres_folder is None:
            ather_expan.add(file_suf)      # Список неизвестных расширений
            new_name = folder.name
            while exists(f"{adres_folder_list['x_files']()}/{new_name}"):
                
                new_name = (f"({i})" + str(folder.name))
                i += 1
            if os.stat(folder).st_size > 50000000:
                with executor:
                    executor.submit(shutil.move, folder, f"{adres_folder_list['x_files']()}/{new_name}")
            else:
                shutil.move(folder, f"{adres_folder_list['x_files']()}/{new_name}")
        else:
            new_name = (folder.name).split(".")
            new_name = normalize(str(new_name[:-1])) + "." + new_name[-1]
            while exists(f"{adres_folder_list[adres_folder]()}/{new_name}"):
                new_name = (folder.name).split(".")
                new_name = normalize(str(new_name[:-1])) + f"({i})" + "." + new_name[-1]
                i += 1
            if os.stat(folder).st_size > 50000000:   
                with executor:
                    executor.submit(shutil.move, folder, f"{adres_folder_list[adres_folder]()}/{new_name}")
            else:
                shutil.move(folder, f"{adres_folder_list[adres_folder]()}/{new_name}")


def scan_folder(path):  
    file_list = []
    path_list = []
    for folder_path, not_use, file_name in os.walk(path):
        if folder_path not in [i() for i in adres_folder_list.values()]:
            path_list.append(folder_path)
            for file in file_name:   
                if file != "result_scan.txt" or file_name == []:
                    file_list.append(f"{folder_path}\\{file}")   
    remove_file(file_list)
    try:
        for i in path_list[::-1]:
            rmdir(i)
    except OSError:
        pass


        
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
        for file in Path(adres_folder_list[type_file]()).iterdir():
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
        file.write("| {:<100} |\n".format(f"Оther expanding"))
        file.write("| {:^100} |\n".format(f"{set(ather_expan)}"))
        file.write("| {:<100} |\n".format(f"All expanding"))
        file.write("| {:^100} |".format(f"{set(all_expan)}"))
    return print("\n>>> Chek your scan folder or use menu options <<<")


def start_scan(path=None):    
    if USER_PATH == "": 
        return "\n>>>>>> WRITE FOLDER ADRESS!!! <<<<<<\n>>>>>> WRITE FOLDER ADRESS!!! <<<<<<\n>>>>>> WRITE FOLDER ADRESS!!! <<<<<<"                         # Функция запуска сортировки
    if path is None:
        return "\n>>>>>> WRITE FOLDER ADRESS!!! <<<<<<\n>>>>>> WRITE FOLDER ADRESS!!! <<<<<<\n>>>>>> WRITE FOLDER ADRESS!!! <<<<<<"
    a = datetime.now()
    
    path = Path(path)
    new_folders_create(path)
    scan_folder(path)
    print_name_def(path)
    print(datetime.now() - a)    

def close(*_):
    return "\n>>> Invalid chose <<<"



def main():
    user_input = ""
    while user_input != 0:
        print_help()
        user_input = input(">>> 0: Exit to main menu.\n\n<< Chose you command: ")
        if user_input == "0":
            return 
        user_input = CLEAN_DICT.get(user_input, close)
        user_input = user_input(USER_PATH)
        if user_input != None:
            print(user_input)

def write_path(*_):
    global USER_PATH
    user_input = ""
    while user_input != "0":
        if user_input == "0":
            return
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
        if sys.platform == "win32":
            startfile(path)
        else:
            subprocess.call(['open', path])
    except:
        return "\n>>> This folder don`t find! <<<"
    

def open_file(path):
    try:
        if sys.platform == "win32":
            startfile(f"{path}\\result_scan.txt")
        else:
            FileName = f"{path}/result_scan.txt"
            subprocess.call(['open', FileName])
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


def start_clean_bot():
    main()
