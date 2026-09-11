from analyzer import load_scores
from analyzer import calculate_average
from analyzer import find_highest_score

csv_path = "data/scores.csv"
scores = load_scores(csv_path)
average = calculate_average(scores)
highest_score = find_highest_score(scores)
print("最高点:", highest_score)
print('平均点:', average)
