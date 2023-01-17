donw = 0
up = 100
for i in range(1,10):
    guessed_age = int((up + donw) / 2)
    answer = input('are you ' + str (guessed_age)+"year old ?")
    if answer == 'correct':
        print("nice")
        break
    elif answer == 'less':
        up = guessed_age
    elif answer == 'more':
        donw = guessed_age
    else:
        print('wrong answer')