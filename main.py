from analyzer import load_scores
from analyzer import calculate_average


csv_path = "data/scores.csv"
scores = load_scores(csv_path)
average = calculate_average(scores)

print('平均点：', average)
