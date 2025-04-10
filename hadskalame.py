import random
def word_guess_game():
    words = ["python", "programming", "developer", "computer", "keyboard"]
    secret_word=random.choice(words)
    guessed_word=['_'for _ in secret_word]
    print('kalame hadsi :'+' '.join(guessed_word))
    while '_'in guessed_word:
        guessed=input('kalame khod ra vared kon : ').lower()
        if len(guessed)!=1 or not guessed.isalpha():
            print('lotfan faqat yek harf vared kon')
            continue
        if guessed in secret_word:
            for index,letter in enumerate(secret_word):
                if letter==guessed:
                    guessed_word[index]=guessed
            print("Kalame hadsi: " + " ".join(guessed_word))
        else:
            print('eshtebah dobare hads bezan')
    print(f"Afarin! Dorost hads zadi. Kalame '{secret_word}' bod.")

word_guess_game()
   

    
    
    



