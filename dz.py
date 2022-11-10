import multiprocessing
import sys
import math


def quadrate(num: int) -> int:
    return num*num


if __name__ == "__main__":
    with multiprocessing.Pool(multiprocessing.cpu_count()) as m:
        mas = m.map(quadrate, [int(sys.argv[1]), int(sys.argv[2])])
    print(math.sqrt(int(mas[0]+mas[1])))
