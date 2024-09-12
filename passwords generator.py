import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"

def password_generator(lower, upper, nums, password_length):
    all_characters_set = lower + upper + nums
    password = "".join(random.choice(all_characters_set) for i in range(password_length))
    return password

def main():
    password_length = 8 #chaange it based on how many charcters you want in the password
    for _ in range(100000000):  # change the number based on how much passwords that you want to be generated
        password = password_generator(lower, upper, numbers, password_length)
        print(f"Generated password: {password}")

if __name__ == "__main__":
    main()