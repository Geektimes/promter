import os
import sys
from src.arg_parses import parse_args
from src.processing import process_folder
from src.clipboard_utils import copy_to_clipboard


if __name__ == "__main__":
    args = parse_args()
    repo_path = args.repo_path
    output_file = args.output
    no_copy = args.no_copy

    if not os.path.isdir(repo_path):
        print(f"Указанный путь не является директорией: {repo_path}")
        sys.exit(1)

    process_folder(repo_path, output_file)
    print(f"Содержимое всех текстовых файлов сохранено в {output_file}")

    copy_to_clipboard(output_file, no_copy)

