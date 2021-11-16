import time, timeit
def measure_runtime(func):
    start = time.time()
    func()
    end = time.time()
    print(end-start)
def power (limits):
    return[x**2 for x in range (limits)]

measure_runtime(lambda : power(500000))


print(timeit.timeit("[x**2 for x in range(10)]"))