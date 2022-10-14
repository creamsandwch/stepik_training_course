#recursive func that counts elements in a list:

def rec_count(list):
    if list == []:
        return 0
    else:
        return 1 + rec_count(list[1:])

