
import threading

lock = threading.Lock()

def thread_safe_function():
    with lock:
        # Critical section of code
        print("Thread-safe operation")

threads = [threading.Thread(target=thread_safe_function) for _ in range(10)]
print(threads)
for t in threads:
    t.start()

for t in threads:
    t.join()

