import multiprocessing

def factorize_number(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def factorize(*numbers):
    result = []
    for number in numbers:
        factors = factorize_number(number)
        result.append(factors)
    return result

if __name__ == "__main__":
    numbers = (128, 255, 99999, 10651060)
    
    # Синхронна версія
    import time
    start_time = time.time()
    results_sync = factorize(*numbers)
    end_time = time.time()
    print("Синхронна версія виконана за", end_time - start_time, "секунд")
    
    # Покращена версія з паралельними обчисленнями
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count())
    start_time = time.time()
    results_async = pool.map(factorize_number, numbers)
    pool.close()
    pool.join()
    end_time = time.time()
    print("Паралельна версія виконана за", end_time - start_time, "секунд")
    
    # Перевірка результатів
    a, b, c, d = results_sync
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
