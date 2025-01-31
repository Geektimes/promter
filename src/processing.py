import os
from src.ignoring import (read_gitignore,
                          should_ignore)


text_extensions = ['.txt', '.md', '.log', '.csv',
                   '.py', '.cfg', '.conf', '.json', '.yml', '.yaml']


def is_text_file(filename: str) -> bool:
    return filename.lower() == 'dockerfile' or any(filename.endswith(ext) for ext in text_extensions)


def process_folder(repo_path: str, output_file: str) -> None:
    repo_path = os.path.abspath(repo_path)
    ignore_patterns = read_gitignore(repo_path)

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for root, dirs, files in os.walk(repo_path):
            # Исключаем папки, указанные в .gitignore
            dirs[:] = [d for d in dirs if not should_ignore(
                os.path.join(root, d), ignore_patterns)]

            for file in files:
                file_path = os.path.join(root, file)
                if should_ignore(file_path, ignore_patterns):
                    continue
                if is_text_file(file):
                    try:
                        with open(file_path, 'r', encoding='utf-8') as infile:
                            content = infile.read()
                            outfile.write(f"--- {file_path} ---\n")
                            outfile.write(content)
                            outfile.write("\n" + "-"*40 + "\n\n")
                    except Exception as e:
                        print(f"Не удалось прочитать файл {file_path}: {e}")
