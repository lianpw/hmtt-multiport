import os
import yaml
from config import BASE_PATH


def read_yaml(filename):
    file_path = BASE_PATH + os.sep + 'data' + os.sep + filename
    with open(file_path, 'r', encoding='utf-8') as f:
        arr = []
        datas = yaml.safe_load(f).values()
        for data in datas:
            arr.append(tuple(data.values()))
        return arr


if __name__ == '__main__':
    read_yaml('mp_login.yml')
