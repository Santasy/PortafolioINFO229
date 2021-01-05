def diamond(car):
    if car == "A": return ["A"] # Simplest
    base = ord('A')
    l = ord(car) - base + 1 # 3
    line = " " * (l-1) + "A" # first
    output = []
    output.append(line)
    for i in range(1, l): # 1 2
        c = chr(base+i)
        line = " " * (l-i-1) + c # first char
        line += " " * (i*2-1) + c # second char
        output.append(line)
    nlist = output[:-1]
    nlist.reverse()
    output.extend(nlist)
    return output