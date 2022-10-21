# Escreva uma classe em Python para converter um número romano em um número inteiro.

class RomanoInteiro:
    def romanToInt(self, r):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(r)):
            if i > 0 and rom_val[r[i]] > rom_val[r[i - 1]]:
                int_val += rom_val[r[i]] - 2 * rom_val[r[i - 1]]
            else:
                int_val += rom_val[r[i]]
        return int_val


print(RomanoInteiro().romanToInt('MMMCMLXXXVI'))
print(RomanoInteiro().romanToInt('MMMM'))
print(RomanoInteiro().romanToInt('L'))