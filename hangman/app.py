import random
import time
import requests
import string
from rich.console import Console

def animate_hangman_intro_single_line():
    """
    Animates 'HANGMAN' on a single line with a flickering slot-machine effect.
    """
    console = Console()
    target_word = "Let's play HANGMAN!"

    # This will hold the parts of the word that are already "locked in"
    revealed_word_parts = []

    # 1. Loop through each letter we need to reveal (H, A, N, G, M, A, N)
    for i in range(len(target_word)):
        start_time = time.time()

        # 2. Flicker random characters in the current position for a short duration
        while time.time() - start_time < 0.4: # Flicker for 0.4 seconds
            # The string to print: already revealed letters + the flickering character
            flickering_part = random.choice(string.ascii_uppercase + "#$%*")

            # Join the revealed parts and add the new flickering character
            # The [1:] removes the space that join would add at the start
            display_text = "".join(revealed_word_parts) + f"[bold yellow]{flickering_part}[/bold yellow]"

            # The key is end='\r'. This returns the cursor to the start of the line.
            console.print(display_text, end='\r')
            time.sleep(0.05)

        # 3. Lock in the correct letter and add it to our list of revealed parts
        correct_letter = target_word[i]
        revealed_word_parts.append(f"[bold bright_green]{correct_letter}[/bold bright_green]")

        # Display the line with the newly locked-in letter
        final_display_text = "".join(revealed_word_parts)
        console.print(final_display_text, end='\r')
        time.sleep(0.15) # Pause briefly after revealing a letter

    # 4. After the loop, print a newline to move to the next line for good.
    print()
    print() # Add an extra line for spacing
    console.print("[cyan]Welcome to the classic word guessing game![/cyan]")
    console.print("[dim]Press Enter to start...[/dim]")
    input()
    console.clear()


# --- To run the intro ---
if __name__ == "__main__":
    animate_hangman_intro_single_line()
    print("Game starts now!")
    # Your game logic follows here...

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
lengthword = len(random_word)
clue = get_word_clue(random_word)
print(clue)
print(f"It is also a {lenghtword} letter word.")

human_choice = input("Guess your first letter: ").lower()
print(human_choice)


#print(lengthword)
# 2. Get the clue for that word
def design():
    for i in random_word:
        if human_choice == i:
            print("you indeed got a letter")
        else:
            print("Paywall...")


#design()
