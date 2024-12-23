import time

# Recursive version
def decimal_to_binary_recursive(n):
    if n == 0:
        return ""
    return decimal_to_binary_recursive(n // 2) + str(n % 2)

# Pengujian dengan berbagai ukuran masukan
for n in [1, 10, 100, 1000, 10000]:
    # Recursive
    start_recursive = time.time()
    binary_recursive = decimal_to_binary_recursive(n)
    end_recursive = time.time()
    time_recursive = (end_recursive - start_recursive) * 1e9  # Convert to nanoseconds

    # Output hasil pengujian
    print(f"n = {n}: Binary = {binary_recursive} Time = {int(time_recursive)} ns")
    
    