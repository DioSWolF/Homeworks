from collections import defaultdict
from datetime import datetime


users = {
            "Keyt" : "1994/08/09",
            "Atrox" : "2013/08/12",
            "Milla" : "2022/08/12",
            "Pyke" : "2012/08/08",
            "Kamilla" : "1976/06/08"
}

def get_birthdays_per_week(users): 
    birth = defaultdict(list)
    now = datetime.now()
    i = 0
    while i < 8:
        for name, birth_day in users.items():
            key_birth = (datetime.strptime(birth_day, "%Y/%m/%d"))
            date_birthday = datetime(year=now.year, month =key_birth.month, day = key_birth.day)
            now_birth = (datetime(year = now.year, month = now.month, day = now.day + i)).strftime("%m/%d")
            if now_birth in date_birthday:
                date_birthday = datetime(year=now.year, month =key_birth.month, day = key_birth.day).strftime("%A")
                birth[date_birthday].append(name)
        i += 1
    birth["Monday"].extend(birth["Sunday"])
    birth["Monday"].extend(birth["Saturday"]) 
    birth["Sunday"].clear()
    birth["Saturday"].clear()
    for key, value in birth.items():
        if len(value) <= 0:
            continue
        print(key, end=": ")
        print(*value, sep=", ")

get_birthdays_per_week(users)