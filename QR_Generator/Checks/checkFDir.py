import os

def check_dir(directory: str) -> None:
    """
    Проверяет существование директории, в которой хранятся qr коды, если директории нету, то создает.

    Args:
        directory (str): Путь к проверяемой директории.

    Returns:
        None
    """
    if not os.path.isdir(directory):
        os.makedirs(directory, exist_ok=True)
        print("Директория для QR кодов успешно создана.")
    else:
        print("Директория для QR кодов уже существует.")

def check_file_data(file_name: str) -> None:
    """
    Проверяет наличие файла с информацией для QR кода.

    Arg:
        file_name (str): Название проверяемого файла

    Return:
        None
    """
    if not os.path.isfile(file_name):
        with open(file_name, "r") as file:
            print("Текстовый файл создан.")
            file.close()
    else:
        print("Текстовый файл уже существует.")
