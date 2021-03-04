'''Write a script that parse sample.json and outputs to console following information:'''
'''Total balances: $1,000,000
Female: $500,000.00
Male: $500,000.00
Female: $33,333.00
Male avg: $33,331.00'''

import json


def total_balances():
    total_balance = 0
    # open first:
    with open("sample.json") as my_file:
        my_file = json.load(my_file)
        for user in my_file:
            user = user["balance"]
            user = user.replace("$", "")
            user = user.replace(",", "")
            total_balance += float(user)

    total_balance = "{:,}".format(round(total_balance, 2))

    return f"Total balances: ${total_balance}"


def total_female_male():
    total_female_balance = 0
    total_male_balance = 0
    with open("sample.json") as my_file:
        my_file = json.load(my_file)
        for user in my_file:
            gender = user["gender"]
            if gender == "female":
                user = user["balance"]
                user = user.replace("$", "")
                user = user.replace(",", "")
                total_female_balance += float(user)
            else:
                user = user["balance"]
                user = user.replace("$", "")
                user = user.replace(",", "")
                total_male_balance += float(user)

    total_female_balance = "{:,}".format(round(total_female_balance, 2))
    total_male_balance = "{:,}".format(round(total_male_balance, 2))

    return f"Female: ${total_female_balance}\nMale: ${total_male_balance}"


def total_female_male_avg():
    total_female_balance_avg = 0
    total_male_balance_avg = 0
    number_of_females = 0
    number_of_males = 0
    with open("sample.json") as my_file:
        my_file = json.load(my_file)
        for user in my_file:
            gender = user["gender"]
            if gender == "female":
                number_of_females += 1
                user = user["balance"]
                user = user.replace("$", "")
                user = user.replace(",", "")
                total_female_balance_avg += float(user)
            else:
                number_of_males += 1
                user = user["balance"]
                user = user.replace("$", "")
                user = user.replace(",", "")
                total_male_balance_avg += float(user)

    total_female_balance_avg = "{:,}".format(round(total_female_balance_avg / number_of_females, 2))
    total_male_balance_avg = "{:,}".format(round(total_male_balance_avg / number_of_males, 2))

    return f"Female avg: ${total_female_balance_avg}\nMale avg: ${total_male_balance_avg}"


print(total_balances())
print(total_female_male())
print(total_female_male_avg())
