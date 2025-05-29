# Majix Find&Replace Libary#
# © Majix Co. 2025 #
# Tested for internal use only #

# Find And Replace Library
def filereplace(filepath, text_to_find, replace, reason):
    def write_to_line(file_path, line_num, text_to_write):
        with open(file_path, 'r') as file:
            lines = file.readlines()

        if 1 <= line_num <= len(lines):
            lines[line_num - 1] = text_to_write + '\n'
        elif line_num > len(lines):
            lines.extend(['\n'] * (line_num - len(lines) -1))
            lines.append(text_to_write + '\n')
        else:
            print("Invalid line number.")
            return

        with open(file_path, 'w') as file:
            file.writelines(lines)
            file.close()
    
    """
    Searches for a specific text within a file and prints the line number if found.

    Args:
        filepath (str): The path to the file to search.
        text_to_find (str): The text to search for within the file.
    """
    try:
        with open(filepath, 'r') as file:
            for line_number, line in enumerate(file, 1):
                if text_to_find in line:
                    #print(f"Text '{text_to_find}' found on line {line_number}: {line.strip()}")
                    #file.close()
                    write_to_line(filepath, line_number, replace)
                    print(reason)
    except FileNotFoundError:
        print(f"Error: File not found at '{filepath}'")
def filecheck(filepath, texttofind):
    try:
        with open(filepath, 'r') as file:
            for line_number, line in enumerate(file, 1):
                if texttofind in line:
                    #print(f"Text '{text_to_find}' found on line {line_number}: {line.strip()}")
                    #file.close()
                    return True
    except FileNotFoundError:
        print(f"Error: File not found at '{filepath}'")
        return False
def filecheck():
    print("You invoked the findtext library please follow the instructions listed on the website or use vscode intelisense to use library")
    import datetime
    year = str(datetime.datetime.now().year)
    print(f"© Majix Installer {year}")
    return