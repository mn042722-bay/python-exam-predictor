import os

from analyzer import load_scores
from analyzer import ExamAnalyzer
from analyzer import append_score


def main():
    base_dir = os.path.dirname(__file__)
    csv_path = os.path.join(base_dir, "data", "scores.csv")

    try:
        scores = load_scores(csv_path)
    except FileNotFoundError:
        print("CSVファイルが見つかりません")
        return
    except ValueError as error:
        print(error)
        return
    else:
        analyzer = ExamAnalyzer(scores)
        average = analyzer.get_average()
        highest_score = analyzer.get_highest_score()
        lowest_score = analyzer.get_lowest_score()
        count_passed = analyzer.get_passed_count()
        pass_rate = analyzer.get_pass_rate()
        last_score = analyzer.get_latest_exam_score()
        change_score = analyzer.get_score_change()
        high_scores = analyzer.get_high_scores()
        points_to_pass = analyzer.get_points_to_pass()

        print("最高点:", highest_score)
        print("最低点:", lowest_score)
        print(f'平均点: {average:.1f}')
        print('合格回数:', count_passed)
        print(f'合格率: {pass_rate:.1f}%')
        print('最新スコア:', last_score)
        print(f'前回比: データ不足' if change_score is None else f'前回比: {change_score:+}' )
        print('70点以上の模試:', high_scores)
        print(f'合格ラインまで: {points_to_pass}点')


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


if __name__ == "__main__":
    main()
