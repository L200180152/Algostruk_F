def rerata(b) :
    x = 0
    y = 0
    for i in b :
        x += 1
        y = y + i
        x = float(x)
        y = float(y)
    return(y/x)
