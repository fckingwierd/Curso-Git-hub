
hola = dict()

def idk(*args,**kwargs):
    for key,value in kwargs.items():
        hola[key] = value
    print(hola)
    print(*args)



idk(1,2,3, ciudad = "hola",hola =  1, idk = "pija")


