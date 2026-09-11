
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
            new_list.append(row)

    return new_list
