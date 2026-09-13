from analyzer import load_scores
from analyzer import calculate_average
from analyzer import find_highest_score
from analyzer import find_lowest_score
from analyzer import count_passed_exams
from analyzer import calculate_pass_rate
from analyzer import get_latest_score
from analyzer import calculate_score_change
from analyzer import filter_high_scores
from analyzer import calculate_points_to_pass
from analyzer import append_score


csv_path = "data/scores.csv"

try:
    scores = load_scores(csv_path)
except FileNotFoundError:
    print("CSVファイルが見つかりません")
except ValueError as error:
    print(error)
else:
    
    average = calculate_average(scores)
    highest_score = find_highest_score(scores)
    lowest_score = find_lowest_score(scores)
    count_passed = count_passed_exams(scores)
    calculate_pass = calculate_pass_rate(scores)
    last_score = get_latest_score(scores)
    change_score = calculate_score_change(scores)
    high_scores = filter_high_scores(scores)
    points_scores = calculate_points_to_pass(scores)

    print("最高点:", highest_score)
    print("最低点:", lowest_score)
    print(f'平均点: {average:.1f}')
    print('合格回数:', count_passed)
    print(f'合格率: {calculate_pass:.1f}%')
    print('最新スコア:', last_score)
    print(f'前回比: データ不足' if change_score is None else f'前回比: {change_score:+}' )
    print('70点以上の模試:', high_scores)
    print(f'合格ラインまで: {points_scores}点')


new_result = input("新しい結果を追加しますか？ (y/n)")

while True:
    if new_result == "y":
        exam = str(input("模試名： "))
        try:
            score = int(input("点数： "))
            study_hours = float(input("勉強時間： "))
            weak_topics = int(input("苦手分野数： "))
        except ValueError:
            print("数値を正しく入力してください")
        else:        
            passed = score >= 70
            new_score = {
                "exam": exam, 
                "score": score, 
                "study_hours": study_hours,
                "weak_topics": weak_topics,
                "passed": passed
            }
            append_score(csv_path, new_score)
            print("模試結果を保存しました")
            break

    else:
        break

