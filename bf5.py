import itertools
import hashlib
import time

# Define the given hash
# given_hash = "68a53d39ef016f3f7635e6aa86d03f89657bd470488b91589a4f051634f76044"
given_hash = input("\n  I need the hash you wan't to find the preimage of: ")

# Asking for special characters & Define a list of possible characters
sp_car = input("\n  Test with special character (Y/N)?: ")

if sp_car == 'Y' or sp_car == 'y':
    print('  Testing with special characters')
    chars = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789#%-=/\+_!?.&§~*:;<>"
else:
    print("  Testing without special characters")
    chars = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# Define a maximum length for the input
max_length = int(input("\n  Define a maximum length of characters tried (default 6): "))

# Set the time limit to 10 seconds
time_limit = int(input("\n  How much time do you got (in sec): "))

# Define a function to generate all possible combinations of characters
def generate_combinations(chars, max_length):
    # Use a generator expression to yield combinations
    yield from (''.join(combination) for length in range(1, max_length + 1) for combination in itertools.product(chars, repeat=length))

start_time = time.time()  # Get the start time

for combination in generate_combinations(chars, max_length):
    elapsed_time = time.time() - start_time  # Calculate the elapsed time
    if elapsed_time >= time_limit:
        print('\n  Your time limit of ' + str(time_limit) + ' seconds has been reached \n  I have found no matching hash.\n')
        break

    combination_hash = hashlib.sha256(combination.encode()).hexdigest()
    print(f"Testing combination: {combination}")
    if combination_hash == given_hash:
        print(f"\n I found a match: {combination} \n")

        fp = open('Knownhashes.txt', 'a')   #Add combination to known hashes list
        fp.write("\n" + given_hash + " = " + combination)
        fp.close()
        
        break
else:
    print("\n I have found no matching hash.")