
import csv

def load_scores(file_path):

    new_list = []

    with open(file_path, encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            num = int(row["score"])
            row["score"] = num
            hours = float(row["study_hours"])
            row["study_hours"] = hours
            topics = int(row["weak_topics"])
            row["weak_topics"] = topics
            row["passed"] = row["passed"] == "True"
            new_list.append(row)


        if len(new_list) == 0:
            raise ValueError("CSVにデータがありません")

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

        if current_score:
            count += 1

    return count

def calculate_pass_rate(scores):

    passed_count = count_passed_exams(scores)
    passed = passed_count / len(scores) * 100

    return passed

def get_latest_score(scores):

    last_score = scores[-1]
    return last_score["score"]


def calculate_score_change(scores):

    score = len(scores)

    if score < 2:
        return None
    else:
        last_score = scores[-1]["score"]
        prev_score = scores[-2]["score"]
        return last_score - prev_score

def filter_high_scores(scores):

    high_scores = []

    for row in scores:
        if row["score"] >= 70:
            high_scores.append(row)

    return high_scores

def calculate_points_to_pass(scores, passing_score=70):

    last_score = get_latest_score(scores)

    if last_score >= passing_score:
        return 0
    else:
        return passing_score - last_score


def append_score(file_path, score_data):

    fieldnames = ("exam", "score", "study_hours", "weak_topics", "passed")

    with open(file_path, mode='a', encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(score_data)


class ExamAnalyzer:
    def __init__(self, scores):
        self.scores = scores

    def get_average(self):
        return calculate_average(self.scores)

    def get_highest_score(self):
        return find_highest_score(self.scores)

    def get_lowest_score(self):
        return find_lowest_score(self.scores)

    def get_passed_count(self):
        return count_passed_exams(self.scores)

    def get_pass_rate(self):
        return calculate_pass_rate(self.scores)

    def get_latest_exam_score(self):
        return get_latest_score(self.scores)

    def get_score_change(self):
        return calculate_score_change(self.scores)

    def get_high_scores(self):
        return filter_high_scores(self.scores)

    def get_points_to_pass(self):
        return calculate_points_to_pass(self.scores)
