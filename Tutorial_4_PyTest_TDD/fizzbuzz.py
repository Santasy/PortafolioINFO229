def fizzBuzz(n):
    output = []
    for i in range(1, n+1):
        out = ""
        if not (i % 3):
            out += "Fizz"
        if not (i % 5):
            out += "Buzz"
        if not out:
            output.append(str(i))
        else:
            output.append(out)
    return output

def fizzBuzz2(n):
    output = []
    for i in range(1, n+1):
        out = ""
        num = str(i)
        # Asumo que basta un postfijo del mismo tipo,
        # o sea, BuzzBuzz no es necesario
        if not (i % 3) or "3" in num:
            out += "Fizz"
        if not (i % 5) or "5" in num:
            out += "Buzz"
        if not out:
            output.append(num)
        else:
            output.append(out)
    return output