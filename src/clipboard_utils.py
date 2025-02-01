import pyperclip


def copy_to_clipboard(output_file: str, no_copy: bool) -> None:
    """
    Копирует содержимое файла в буфер обмена, если no_copy равно False.
    """
    if no_copy:
        print(f"Копирование содержимого {output_file} в буфер обмена отключено.")
        return

    try:
        with open(output_file, 'r', encoding='utf-8') as outfile:
            content = outfile.read()
            pyperclip.copy(content)
            print(f"Содержимое {output_file} скопировано в буфер обмена")
    except Exception as e:
        print(f"Не удалось скопировать содержимое {output_file} в буфер обмена: {e}")

