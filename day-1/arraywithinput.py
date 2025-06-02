
# declare empty array

use_numbers=[]

# ask the user to enter the range

data= int(input('How many numbers you wana add ?  '))

for i in range(data):
    num = int(input(f"Enter number {i+1} "))
    use_numbers.append(num)
print(f"The Array Value is {use_numbers} ")

for num in use_numbers:
    if(num%2==0):
        print(f"{num} is even number")
    else:
        print(f"{num} is odd number")
total =0
for data in use_numbers:
  
    total +=num
print(f"total is {total} ")




