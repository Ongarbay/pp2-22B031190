import datetime
day = datetime.date.today()-datetime.timedelta(5)
print(f"5 days before {day}")
yesterday = datetime.date.today()-datetime.timedelta(1)
today = datetime.date.today()
tomorrow = datetime.date.today()+datetime.timedelta(1)
print(f"Yesterday:{yesterday}, Today:{today}, Tomorrow:{tomorrow}")
micro = datetime.datetime.today().replace(microsecond=0)

print("Enter a number:", end=' ')
n = int(input())
print(n*86400)