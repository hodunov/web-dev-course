import os
import random

# settings
FILE_FOLDER_NAME = 'data'
AMOUNT_OF_FILES = 1000
CWD = os.getcwd()


def generate_files(file_number):
    """
    generate files according to the task:
    In the directory there are input text files named as follows:
    in_<N>.dat, where N is a natural number. Each file consists of two lines.
    The first line contains the number denoting the action, and
    the second line contains floating point numbers separated by a space.
    The actions can be as follows:
    1 - addition
    2 - multiplication
    3 - sum of squares
    """
    os.makedirs(FILE_FOLDER_NAME, exist_ok=True)
    files_dir = os.path.join(CWD, FILE_FOLDER_NAME)
    for i in range(1, file_number + 1):
        with open(os.path.join(files_dir, f"in_{i}.dat"), "w+") as file:
            file.write(f"{random.randint(1, 3)}\n{random.uniform(1, file_number)} {random.uniform(1, file_number)}")
    return print(f"Successfully generated {file_number} files")


if __name__ == "__main__":
    generate_files(file_number=AMOUNT_OF_FILES)
