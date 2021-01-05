def numberToRoman(num):
    dicc = {
        1000: 'M',
        900: "CM",
        500: 'D',
        400: "CD",
        100: 'C',
        90: "XC",
        50: 'L',
        40: "XL",
        10: 'X',
        9: "IX",
        5: 'V',
        4: 'IV',
        1: 'I'
    }
    stack = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    ans = ""
    acum = num
    while acum > 0:
        if acum < stack[0]:
            stack = stack[1:]
        else:
            ans += dicc[stack[0]]
            acum -= stack[0]
    return ans

def romanToNumber(numeral):
    dicc = {
        'M': 1000,
        "CM": 900,
        'D': 500,
        "CD": 400,
        'C': 100,
        "XC": 90,
        'L': 50,
        "XL": 40,
        'X': 10,
        "IX": 9,
        'V': 5,
        'IV': 4,
        'I': 1
    }
    sections = []
    temp = ""
    l = len(numeral)
    # Comparo pos i con i+1
    for i in range(l-1):
        a = dicc[numeral[i]]
        b = dicc[numeral[i+1]]
        temp += numeral[i]
        if a >= b:
            sections.append(temp)
            temp = ""
    acum = 0
    for sec in sections:
        print(sec)
        acum += dicc[sec]
    if temp:
        acum += dicc[numeral[-2:]]
    else:
        acum += dicc[numeral[-1]]
    return acum