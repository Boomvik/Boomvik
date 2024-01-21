import configparser

def get_info_for_qr(file_name: str) -> tuple:
    """
    Получает информацию из файла.

    Arg:
        file_name (str): Название файла, в котором хранится информацию.

    Return:
        tuple_data (str): Кортеж с данными из файла.

    """
    # Создание кортежа
    tuple_data = ()

    # Чтение файла и разделение информации на строки.
    with open(file_name, "r") as file:
        for string in file.readlines():
            string = string.strip()
            tuple_data += (string,)

    # Возвращение кортежа, в котором строка файла = 1 значению для QR.
    return tuple_data


def load_config(default_settings: str, user_settings: str):
    """
    Загружает конфигурационные настройки из двух файлов:
    default_settings (файл с настройками по умолчанию) и
    user_settings (файл с пользовательскими настройками).

    Возвращает объект Config, содержащий объединенные настройки.
    """

    # Создание объекта ConfigParser
    config = configparser.ConfigParser()

    # Чтение конфигурационных файлов
    config.read(default_settings)
    config.read(user_settings)

    # Возвращение объекта ConfigParser с объединенными настройками
    return config
