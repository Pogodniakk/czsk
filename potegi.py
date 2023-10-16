def potegowanie_szybkie(a, n):
    w = 1  

    while n > 0: 
        if n % 2 == 1:  
            w *= a  

        a *= a 
        n //= 2  

    return w  

a = 6
n = 10
wynik = potegowanie_szybkie(a, n)
print(f"{a}^{n} = {wynik}")