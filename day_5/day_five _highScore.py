#coding challenge High Score

# You are going to write a program that calculates the highest score from a List of scores.

student_scores = [180, 124, 165, 173, 189, 169, 146, 199]

total_student_score = sum(student_scores)
print(total_student_score)  

sum = 0

for score in student_scores: # this is the for loop that will iterate through the list of student scores and is what the sum function is doing
    sum += score

print(sum)

max_score = 0
for score in student_scores:
    if score > max_score:
        max_score = score
print(max_score)