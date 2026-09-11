
import csv
import os

# 実行しているスクリプトのディレクトリを取得
base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "data", "scores.csv")

def load_scores(file_path):

    new_list = []

    with open(file_path, encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            num = int(row["score"])
            row["score"] = num
            new_list.append(row)

    return new_list

def calculate_average(scores):

    total = 0

    for row in scores:
        point = row["score"]
        total += point

    average = total / len(scores)

    return average

def find_highest_score(scores):

    high_score = scores[0]["score"]

    for row in scores:

        current_score = row["score"]

        if current_score > high_score:
            high_score = current_score

    return high_score


def find_lowest_score(scores):

    low_score = scores[0]["score"]

    for row in scores:

        current_score = row["score"] 

        if current_score < low_score:
            low_score = current_score

    return low_score

def count_passed_exams(scores):

    count = 0

    for row in scores:
        current_score = row["passed"]

        if current_score == "True":
            count += 1

    return count

def calculate_pass_rate(scores):

    passed_count = count_passed_exams(scores)
    passed = passed_count / len(scores) * 100

    return passed