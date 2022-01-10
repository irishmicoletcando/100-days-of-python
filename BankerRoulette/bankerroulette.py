import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
number_items = len(names)
choices = random.randint(0, number_items-1)
person = names[choices]
print(f"{person} is going to buy the meal today!")