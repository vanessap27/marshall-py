participants = int(input("enter the number of participants: "))
score_dict = {}

for i in range(participants):
    current_score = int(input('enter score: '))
    if current_score in score_dict:
        score_dict[current_score] += 1
    else: 
        score_dict[current_score] = 1
score_list = sorted(list(score_dict.keys()))
third = score_list[-3]
print (f"Bronze score: {third}, Number of Bronzes {score_dict[third]}")