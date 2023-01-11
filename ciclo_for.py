vowels = ["A", "E", "I", "O", "U"]
word_without_vowels = ""
user_word = input("Ingrese una palabra: ").upper()

for letter in user_word:
    if letter in vowels:
        continue
    word_without_vowels += letter
    
print(word_without_vowels, end="")