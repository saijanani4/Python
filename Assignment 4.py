
try:
    file1 = open("sample.txt","r")
    print("Reading File contents:")
    print("Line 1: ",file1.readline())
    print("Line 2: ",file1.readline())
    file1.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")

#--------------


text = input("Enter text to be written on the file : ") + "\n"
file = open("output.txt", "w")
file.write(text)
print("Data successfully written to 'output.txt' file\n")
file.close()

text_1 = input("Enter additional to be written on the file : ") + "\n"
file = open("output.txt", "a")
file.write(text_1)
print("Data successfully appended\n")
file.close()

file = open("output.txt", "r")
print("Final content of 'output.txt':")
print(file.read())
file.close()




