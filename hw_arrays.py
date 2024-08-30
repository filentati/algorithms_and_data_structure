size = int(input())
input_array = input() 
element = int(input())

array = list(map(int, input_array.split()))

counter = 0 

for el in array:
    if el == element:
        counter+=1
        
print(size - counter)