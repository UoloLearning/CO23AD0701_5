word = input("Enter a word: ")
length = len(word)
first_letter = word[0]
print('First Letter:',first_letter)
last_letter = word[-1]
print('Last Letter:',last_letter)

#If length is an odd number
#Dividing it by 2 will give float value
#So convert it into integer
mid = int(length/2)
middle_letter = word[mid]
print('Middle Letter:',middle_letter)
