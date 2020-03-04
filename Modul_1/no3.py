def jumhurufvokal() :
    jv = input("Masukkan Kata:")
    b = len(jv)
    a = 0
    for i in jv :
        if (i=='A' or i=='a' or i=='E' or i =='e' or i=='I' or i=='i' or i=='O' or i=='o' or i=='U' or i=='u'):
            a += 1
    return b,a

def jumhurufkonsonan() :
    jk = input("Masukkan Kata:")
    b = len(jk)
    a = 0
    for i in jk :
        if (i=='A' or i=='a' or i=='E' or i =='e' or i=='I' or i=='i' or i=='O' or i=='o' or i=='U' or i=='u'):
            a += 1
    return b,b-a
