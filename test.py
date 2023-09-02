from multiprocessing import Pool, cpu_count
import time

def factorize_single(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors

def factorize(*numbers):
    start_time = time.time()
    pool = Pool(processes=cpu_count())
    result = pool.map(factorize_single, numbers)
    pool.close()
    pool.join()
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

if __name__ == "__main__":
    numbers = (128, 255, 99999, 10651060)
    result, execution_time = factorize(*numbers)
    
    print("Factorization results:")
    for i, num in enumerate(numbers):
        print(f"Number {num}: {result[i]}")

    print(f"Execution time: {execution_time} seconds")

