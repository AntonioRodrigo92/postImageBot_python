import configparser
import pathlib

import requests


def url_to_image(url, temp_path):
    img_data = requests.get(url).content
    with open(temp_path, 'wb') as handler:
        handler.write(img_data)


def delete_temp_file(temp_path):
    file_to_rem = pathlib.Path(temp_path)
    file_to_rem.unlink()


def read_config_file(file_path):
    config = configparser.ConfigParser()
    config.read(file_path)
    return config
