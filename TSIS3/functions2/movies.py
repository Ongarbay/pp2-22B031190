def check_IMDB(s, imdb):
    if imdb > 5.5:
        return f"{s} is a good film"
    else:
        return f"{s} is a bad film"


def sublist(imdb):
    if imdb > 5.5:
        return True
    return False


def category(category, film):
    if category == film:
        return True


def average_IMDB(imdb, sum):
    sum += imdb
    return sum


movies = [
    {
        "name": "Usual Suspects",
        "imdb": 7.0,
        "category": "Thriller"
    },
    {
        "name": "Hitman",
        "imdb": 6.3,
        "category": "Action"
    },
    {
        "name": "Dark Knight",
        "imdb": 9.0,
        "category": "Adventure"
    },
    {
        "name": "The Help",
        "imdb": 8.0,
        "category": "Drama"
    },
    {
        "name": "The Choice",
        "imdb": 6.2,
        "category": "Romance"
    },
    {
        "name": "Colonia",
        "imdb": 7.4,
        "category": "Romance"
    },
    {
        "name": "Love",
        "imdb": 6.0,
        "category": "Romance"
    },
    {
        "name": "Bride Wars",
        "imdb": 5.4,
        "category": "Romance"
    },
    {
        "name": "AlphaJet",
        "imdb": 3.2,
        "category": "War"
    },
    {
        "name": "Ringing Crime",
        "imdb": 4.0,
        "category": "Crime"
    },
    {
        "name": "Joking muck",
        "imdb": 7.2,
        "category": "Comedy"
    },
    {
        "name": "What is the name",
        "imdb": 9.2,
        "category": "Suspense"
    },
    {
        "name": "Detective",
        "imdb": 7.0,
        "category": "Suspense"
    },
    {
        "name": "Exam",
        "imdb": 4.2,
        "category": "Thriller"
    },
    {
        "name": "We Two",
        "imdb": 7.2,
        "category": "Romance"
    }
]
sub = []
for i in movies:
    print(check_IMDB(i["name"], i["imdb"]))
    if sublist(i["imdb"]) == 1:
        sub.append(i["name"])
print("Good films:")
print(sub)
print("Enter category:")
cate = input()
films = []
for i in movies:
    if category(cate, i["category"]) == 11:
        films.append(i["name"])
print("Films in this category")
print(films)
sum = 0
count = 0
csum = 0
for i in movies:
    if category(cate, i["category"]) == 1:
        csum = average_IMDB(i["imdb"], csum)
    sum = average_IMDB(i["imdb"], sum)
    count += 1
print(f"Average value of IMDB:{sum/count}")
print(f"Average value of IMDB of chosen category:{csum/count}")
