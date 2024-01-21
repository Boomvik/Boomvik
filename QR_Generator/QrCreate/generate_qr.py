import qrcode
from PIL import Image
from GetData.get_data_for_qr import load_config

# Загрузка настроек
default_config_path = 'default_settings.ini'
user_config_path = 'user_settings.ini'
config = load_config(default_config_path, user_config_path)

# Исключение для некоторых данных
error_correction_string = config.get('options', 'error_correction')
error_correction = getattr(qrcode.constants, error_correction_string.split('.')[-1])
fill_color = config.get("options", "fill_color")
back_color = config.get("options", "back_color")

def generate_qr(path_save: str, data: tuple, name_qr: str) -> None:
    """
    Создаёт QR код для заданной информации и сохраняет его.

    Args:
        path_save (str): Путь сохранения QR кода.
        data (tuple): Информация, которая генерируется в QR код.
        name_qr (str): Название QR кода.

    Return:
        None
    """
    qr = qrcode.QRCode(
        version=config.getint("options", "version"),
        box_size=config.getint("options", "box_size"),
        border=config.getint("options", "border"),
        error_correction=error_correction

    )

    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fill_color, back_color=back_color)
    img.save(f"{path_save}{name_qr}")
