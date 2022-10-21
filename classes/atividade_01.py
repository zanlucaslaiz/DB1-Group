# Escreva uma classe em Python para converter um número inteiro em um numeral romano.

class InteiroRomano:
    def intToRoman(self, n):
        val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        syb = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    
        roman = ''
        i = 0
        while n > 0:
            for _ in range(n // val[i]):
                roman += syb[i]
                n -= val[i]
            i += 1
        return roman


print(InteiroRomano().intToRoman(1))
print(InteiroRomano().intToRoman(4000))
