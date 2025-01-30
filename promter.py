import os
import sys
import fnmatch

text_extensions = ['.txt', '.md', '.log', '.csv', '.py', '.cfg', '.conf', '.json', '.yml']

def is_text_file(filename):
    return filename.lower() == 'dockerfile' or any(filename.endswith(ext) for ext in text_extensions)

def read_gitignore(root_path):
    gitignore_path = os.path.join(root_path, '.gitignore')
    ignore_patterns = []
    if os.path.exists(gitignore_path):
        with open(gitignore_path, 'r', encoding='utf-8') as gitignore_file:
            for line in gitignore_file:
                line = line.strip()
                if line and not line.startswith('#'):
                    ignore_patterns.append(line)
    return ignore_patterns

def should_ignore(path, ignore_patterns):
    for pattern in ignore_patterns:
        if fnmatch.fnmatch(os.path.basename(path), pattern):
            return True
        if os.path.isdir(path) and fnmatch.fnmatch(path, pattern):
            return True
    return False

def process_folder(folder_path, output_file):
    root_path = os.path.abspath(folder_path)
    ignore_patterns = read_gitignore(root_path)

    with open(output_file, 'w', encoding='utf-8') as outfile:
        for root, dirs, files in os.walk(folder_path):
            # Исключаем папки, указанные в .gitignore
            dirs[:] = [d for d in dirs if not should_ignore(os.path.join(root, d), ignore_patterns)]

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

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python promter.py <путь_к_папке>")
        sys.exit(1)

    folder_path = sys.argv[1]
    output_file = "output.txt"

    if not os.path.isdir(folder_path):
        print(f"Указанный путь не является директорией: {folder_path}")
        sys.exit(1)

    process_folder(folder_path, output_file)
    print(f"Содержимое всех текстовых файлов сохранено в {output_file}")