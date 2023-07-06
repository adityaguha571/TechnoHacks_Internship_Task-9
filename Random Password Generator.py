import random
import string

def generate_password(length, include_digits=True, include_punctuation=True):
    characters = string.ascii_letters
    if include_digits:
        characters += string.digits
    if include_punctuation:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    while True:
        length = int(input("Enter the length of your Password: "))
        password = generate_password(length, include_digits=True, include_punctuation=True)
        print("Generated Password:", password)

        choice = input("do you want another password? (Y/N): ")
        if choice.lower() != "y":
            break
