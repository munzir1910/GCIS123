pi = 3.14159

def circumference(r):
    circum = 2 * pi * r
    return circum

def area_circle(r):
    area = pi * r**2
    return area

def add(x, y):
    adding =  x + y
    return adding

def subtract(x, y):
    subtracting = x - y
    return subtracting

def multiply(x, y):
    multiplying = x * y
    return multiplying

def divide(x, y):
    dividing = x / y
    return dividing

def main():
    no1 = int(input("Enter first value: "))
    no2 = int(input("Enter second value: "))
    radius = int(input("Enter radius value: "))

    addResult = add(no1,no2)
    print("Addition: ",addResult)

    subResult = subtract(no1, no2)
    print("Subtraction: ",subResult)

    multiResult = multiply(no1, no2)
    print("Multiplicaton: ",multiResult)

    divResult = divide(no1, no2)
    print("Division: ",divResult)

    circumResult = circumference(radius)
    print("Circumference: ",circumResult)

    areaResult = area_circle(radius)
    print("Area :", areaResult)


main()