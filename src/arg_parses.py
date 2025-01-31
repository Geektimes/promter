import argparse


def parse_args():
    parser = argparse.ArgumentParser(
        description='Сохранение содержимого текстовых файлов в один файл')

    parser.add_argument('--repo_path', default='.', required=False, type=str,
                        help='Путь к папке с репозиторием')
    parser.add_argument('--output', default='output.txt', required=False, type=str,
                        help='Имя файла для сохранения содержимого')

    return parser.parse_args()
