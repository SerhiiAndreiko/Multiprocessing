from multiprocessing import Pool, cpu_count

def factorize_single(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def factorize(*numbers):
    pool = Pool(processes=cpu_count())
    result = pool.map(factorize_single, numbers)
    pool.close()
    pool.join()
    return result

if __name__ == "__main__":
    a, b, c, d = factorize(128, 255, 99999, 10651060)
    print(a)
    print(b)
    print(c)
    print(d)
