import os
from datetime import datetime
from file_generator import FILE_FOLDER_NAME, CWD, AMOUNT_OF_FILES

files_dir = os.path.join(CWD, FILE_FOLDER_NAME)

all_res = []
start = datetime.now()


def line_reader(afp):
    with open(afp, 'r') as afp:
        first_line = afp.readline()
        first_line = first_line.strip()
        second_line = afp.readline()
        num_1, num_2 = [float(word) for word in second_line.split()]
        if first_line == '1':
            all_res.append(num_1 + num_2)
        if first_line == '2':
            all_res.append(num_1 * num_2)
        if first_line == '3':
            all_res.append(num_1 ** 2 + num_2 ** 2)


for number in range(1, AMOUNT_OF_FILES + 1):
    line_reader(os.path.join(files_dir, f"in_{number}.dat"))

print(sum(map(float, all_res)))

end = datetime.now()
time_taken = end - start

print('Time: ', time_taken)
