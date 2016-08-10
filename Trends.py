from pytrends.pyGTrends import pyGTrends
import csv
import random
import os

category = input("Choose a category (Politics, Sport, Science, History, Music, Celebrities, Random (18+)): ").capitalize()

term = random.choice(open(category + ".txt").read().split())

attempt1 = term + " " + input(term + " - Player 1: ")
attempt2 = term + " " + input(term + " - Player 2: ")
attemptStr = attempt1 + ", " + attempt2
score1 = 0
score2 = 0

print(attemptStr)

google_username = "britishracinggreen111@gmail.com"
google_password = "bOLtPpK7ehWK"
path = ""

# connect to Google
connector = pyGTrends(google_username, google_password)

# make request
connector.request_report(attemptStr, date="today 3-m")

# download report file
connector.save_csv(path, attemptStr)

# open report file
report = open(attemptStr + ".csv")
reportReader = csv.reader(report)

error = 1
# sum score
for row in reportReader:
    # sum scores for rows 10 to 90 in columns 2 and 3
    try:
        print(int(row[1]), int(row[2]))
        error = 0
        score1 += int(row[1])
        score2 += int(row[2])
    except Exception as e:
        if 0 == error:
            break
        error = 1
        print(e, "Exception")  # or whatever kind of logging you want
        pass


maxScore = max(score1, score2)
if maxScore != 0:
    score1 = round((score1/maxScore*100))
    score2 = round((score2/maxScore*100))

print(attempt1 + ": " + str(score1))
print(attempt2 + ": " + str(score2))

if score1 > score2:
    print("Player 1 wins!")
elif score1 < score2:
    print("Player 2 wins!")
else:
    print("Draw!")

os.remove(attemptStr+".csv")
