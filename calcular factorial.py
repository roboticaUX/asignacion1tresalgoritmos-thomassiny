n= int(input("Ingrese un numero: "))
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print("El factorial: " + str(n) + " es " + str(factorial(n)))