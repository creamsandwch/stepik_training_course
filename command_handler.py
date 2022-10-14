def command_handler():
    inp = input()
    while inp != 'End':
        print(f'Processing "{inp}" command...')
        inp = input()
    print('Good bye!')

command_handler()