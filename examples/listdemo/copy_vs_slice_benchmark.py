import timeit

# Create a list with 1 million elements
test_list = list(range(1000000))

# Benchmark .copy()
copy_time = timeit.timeit(lambda: test_list.copy(), number=100)

# Benchmark [:]
slice_time = timeit.timeit(lambda: test_list[:], number=100)

print(f"list.copy(): {copy_time:.5f} seconds")
print(f"list[:]:     {slice_time:.5f} seconds")

# Calculate the difference
diff = (slice_time - copy_time) / slice_time * 100
print(
    f"\nResult: .copy() is {abs(diff):.2f}% {'faster' if diff > 0 else 'slower'} than [:]")
