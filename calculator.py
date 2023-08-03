import talk

def takefunction():
    first = int(input("Enter the first number "))
    sign = input("What is the sign? ")
    last = int(input("What is the second number "))
    if sign == "+":
        talk.talk(first + last)
        print(first + last)
    elif sign == "-":
        talk.talk(first - last)
        print(first - last)
    elif sign == "*":
        talk.talk(first * last)
        print(first * last)
    elif sign == "/":
        talk.talk(first / last)
        print(first / last)
    elif sign == "**":
        talk.talk(first ** last)
        print(first ** last)
    elif sign == "//":
        talk.talk(first // last)
        print(first // last)
    elif sign == "%":
        talk.talk(first % last)
        print(first % last)
    else:
        pass

takefunction()