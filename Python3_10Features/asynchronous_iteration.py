# line_count
import asyncio
import sys
import aiofiles

# define asynchronous function
async def count_lines(filename):
    count = 0

    # async file operations
    async with aiofiles.open(filename, 'rb') as f:
        lines = aiter(f) # async iterator

        while True:
            try:
                line = await anext(lines) # async next
                count += 1
            except StopAsyncIteration: # stop if async iter done
                break
    
        print(f" {count} ", sep="", end="", flush=True)


async def all_files(filenames):
    tasks = []

    for filename in filenames:
        task = asyncio.create_task(count_lines(filename))
        tasks.append(task)
    
    # boundary between async and sync
    await asyncio.gather(*tasks)
    print()


if __name__ == '__main__':
    asyncio.run(all_files(sys.argv[1:]))
