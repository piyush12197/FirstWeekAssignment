word = input("Enter a string: ")
reversed_word = ""

for char in word:
    reversed_word = char + reversed_word

print("Reversed string:", reversed_word)

if word == reversed_word:
    print("It is a palindrome")
else:
    print("Not a palindrome")
