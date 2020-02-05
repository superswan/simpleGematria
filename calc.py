import string

#gets letter position value using Python string module
def getValue(l):
    return string.ascii_lowercase.index(l)+1

#Loops and sums the value using getValue()
def calcGematria(word):
    total = 0
    if word.isalpha():
        for letter in word:
            total = total+getValue(letter)
    else:
        raise Exception("String must only contain letters")
    return total

user_input = input("Please enter a word or phrase you would like to find the simple english gematria of: ")
print(f"Your word's simple english gematria sums to: {calcGematria(user_input)}"

	
	



