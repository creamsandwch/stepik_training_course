cards = input()
trump_suit = input()

key_list = [str(i) for i in range(6, 11)]
key_list.append('J')
key_list.append('Q')
key_list.append('K')
key_list.append('A')

card_values = {}

for i in range(len(key_list)):
    card_values[key_list[i]] = i

card_list = cards.split()

suit_1 = card_list[0][-1]
suit_2 = card_list[1][-1]

for key in card_values.keys():
    if str(key) in str(card_list[0]):
        value_1 = card_values[key]

for key in card_values.keys():
    if key in card_list[1]:
        value_2 = card_values[key]

print(f'первая карта: величина - {value_1}, масть - {suit_1}')
print(f'вторая карта: величина - {value_2}, масть - {suit_2}')
print(f'козырь - {trump_suit}')

if suit_1 == suit_2:
    if value_1 > value_2:
        output = 'First'
    elif value_1 < value_2:
        output = 'Second'
    else:
        output = 'Error'
else:
    if suit_1 == trump_suit:
        output = 'First'
    elif suit_2 == trump_suit:
        output = 'Second'
    else:
        output = 'Error'

print(output)
