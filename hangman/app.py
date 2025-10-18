import random
import time
import requests

def get_word_clue(word):
    """Fetches a clue for a word from the Free Dictionary API."""

    # The API URL endpoint
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

    try:
        # Make the request to the API
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.json()
            # Extract the first definition as the clue
            definition = data[0]['meanings'][0]['definitions'][0]['definition']
            part_of_speech = data[0]['meanings'][0]['partOfSpeech']

            return f"Clue: It's a {part_of_speech}. Definition: {definition}"
        else:
            # Handle cases where the word is not found (like a 404 error)
            return "Could not find a clue for this word."

    except requests.exceptions.RequestException as e:
        # Handle potential network errors
        return f"An error occurred: {e}"

print("The Hangman Project")

easy_words = [
    'the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have', 'it',
    'for', 'not', 'on', 'with', 'he', 'as', 'you', 'do', 'at', 'this',
    'but', 'his', 'by', 'from', 'they', 'we', 'say', 'her', 'she', 'or',
    'an', 'will', 'my', 'one', 'all', 'would', 'there', 'their', 'what', 'so',
    'up', 'out', 'if', 'about', 'who', 'get', 'which', 'go', 'me', 'when',
    'make', 'can', 'like', 'time', 'no', 'just', 'him', 'know', 'take', 'people',
    'into', 'year', 'your', 'good', 'some', 'could', 'them', 'see', 'other', 'than',
    'then', 'now', 'look', 'only', 'come', 'its', 'over', 'think', 'also', 'back',
    'after', 'use', 'two', 'how', 'our', 'work', 'first', 'well', 'way', 'even',
    'new', 'want', 'because', 'any', 'these', 'give', 'day', 'most', 'us', 'is'
]

# You can then use it like this:
# print(easy_words[0])  # Output: 'the'
# print(len(easy_words)) # Output: 100

# --- Let's try it out! ---
# 1. Choose a random word from the list
random_word = random.choice(easy_words)
print(f"The chosen word is: '{random_word}'")

# 2. Get the clue for that word
clue = get_word_clue(random_word)
print(clue)
