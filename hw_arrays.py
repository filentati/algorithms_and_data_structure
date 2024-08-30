def move_zeros_to_end(arr):
    new_array = []
    counter = 0 
    
    for el in arr:
        if el == 0:
            counter += 1
        else:
            new_array.append(el)
            
    new_array.extend([0]*counter)
    return ' '.join(map(str, new_array))


size = int(input())
input_array = input() 

array = list(map(int, input_array.split()))

print(move_zeros_to_end(array))

