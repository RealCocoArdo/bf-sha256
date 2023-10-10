import itertools
import hashlib
import time

# Define the given hash
given_hash = "68a53d39ef016f3f7635e6aa86d03f89657bd470488b91589a4f051634f76044"

# Define a list of possible characters
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# Define a maximum length for the input
max_length = 6

# Set the time limit to 10 seconds
time_limit = 100

# Define a function to generate all possible combinations of characters
def generate_combinations(chars, max_length):
    # Use a generator expression to yield combinations
    yield from (''.join(combination) for length in range(1, max_length + 1) for combination in itertools.product(chars, repeat=length))

start_time = time.time()  # Get the start time

for combination in generate_combinations(chars, max_length):
    elapsed_time = time.time() - start_time  # Calculate the elapsed time
    if elapsed_time >= time_limit:
        print("Time limit reached")
        break

    combination_hash = hashlib.sha256(combination.encode()).hexdigest()
    print(f"Testing combination: {combination}")
    if combination_hash == given_hash:
        print(f"Found a match: {combination}")
        break
else:
    print("No matching hash found.")