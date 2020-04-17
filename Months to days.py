month = input("Please input a month: ")
thirty_days = ["April", "June", "September", "Novemeber"]
thirty_one_days = ["January", "March", "May",
"July", "August", "October", "December"]

if month in thirty_days:
    print("30 days")

elif month in thirty_one_days:
    print("31 days")

else:
    print("28 or 29 Days")
