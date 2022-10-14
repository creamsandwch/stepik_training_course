def get_int(
        end_message: str = 'Thank you.',
        start_message: str = 'Input int number:',
        error_message: str = 'Wrong value. Input int number:'
) -> int:
    flag_1 = 0
    flag_2 = 0
    print(start_message)
    while not flag_1:
        inp = input().strip()
        if inp != '':
            if inp[0] == '-':
                if inp[1:].find('-'):
                    inp = inp[1:]
                    flag_2 = 1
            if inp.isdigit():
                print(end_message)
                return int(f'{flag_2 * "-"}{inp}')
                flag_1 = 1
            else:
                print(error_message)
        else:
            print(error_message)



