import logging
import os
import requests

modules = {}
commands = {}
files = {}
modules_int = 0


def add_module(module_name: str, filename: str):
    global modules_int

    modules[module_name] = filename
    modules_int = modules_int + 1


def add_command(module_name: str, command_name: str, help_command: str):
    commands.setdefault(module_name, {})
    commands[module_name][command_name] = help_command


def get_module_commands(module_name):
    if module_name in commands:
        return commands[module_name]
    else:
        return {}


def get_file_by_module(module_name):
    if module_name in modules:
        dir_name, file_name = os.path.split(modules[module_name])
        last_folder = os.path.basename(dir_name)
        return os.path.join(last_folder, file_name)
    else:
        return None


def add_file(module_name: str, file_name: str):
    files.setdefault(module_name, {})
    var = files[module_name][file_name]


def load_module(link):
    filename = os.path.basename(link)
    code = requests.get(link).text
    return filename, code


def upload_module(module_name: str):
    if module_name in modules:
        return modules[module_name]
    else:
        return "Module not found"


def remove_module(module_name: str):
    if module_name in modules:
        try:
            os.remove(modules[module_name])
            return "successfully"
        except Exception as e:
            logging.error(e)
            return "error"
    else:
        return "Module not found"
