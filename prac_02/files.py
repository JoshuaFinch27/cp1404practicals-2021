"""
CP1404/CP5632 - Practical - Suggested Solution
Quick file opening/writing/reading exercises
"""

# Program 1
out_file = open("name.txt", "w")
name = input("Enter Name: ")
print(name, file=out_file)
out_file.close()

# Program 2
in_file = open("name.txt", "r")
name = in_file.read().strip()
print("Your name is ", name)
in_file.close()

# Program 3
in_file = open("numbers.txt", "r")
first_number = int(in_file.readline())
second_number = int(in_file.readline())
print(first_number + second_number)
in_file.close()

# Program 4
in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
print(total)
in_file.close()








