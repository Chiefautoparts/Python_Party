def stars(arr):
    for x in arr:
        print '*' * x


number = [4,6,5,2,9]

stars(number)

def moreStars(arr):
    for y in arr:
        if isinstance(y, int):
            print "*" * y
        elif isinstance(y, str):
            length = len(y)
            letter = y[0].lower()
            print letter * length

things = [4, "jeb", 1, "steve", 5, 9, "duke"]

moreStars(things)
