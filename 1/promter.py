import os
import sys
from src.arg_parses import parse_args
from src.processing import process_folder


if __name__ == "__main__":
    args = parse_args()
    repo_path = args.repo_path
    output_file = args.output

    if not os.path.isdir(repo_path):
        print(f"Указанный путь не является директорией: {repo_path}")
        sys.exit(1)

    process_folder(repo_path, output_file)
    print(f"Содержимое всех текстовых файлов сохранено в {output_file}")
    
    
