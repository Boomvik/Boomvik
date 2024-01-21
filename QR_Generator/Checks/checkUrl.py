import validators


def find_url(data_for_qr: tuple) -> tuple:
    """
    Проверяет, является ли переданный URL валидным, если да, то добавляет его в list_links.

    Arg:
     data_for_qr (tuple): Информация для QR.
    Return:
        tuple_links (tuple): Кортеж с ссылками.
    """
    # Создание списка
    list_links = []

    for el in data_for_qr:
        if validators.url(el):
            list_links.append(el)
        tuple_links = tuple(list_links)
    return tuple_links
