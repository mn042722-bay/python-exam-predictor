from analyzer import load_scores
from analyzer import calculate_average
from analyzer import find_highest_score
from analyzer import find_lowest_score
from analyzer import count_passed_exams
from analyzer import calculate_pass_rate
from analyzer import get_latest_score
from analyzer import calculate_score_change
from analyzer import filter_high_scores

csv_path = "data/scores.csv"
scores = load_scores(csv_path)
average = calculate_average(scores)
highest_score = find_highest_score(scores)
lowest_score = find_lowest_score(scores)
count_passed = count_passed_exams(scores)
calculate_pass = calculate_pass_rate(scores)
last_score = get_latest_score(scores)
change_score = calculate_score_change(scores)
high_scores = filter_high_scores(scores)

print("最高点:", highest_score)
print("最低点:", lowest_score)
print('平均点:', average)
print('合格回数:', count_passed)
print(f'合格率: {calculate_pass}%')
print('最新スコア:', last_score)
print(f'前回比: {change_score:+}')
print('70点以上の模試:', high_scores)
