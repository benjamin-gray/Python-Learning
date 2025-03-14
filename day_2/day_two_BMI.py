#BMI Calc
height = 1.65 
weight = 84

bmi = weight / height ** 2

print(bmi)
print(int(bmi)) #this will give the integer part of the BMI, this will round down the BMI to the nearest integer
print(round(bmi)) #this will give the rounded BMI to the nearest integer
print(round(bmi, 2)) #this will give the rounded BMI to 2 decimal places

score = 0
#user scores point
score += 1 #this will add 1 to the score
print(score) #this will give the current score, which is 1

#user loses point
score -= 1 #this will subtract 1 from the score
print(score) #this will give the current score, which is 0

#user scores 10 points
score += 10 #this will add 10 to the score

#fstring
print(f"Your score is {score}") #this will give the current score, which is 10

score=0
height=1.8
is_Winning=False

print(f"Your height is {height} and your score is {score} and you are {'winning' if is_Winning else 'losing'}") #this will give the current height, score and winning status