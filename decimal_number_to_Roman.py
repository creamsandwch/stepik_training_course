class DecimalToRoman:
    inp_num: str

    def transfer(inp_num: str):

        letters = {
            1000: 'M',
            900: 'CM',
            500: 'D',
            400: 'CD',
            100: 'C',
            90: 'XC',
            50: 'L',
            40: 'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4: 'IV',
            1: 'I'
        }
        num = int(inp_num)

        while num > 0:
            for key in letters.keys():
                out_num = (num - num % key) // key
                print(
                    f'{out_num * letters[key]}',
                    end=''
                )
                num %= key


DecimalToRoman.transfer(input().strip())