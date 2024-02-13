import os
import shutil


# Prompt: Нужно написать скрипт на Python, который будет копировать каждую папку внутри папки mods в заданную целевую
# директорию.
def find_mods_dirs(root_dir):
    """
    Находит все директории mods внутри заданной корневой директории.
    """
    mods_dirs = []
    for root, dirs, files in os.walk(root_dir):
        if os.path.basename(root) == 'mods':
            mods_dirs.append(root)
    return mods_dirs


def copy_mods_dirs(mods_dirs, target_dir):
    """
    Копирует все папки внутри директорий mods в целевую директорию.
    """
    for mods_dir in mods_dirs:
        print("Обработка папки mods:", mods_dir)
        for folder_name in os.listdir(mods_dir):
            folder_path = os.path.join(mods_dir, folder_name)
            # Проверяем, является ли элемент директорией
            if os.path.isdir(folder_path):
                print("Найдена папка:", folder_path)
                # Создаем путь к целевой директории, сохраняя структуру папок
                target_folder_path = os.path.join(target_dir,
                                                  os.path.relpath(folder_path, start=os.path.dirname(mods_dir)))
                print("Целевая директория для копирования:", target_folder_path)
                # Проверяем, существует ли целевая директория
                if not os.path.exists(target_folder_path):
                    os.makedirs(target_folder_path)
                # Копируем содержимое папки
                print("Копирование папки...")
                for src_dir, dirs, files in os.walk(folder_path):
                    dst_dir = src_dir.replace(folder_path, target_folder_path, 1)
                    if not os.path.exists(dst_dir):
                        os.makedirs(dst_dir)
                    for file_ in files:
                        src_file = os.path.join(src_dir, file_)
                        dst_file = os.path.join(dst_dir, file_)
                        if os.path.exists(dst_file):
                            os.remove(dst_file)
                        shutil.copy2(src_file, dst_dir)
                print("Папка успешно скопирована.")


# Задайте корневую директорию для поиска директорий mods. Путь до папки с модами для Zomboid.
# ОТКУДА КОПИРОВАТЬ
root_dir = r'C:\Program Files (x86)\Steam\steamapps\workshop\content\108600'

# Задайте целевую директорию для копирования. Папка mods создаётся автоматически, все моды внутри перезаписываются.
# КУДА КОПИРОВАТЬ
target_dir = r'C:\Users\НАЗВАНИЕ ПРОФИЛЯ ПОЛЬЗОВАТЕЛЯ\Zomboid'

# Проверяем, существует ли корневая директория
if not os.path.exists(root_dir):
    print(f"Корневая директория {root_dir} не существует. Проверьте путь и повторите попытку.")
    exit(1)  # Выход из скрипта с кодом ошибки

# Проверяем, существует ли целевая директория
if not os.path.exists(target_dir):
    print(f"Целевая директория {target_dir} не существует. Создаём директорию.")
    os.makedirs(target_dir)  # Создаем целевую директорию, если она не существует

# Находим все директории mods
mods_dirs = find_mods_dirs(root_dir)
# Копируем содержимое найденных директорий mods в целевую директорию
copy_mods_dirs(mods_dirs, target_dir)
