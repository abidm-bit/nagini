import asyncio
import concurrent.futures

# this program prints the word test 1000 times

def blocking_io():
    with open('test.txt', 'w') as f:
        for i in range(10000):
            f.write('test ')
    return 'IO task completed.'

async def main():
    loop = asyncio.get_event_loop()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        result = await loop.run_in_executor(executor, blocking_io)
        print(result)

if __name__ == "__main__":
    asyncio.run(main())


""" 
** Which of the following changes will NOT allow the program to work as intended **

Pick ONE option

- Replace concurrent.futures.ThreadPoolExecutor() 
  with concurrent.futures.ProcessPoolExecutor()

- Replace loop = asyncio.get_event_loop() with
   loop = asyncio.new_event_loop().

- Replace result = away loop.run_in_executor(executor,blocking_io) with 
  result = blocking_io(). 

- Replace asyncio.run(main()) with main().

"""