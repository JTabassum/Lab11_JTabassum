# Intermediate programming practice: async and sockets.
#
# For EACH problem, work out your problem-solving OUTLINE first, then implement it (you
# may use an AI assistant to help - see the README). The async parts must actually run
# their work CONCURRENTLY (that's the whole point), not one after another.
#
# Do not rename the functions - the tests use these names.

import asyncio
import socket


async def gather_doubled(numbers):
    # Outline (write your plan here first):
    # create async helper
    # have it double one number
    # use asyncio to make it all work at once
    
    # TODO (Part 1, async): run one async task per number that returns n * 2, all
    #   CONCURRENTLY with asyncio.gather, and return the results as a list in the same
    #   order as `numbers`.
    
    async def double(number):
        await asyncio.sleep(0)
        return number *2
    tasks = [
        asyncio.create_task(double(number))
        for number in numbers
    ]
    return await asyncio.gather(*tasks)
    


async def fastest(jobs):
    # Outline:
    #  create async for one jobs delay
    # start task for (job, delay) pair
    #   Use as_completed to check the tasks in finish order.
    #   Return the label from the first completed task.
    # TODO (Part 2, async): `jobs` is a list of (label, delay) pairs. Start them all
    #   concurrently - each one just does `await asyncio.sleep(delay)` - and return the
    #   label of the FIRST job to finish. (Hint: asyncio.as_completed.)
    async def wait_for_job(label, delay):
        await asyncio.sleep(delay)
        return label

    if not jobs:
        return None

    tasks = [
        asyncio.create_task(wait_for_job(label, delay))
        for label, delay in jobs
    ]

    for completed_task in asyncio.as_completed(tasks):
        return await completed_task
        


def echo_once(host, port, message):
    # Outline:
    # create socket
    # connect to (host, port).
    # encode the message and send it.
    # receive the reply and decode it to text.
    # TODO (Part 3, sockets): open a TCP socket and connect to (host, port). Send
    #   `message` (encode it to bytes first), receive the server's reply, and return it
    #   as a string. (Hint: socket.socket, .connect, .sendall, .recv, .decode.)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((host, port))
        client.sendall(message.encode())
        reply = client.recv(1024)
        return reply.decode()


def main():
    # Optional scratch space - try the async parts here, e.g.:
    # print(asyncio.run(gather_doubled([1, 2, 3, 4])))   # [2, 4, 6, 8]
    pass


if __name__ == "__main__":
    main()
