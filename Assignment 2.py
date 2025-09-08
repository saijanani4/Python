x= int(input("Enter a number:"))

if x%2 == 0:
    print(x,"is an even number.")
else:
    print(x, "is an odd number.")


#--------------
total = 0

for i in range(1,51):
 total = total + i
print( "The sum of the numbers from 1 to 50 is", total)
