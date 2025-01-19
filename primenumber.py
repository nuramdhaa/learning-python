def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Loop through numbers from 1 to 250
for number in range(1, 251):
    if is_prime(number):
        print(number)
