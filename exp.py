table = {'Holy Grail': '1975',
         'Life of Brian': '1979',
         'The Meaning of Life': '1983'}

print(title for (title, year) in table.items() if year == '1975')