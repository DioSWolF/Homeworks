from datetime import datetime
from multiprocessing import Pool
import os
from time import sleep

def factorize(*number):
    print(f"pid={os.getpid()}")
    for num in number:

        i = 1
        a = []
        while i <= num:

            if num % i == 0:
                a.append(i)
            i += 1
    # sleep(2)
    # raise NotImplementedError()
    return a



if __name__ == '__main__':
    time_start = datetime.now()
    with Pool(processes=4) as pool:
        # a, b, c, d  = factorize(128, 255, 99999, 10651060)
        a, b, c, d  = pool.map(factorize, (99999999, 99999999, 99999999, 99999999))
    time_end = datetime.now() - time_start
    print(time_end)
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]