import os
from datetime import datetime
import asyncio
import aiofiles
from file_generator import FILE_FOLDER_NAME, CWD, AMOUNT_OF_FILES

files_dir = os.path.join(CWD, FILE_FOLDER_NAME)

RESULT = []


async def line_reader(afp):
    async with aiofiles.open(afp, 'r') as afp:
        lines = await afp.readlines()
        first_line = lines[0].strip()
        second_line = lines[1].strip()
        num_1, num_2 = [float(word) for word in second_line.split()]
        if first_line == '1':
            RESULT.append(num_1 + num_2)
        if first_line == '2':
            RESULT.append(num_1 * num_2)
        if first_line == '3':
            RESULT.append(num_1 ** 2 + num_2 ** 2)


async def main():
    tasks = []
    for number in range(1, AMOUNT_OF_FILES + 1):
        tasks.append(line_reader(os.path.join(files_dir, f"in_{number}.dat")))
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    start = datetime.now()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    sum_result = sum(map(float, RESULT))
    with open('out.dat', 'w') as out_file:
        out_file.write(str(sum_result))
    end = datetime.now()
    time_taken = end - start
    print('Time: ', time_taken)
