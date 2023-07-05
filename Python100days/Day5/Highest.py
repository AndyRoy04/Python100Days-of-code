print("Get the Highest score !!!")
scores = input("\nEnter the lsit of scores: ").split()

for a_score in range(len(scores)):
    scores[a_score] = int(scores[a_score])

highest_score = 0
for another_score in scores:
    # if another_score > Average:
    if another_score > highest_score:
        highest_score = another_score
print(f'The highest Score is : {highest_score}')