from Checks.checkFDir import check_dir, check_file_data
from Checks.checkUrl import find_url
from Api.url_shortener import generate_short_link
from GetData.get_data_for_qr import get_info_for_qr, load_config
from QrCreate.generate_qr import generate_qr

if __name__ == "__main__":
    num = 0

    # Загрузка настроек
    default_config_path = 'default_settings.ini'
    user_config_path = 'user_settings.ini'
    config = load_config(default_config_path, user_config_path)

    # Получение пути сохранения QR кода
    directory = config.get("path", "qr_save_path")

    # Проверка на наличие директории для сохранения QR
    check_dir(directory)

    # Проверка на наличие файла с информацией для QR
    check_file_data("Data For QR.txt")

    # Получение информации для QR
    tuple_data = get_info_for_qr("Data For QR.txt")

    # Поиск ссылок из tuple_data
    tuple_links = find_url(tuple_data)

    # Генерация коротких ссылок
    short_links = generate_short_link(tuple_links)

    # Создание и сохранение QR кода
    for data in short_links:
        generate_qr(directory, data, f"Qr_code_{num}.png")
        num += 1
        