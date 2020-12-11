def binary_seach(numbers,number_to_find,low,high):
    if low > high:
        return False
    mid = (low + high) // 2


    if numbers[mid] == number_to_find:
        return True
    
    if numbers[mid] < number_to_find:
        return binary_seach(numbers,number_to_find,mid + 1, high)
    
    else:
        return binary_seach(numbers,number_to_find,low, mid - 1)



if __name__ == "__main__":
    numbers = [1,3,6,7,9,13,16,18,19,21,22,25,27,30]
    number_to_find = int(input("Que numero quieres encontrar?: "))
    result = binary_seach(numbers,number_to_find,0,len(numbers) - 1)
    if result:
        print("El numero que ingresaste esta en la lista")
    else:
        print ("El numero no esta en la lista")
    
