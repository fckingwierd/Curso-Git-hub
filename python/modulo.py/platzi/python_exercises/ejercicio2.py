def is_prime (number):
    if number < 2:
        return False
    elif number == 2:
        return True
    elif number > 2 and number % 2 == 0:
        return False
    else:
        for i in range(3,5):
            if number % i == 0:
                return False
    return True

def run():
    number = int(input("Escribe un numero: "))
    result = is_prime(number)
    if result:
        print("Tu numero es primo")
    else:
        print ("Tu numero no es primo")
run ()