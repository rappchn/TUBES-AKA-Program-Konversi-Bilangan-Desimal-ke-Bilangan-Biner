import time

# Iterative version
def decimal_to_binary_iterative(n):
    if n == 0:
        return "0"
    binary = ""
    while n > 0:
        binary = str(n % 2) + binary
        n = n // 2
    return binary

# Pengujian dengan berbagai ukuran masukan
for n in [1, 10, 100, 1000, 10000]:
    # Iterative
    start_iterative = time.time()
    binary_iterative = decimal_to_binary_iterative(n)
    end_iterative = time.time()
    time_iterative = (end_iterative - start_iterative) * 1e9  # Convert to nanoseconds

    # Output hasil pengujian
    print(f"n = {n}: Binary = {binary_iterative} Time = {int(time_iterative)} ns")