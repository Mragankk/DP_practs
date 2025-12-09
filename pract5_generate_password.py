# dict_file={'a':'z','b':'boy','c':'absorb','d':'oneplus','e':'zebra'}
# num = int(input("How many words in password? "))

# # password = generate_password(dict_file, num)


# selected = random.sample(sorted(dict_file.values()), num)

# password = ' '.join(selected)
# print("\nGenerated Password:", password)


import random

def generate_password(dictionary_file, num_words=4):
    # Read all words from dictionary file
    with open(dictionary_file, 'r') as f:
        words = [line.strip() for line in f if line.strip()]

    # Randomly pick words
    selected = random.sample(words, num_words)

    # Join selected words to form a password
    password = ''.join(selected)

    return password


# ---- USER INPUT ----
dict_file = input("Enter dictionary filename (e.g., words.txt): ")
num = int(input("How many words in password? "))

password = generate_password(dict_file, num)
print("\nGenerated Password:", password)





