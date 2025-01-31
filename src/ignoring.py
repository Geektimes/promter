import os
import fnmatch


def read_gitignore(repo_path: str) -> list[str]:
    gitignore_path = os.path.join(repo_path, '.gitignore')
    ignore_patterns = []

    try:
        with open(gitignore_path, 'r', encoding='utf-8') as gitignore_file:
            for line in gitignore_file:
                line = line.strip()
                if line and not line.startswith('#'):
                    ignore_patterns.append(line.rstrip('/'))

    except FileNotFoundError:
        print(f"Файл {gitignore_path} не найден.")
    except OSError as e:
        print(f"Ошибка при чтении {gitignore_path}: {e}")

    return ignore_patterns


def should_ignore(repo_path: str, ignore_patterns: list[str]) -> bool:
    for pattern in ignore_patterns:
        if fnmatch.fnmatch(os.path.basename(repo_path), pattern):
            return True
        if os.path.isdir(repo_path) and fnmatch.fnmatch(repo_path, pattern):
            return True
    return False
