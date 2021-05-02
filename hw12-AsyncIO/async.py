import os
from datetime import datetime
import asyncio
import aiofiles
from file_generator import FILE_FOLDER_NAME, CWD, AMOUNT_OF_FILES

files_dir = os.path.join(CWD, FILE_FOLDER_NAME)

all_res = []
start = datetime.now()


async def line_reader(afp):
    async with aiofiles.open(afp, 'r') as afp:
        lines = await afp.readlines()
        first_line = lines[0].strip()
        second_line = lines[1].strip()
        num_1, num_2 = [float(word) for word in second_line.split()]
        if first_line == '1':
            all_res.append(num_1 + num_2)
        if first_line == '2':
            all_res.append(num_1 * num_2)
        if first_line == '3':
            all_res.append(num_1 ** 2 + num_2 ** 2)


async def main():
    tasks = []
    for number in range(1, AMOUNT_OF_FILES + 1):
        tasks.append(line_reader(os.path.join(files_dir, f"in_{number}.dat")))
    # for task in tasks:
    #     await task
    await asyncio.gather(*tasks)

# asyncio.run(main())
loop = asyncio.get_event_loop()
loop.run_until_complete(main())

print(sum(map(float, all_res)))
end = datetime.now()
time_taken = end - start
print('Time: ', time_taken)
