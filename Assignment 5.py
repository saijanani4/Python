
student ={'John': 89, 'Alice': 95, 'Fred': 87.5, 'Bob': 89.3, 'Sam': 75 }
key = input("Enter the student's name: ")
score = student.get(key)
if score is not None:
    print(f"{key}'s score:", score)
else:
    print("Student not found.")

#-----------

first_list = list(range(1,11))
extract_list = first_list[0:5]
reversed_list = extract_list[::-1]

print("Original List: " ,first_list)
print("The Extracted List: ", extract_list)
print("The Reversed List: ", reversed_list)




