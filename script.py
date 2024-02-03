import random
import string
from nltk.corpus import words

# Download the NLTK words dataset
import nltk
nltk.download('words')

def get_rhyming_words(word, num_words=3):
    rhyming_words = [w for w in words.words() if w.endswith(word[-2:])]
    return random.sample(rhyming_words, min(num_words, len(rhyming_words)))

def generate_username(word_list, length=7):
    username_parts = []
    
    # Add rhyming words with a capital letter
    for _ in range(length - 1):
        word = random.choice(word_list).capitalize()
        rhyming_words = get_rhyming_words(word)
        username_parts.append(random.choice(rhyming_words).capitalize())
    
    # Add one number
    username_parts.append(str(random.randint(1000, 9999)))

    return ''.join(username_parts)

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choices(characters, k=length))

def save_credentials_to_file(username, password, filename='credentials.txt'):
    with open(filename, 'a') as file:
        file.write(f'Username: {username}, Password: {password}\n')

# List of words for username generation
word_list = ['python', 'data', 'research', 'code', 'project', 'science', 'analyze']

# Number of usernames and passwords to generate
num_accounts = 10

for _ in range(num_accounts):
    username = generate_username(word_list)
    password = generate_password()
    save_credentials_to_file(username, password)

print(f'{num_accounts} usernames and passwords generated and saved to "credentials.txt".')
