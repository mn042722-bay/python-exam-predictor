from analyzer import load_scores
from analyzer import calculate_average
from analyzer import find_highest_score
from analyzer import find_lowest_score
from analyzer import count_passed_exams

csv_path = "data/scores.csv"
scores = load_scores(csv_path)
average = calculate_average(scores)
highest_score = find_highest_score(scores)
lowest_score = find_lowest_score(scores)
count_passed = count_passed_exams(scores)

print("最高点:", highest_score)
print("最低点:", lowest_score)
print('平均点:', average)
print('合格回数:', count_passed)
