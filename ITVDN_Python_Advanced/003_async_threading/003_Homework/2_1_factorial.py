import time
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor


def factorial(n):
    for j in range(100_000):
        res = 1
        for i in range(1, n+1):
            res *= i
    return res


def run_by_executor(executor_class, max_workers=4):
    executor = executor_class(max_workers=max_workers)
    started = time.time()

    future1 = executor.submit(factorial, 300)
    future2 = executor.submit(factorial, 300)
    future3 = executor.submit(factorial, 300)
    future4 = executor.submit(factorial, 300)

    result = (future1.result(), future2.result(), future3.result(), future4.result(),)

    print('Result: {result}. Time for {executor}: {spent_time}'.format(
        result=None,
        executor=executor_class.__name__,
        spent_time=time.time() - started
    ))


if __name__ == '__main__':
    run_by_executor(ThreadPoolExecutor)
    run_by_executor(ProcessPoolExecutor)