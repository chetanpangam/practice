import multiprocessing

def print_numbers():
    for i in range(20):
        print(i)

if __name__ == "__main__":
    process1 = multiprocessing.Process(target=print_numbers)
    process2 = multiprocessing.Process(target=print_numbers)

    process1.start()
    process2.start()

    process1.join()
    process2.join()