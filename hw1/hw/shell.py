import os
import zipfile
import json
import xml.etree.ElementTree as ET

def read_config(config_path):
    tree = ET.parse(config_path)
    root = tree.getroot()

    config = {
        "hostname": root.find('hostname').text,
        "vfs_path": root.find('vfs_path').text,
        "log_path": root.find('log_path').text
    }
    return config

def extract_vfs(zip_path, extract_to):
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def list_directory(path):
    try:
        files = os.listdir(path)
        if files:
            print("  ".join(files))  # Выводим файлы в одну строку с пробелами
        else:
            print("Directory is empty.")
    except FileNotFoundError:
        print("Directory not found.")

def change_directory(path, start_dir):
    try:
        new_path = os.path.abspath(os.path.join(os.getcwd(), path))
        if not new_path.startswith(start_dir):
            return "Cannot go outside the starting directory."
        os.chdir(new_path)
        return os.getcwd()
    except FileNotFoundError:
        return "Directory not found."

def log_command(log_file, command):
    with open(log_file, 'a') as log:
        json.dump({"command": command, "path": os.getcwd()}, log)
        log.write('\n')

def view_history(log_file):
    with open(log_file, 'r') as log:
        for line in log:
            print(json.loads(line))

def shell(config):
    extract_vfs(config["vfs_path"], "./vfs")
    log_file = config["log_path"]
    start_dir = os.getcwd()
    command_history = []

    # Создание лог-файла, если он не существует
    if not os.path.exists(log_file):
        with open(log_file, 'w') as log:
            pass

    while True:
        command = input(f"{config['hostname']}:~$ ")

        if command == "exit":
            break
        elif command == "ls":
            list_directory(os.getcwd())  # Здесь не нужно использовать print()
            log_command(log_file, command)
        elif command.startswith("cd "):
            path = command[3:]
            result = change_directory(path, start_dir)
            
            log_command(log_file, command)
        elif command == "history":
            for cmd in command_history:
                print(cmd)
        elif command == "who":
            print("Current user: root")
            log_command(log_file, command)
        else:
            print("Command not found.")

        command_history.append(command)

    # Очистка истории команд после завершения цикла
    with open(log_file, 'w') as log:
        log.truncate(0)

if __name__ == "__main__":
    config = read_config("config.xml")
    shell(config)
