# Import the itertools and hashlib modules
import itertools
import hashlib

# Define the given hash
given_hash = "68a53d39ef016f3f7635e6aa86d03f89657bd470488b91589a4f051634f76044"

# Define a list of possible characters
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# Define a maximum length for the input
max_length = 6

# Define a function to generate all possible combinations of characters
def generate_combinations(chars, max_length):
    # Use a generator expression to yield combinations
    yield from (''.join(combination) for length in range(1, max_length + 1) for combination in itertools.product(chars, repeat=length))

# Iterate over the possible combinations
for combination in generate_combinations(chars, max_length):
    print(f"Testing combination: {combination}")  # Print the combination being tested
    # Compute the hash of the combination
    combination_hash = hashlib.sha256(combination.encode()).hexdigest()
    # Compare the hash with the given hash
    if combination_hash == given_hash:
        # Print the matching combination and exit the loop
        print(f"Found a match: {combination}")
        break
else:
    print("No matching hash found.")