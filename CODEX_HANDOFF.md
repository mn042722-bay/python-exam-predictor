# Python Exam Predictor - Codex引継ぎ資料

## 1. プロジェクトの目的

Python 3 エンジニア認定基礎試験の学習を兼ねて、
2日程度で完成できる小規模なPythonアプリを作成する。

単にアプリを完成させることが目的ではなく、

「自分でPythonコードを書けるようになる」

ことを最優先とする。

将来的には機械学習を組み込み、
Python模擬試験の結果などから合格・スコアを予測する
「Python試験合格予測ミニアプリ」に発展させたい。

AWS / SageMaker等への展開も候補だが、
現時点ではAWSは考えなくてよい。

まずローカル環境でPythonアプリを完成させる。


---

# 2. 最重要：Codexへの指示

このプロジェクトでは、ユーザーの代わりに
完成コードを最初から実装しないこと。

Codexは「実装担当」よりも
「Pythonの先生・ペアプログラマー」として振る舞う。

基本フロー：

1. 次に実装する小さな課題を1つ提示する
2. ユーザー自身にコードを書かせる
3. 書かれたコードをレビューする
4. 間違いがあれば、まずヒントを出す
5. それでも分からなければ詳しく説明する
6. 正解したら次の小さな課題へ進む

例：

「scores.csvを読み込む関数を作ってください」

↓

ユーザーが実装

↓

Codexがレビュー

↓

次の課題へ

一度に大量のコードを生成しないこと。


---

# 3. 学習目的

2026年9月20日に
Python 3 エンジニア認定基礎試験を受験予定。

そのため、このアプリ開発では可能な限り
Python基礎試験につながる構文を使用する。

優先して使いたいもの：

- 変数
- list
- dict
- tuple
- set
- if / elif / else
- for
- while
- range()
- len()
- enumerate()
- zip()
- 関数
- 引数
- return
- import
- try / except / else / finally
- ファイル操作
- csvモジュール
- クラス
- インスタンス
- リスト内包表記
- lambda
- sorted()
- sum()
- max()
- min()

必要であれば標準ライブラリも使用する。


---

# 4. 外部ライブラリについて

最初からpandas等に処理を任せすぎない。

特にCSVについては最初は、

import csv

を利用してPython標準機能で処理する。

理由：

Python基礎構文の練習を優先するため。

基礎部分が完成した後、

- pandas
- scikit-learn

などを導入してよい。


---

# 5. 最終的に作りたいもの

仮称：

Python Exam Predictor

ユーザーのPython模擬試験結果などを記録・分析する。


想定データ例：

- 模試名
- 点数
- 正答率
- 勉強時間
- 苦手分野数
- 受験日
- 合格 / 不合格


例：

score = {
    "exam": "mock_01",
    "score": 65,
    "study_hours": 2.5,
    "weak_topics": 4,
    "passed": False
}


CSV形式でデータを保存することも検討する。


---

# 6. 第一段階で実装したい機能

まず機械学習は使わず、
普通のPythonアプリとして完成させる。

想定機能：

CSV読み込み

↓

list / dictへの変換

↓

模試データの分析

↓

以下などを計算

- 平均点
- 最高点
- 最低点
- 合格回数
- 合格率
- 直近の点数
- 前回から何点上がったか
- 70点以上の試験を抽出

↓

結果をコンソール表示


例：

=== Python Exam Analyzer ===

受験回数: 5
平均点: 63.4
最高点: 75
最低点: 52

最新スコア: 65
前回比: +5

合格ラインまで: 5点


---

# 7. 第二段階

第一段階が完成したら、
簡単な機械学習を追加する。

候補：

scikit-learn

目的：

過去の模試結果等から、

「合格できそうか」

あるいは

「予測スコア」

を算出する。


イメージ：

学習データ
    ↓
scikit-learn
    ↓
モデル学習
    ↓
現在の学習状況を入力
    ↓
予測
    ↓
合格可能性 / 予測点数


ただし、

機械学習の精度そのものは重要ではない。

目的は、

Python
+
データ処理
+
機械学習

を一通り経験すること。


---

# 8. 第三段階（余裕があれば）

ローカル版完成後に検討する。

- AWS S3
- Amazon SageMaker AI
- AWS上での学習
- AWS上での推論

現段階では実装不要。

ローカル版が完成してから判断する。


---

# 9. 現在のPython習熟状況

Python基礎試験を勉強中。

コードは読めるようになってきたが、
ゼロから書く力を重点的に鍛えている。


比較的書ける：

- for
- if
- list
- dict
- .items()
- append()
- 関数
- 基本的なreturn
- 条件付き集計


最近自力で書けた例：

def count_passed_students(scores):
    count = 0

    for name, score in scores.items():
        if score >= 60:
            count += 1

    return count


辞書の生成も可能：

def apply_discount(prices):
    new_prices = {}

    for name, price in prices.items():
        if price >= 100:
            new_prices[name] = price - 20

    return new_prices


リスト内の辞書も扱える：

def calculate_sales(sales):
    total = 0

    for sale in sales:
        if sale["price"] >= 100:
            total += sale["price"]

    return total


---

# 10. 現在の弱点

特に以下をアプリ開発の中で練習したい。


## while + index

以前、

index

と

numbers[index]

の違いで混乱していた。

現在は、

index = 0

while index < len(numbers):
    print(numbers[index])
    index += 1

という基本形は理解し始めている。


## indexと値

重要：

index
→ 要素の場所

numbers[index]
→ その場所に入っている値


## return

最近よくあったミス：

合計値を計算しているのに、

return price

など別の変数を返してしまう。

また以前、

whileの途中で

else:
    return None

としてしまい、
最初の要素しかチェックできないことがあった。

「最終的にこの関数は何を返すのか」
を毎回確認させること。


## クラス

かなり苦手。

特に：

- class
- instance
- self
- __init__
- クラス変数
- インスタンス変数
- 継承
- オーバーライド

アプリ内で無理のない範囲でクラスを使わせたい。


## mutable / shallow copy

以下も弱い：

- リストの参照
- shallow copy
- mutable default argument
- mutationとrebind


## 座学系

以下も弱い：

- 標準ライブラリ
- モジュール
- 例外
- annotations
- docstring
- PEP8

アプリ内で自然に触れられるものは触れたい。


---

# 11. 教え方

ユーザーは、

「コードを見ると分かるが、自分では書けない」

状態を改善したい。

そのため完成コードを先に見せない。


良い例：

「平均点を計算する関数を作ってください。

条件：
- forを使う
- sum()は禁止
- returnで平均値を返す」

↓

ユーザーが実装


悪い例：

「このコードをコピペしてください」

として完成コードを最初から渡す。


---

# 12. エラー時の対応

コードが間違っていた場合、
すぐ完成コードを出さない。

まず、

「この変数には今何が入っていますか？」

「この関数は最終的に何をreturnしたいですか？」

「indexとnumbers[index]のどちらが必要ですか？」

など、原因を考えさせる。

それでも分からない場合は、
実際の値を使って1行ずつトレースする。


例：

numbers = [4, 18, 7]

index = 0
numbers[index] = 4

index = 1
numbers[index] = 18

のように説明する。


---

# 13. 難易度

基本：

Python基礎試験
「本番標準〜やや難」

を中心にする。

難解なパズルコードばかりにしない。

目的は、

試験合格
+
自力コーディング力向上

の両方。


---

# 14. コードレビュー方針

レビュー時は、

1. 正しく動くか
2. ロジックは正しいか
3. Pythonとして自然か
4. 試験対策として何を学べるか

を見る。

単純なタイプミスと
理解不足によるロジックミスは区別する。


例：

append[name]

↓

append(name)

これはロジックではなく構文ミス。


一方、

return index

なのに問題では値を要求している場合は、

indexと値の理解を確認する。


---

# 15. 変数名について

Python組み込み関数と同じ変数名はなるべく避ける。

例：

sum = 0

ではなく、

total = 0

を推奨。

他にも、

list
dict
str
int
max
min

などを変数名にしない。


---

# 16. 初日の進め方

明日はまず環境確認から始める。

想定プロジェクト：

python-exam-predictor/
│
├── main.py
├── analyzer.py
├── model.py
├── data/
│   └── scores.csv
├── .gitignore
└── README.md


最初からすべて作る必要はない。


推奨Step 1：

小さなscores.csvを作る。


推奨Step 2：

csvモジュールを使用して、
scores.csvを読み込む関数をユーザー自身に実装させる。


推奨Step 3：

読み込んだデータをlist / dictとして扱う。


推奨Step 4：

平均点などの分析関数を1つずつ作る。


例：

calculate_average()

find_highest_score()

find_lowest_score()

count_passed_exams()

calculate_pass_rate()

calculate_score_change()


推奨Step 5：

main.pyから各関数を呼び出す。


推奨Step 6：

try / exceptを導入して、
ファイルが存在しない場合などのエラー処理を追加する。


推奨Step 7：

必要に応じてクラス化する。


---

# 17. 重要な制約

ユーザーから明示的に、

「完成コードを書いて」

と言われない限り、
プロジェクト全体をCodex側で完成させない。

ユーザー自身がコードを書く量を最大化する。

Codexは、

設計
→ 小問題
→ ユーザー実装
→ レビュー
→ 修正
→ 次の小問題

という形で進行する。


---

# 18. 最初にユーザーへ出す課題（2026年9月11日 完了）

環境確認後、いきなり機械学習には進まない。

まず、

「CSVから模試データを読み込む」

ところから始める。

ただしcsvモジュール自体に慣れていない可能性があるため、
必要なら最小限の使い方だけ説明してから、
関数部分を本人に実装させる。

最初のゴールは、

CSV
↓
Python
↓
list / dict
↓
print()

まで。


---

# 19. 最終目標

2日程度で、

「自分でPythonを書いて作った」

と言える小規模アプリを完成させる。

完成度やUIよりも、

- Python基礎構文を実際に使った
- ファイルを分割した
- CSVを扱った
- 関数を自分で作った
- エラー処理をした
- データを分析した

という経験を優先する。

その後余裕があれば、

scikit-learn
↓
機械学習
↓
AWS

へ拡張する。


---

# 20. 2026年9月11日の作業環境

プロジェクト直下：

```text
C:\Users\user01\Desktop\python-exam-predictor
```

GitHubリポジトリ：

```text
https://github.com/mn042722-bay/python-exam-predictor.git
```

ブランチは `main`。

Python環境：

- `python` コマンドで Python 3.11.9 を実行可能
- `py` ランチャーは未導入だが、現在の作業に支障はない
- MinGitは `mingit/cmd/git.exe` に展開済み
- MinGit本体とダウンロードZIPは `.git/info/exclude` でローカル除外済み

CodexのサンドボックスユーザーからGitを実行するときは、所有者保護対策として必要に応じて次をコマンド単位で指定する。

```text
-c safe.directory=C:/Users/user01/Desktop/python-exam-predictor
```

ユーザー自身のVS Codeターミナルでは通常この指定は不要。


---

# 21. 2026年9月11日に完了した作業

現在の構成：

```text
python-exam-predictor/
├── analyzer.py
├── main.py
├── data/
│   └── scores.csv
├── .gitignore
├── README.md
└── CODEX_HANDOFF.md
```

サンプルCSVには以下の3件が入っている。

```text
mock_01: 58点、不合格
mock_02: 67点、不合格
mock_03: 74点、合格
```

## `load_scores(file_path)`

完了・動作確認済み。

- `csv.DictReader` でCSVを読み込む
- 各行を辞書として扱う
- `row["score"]` を文字列から整数へ変換する
- 辞書をリストへ追加する
- 3件すべてを読み込み、辞書のリストを返す

重要な学習内容：

```text
scores             → 辞書が複数入ったlist
row                → 模試1回分のdict
row["score"]       → その模試の点数（intへ変換済み）
```

## `calculate_average(scores)`

完了・動作確認済み。

- `sum()`を使わず、`for`で合計する
- `len(scores)`で受験回数を取得する
- 平均値を`return`する
- 現在の結果は `66.33333333333333`

## `find_highest_score(scores)`

完了・動作確認済み。

- `max()`を使わずに実装
- `scores[0]["score"]`を初期値にする
- 現在の結果は `74`

## `find_lowest_score(scores)`

完了・動作確認済み。

- `min()`を使わずに実装
- `scores[0]["score"]`を初期値にする
- 現在の結果は `58`

## `count_passed_exams(scores)`

完了・動作確認済み。

- `for`と`if`で合格件数を数える
- 現在の`passed`はboolではなくCSV由来の文字列なので、`"True"`と比較している
- 現在の結果は `1`

## `calculate_pass_rate(scores)`

完了・動作確認済み。

- 既存の`count_passed_exams(scores)`を再利用する
- `合格回数 / 受験回数 * 100`で計算する
- 不要な`for`ループは削除済み
- 現在の結果は `33.33333333333333%`

## `main.py`

完了済みの各関数をインポートして呼び出し、以下をコンソール表示できる。

```text
最高点: 74
最低点: 58
平均点: 66.33333333333333
合格回数: 1
合格率: 33.33333333333333%
```

2026年9月11日時点で、上記の各関数は個別実行でも確認済み。


---

# 22. 本日確認できた理解と、引き続き注意する点

ユーザーは以下を自分で実装できた。

- `csv.DictReader`による読み込み
- 関数の定義、引数、戻り値
- `for`による辞書リストの処理
- 辞書からの値の取得
- `int()`による型変換
- 合計、平均、最大、最小、条件付きカウント
- 既存関数を別の関数から呼び出す処理
- `main.py`から別モジュールの関数を呼び出す処理

特に混乱しやすかった点：

- `scores`はlist、`row`はdict、`row["score"]`はintというデータ構造の階層
- 辞書全体をリストへ残す場合、点数だけを`append()`しないこと
- `return`を`for`の中に置くと最初の要素で関数が終了すること
- ループ変数を使っていない`for`は不要な可能性が高いこと
- 関数を定義しただけではコンソールには表示されないこと
- 新しい関数は`main.py`から呼び出し、`print()`して初めてユーザー側で結果を確認できること

今後、Codexは新しい分析関数について、必ず次を1セットとして案内する。

```text
analyzer.pyで関数を実装
↓
main.pyでインポート
↓
main.pyで関数を呼び出す
↓
戻り値をprintする
↓
python main.pyで表示確認
```

エラー確認について：

- 実行時エラーはVS Code下部のターミナルに表示される
- `Traceback`は最後の行の例外名・メッセージから上へ読む
- エラーが出ないロジックミスは、具体的な値のトレースやテストで確認する

教える際は、抽象的な説明だけで進めない。
次のように実際の値を示す。

```text
row = {"exam": "mock_01", "score": 58, ...}
row["score"] = 58
total = 0 + 58
```

最初はヒントを出すが、同じ点で詰まった場合は、空欄問題だけを繰り返さず、値を1行ずつ追って具体的に説明する。


---

# 23. 現在残っている軽微な改善点

現時点では動作を優先しており、以下は未対応。

- `analyzer.py`の`os`、`base_dir`、グローバルな`file_path`は現在使われていない
- `study_hours`と`weak_topics`は文字列のまま
- `passed`も文字列の`"True"` / `"False"`のまま
- 空のCSVに対する処理がなく、`scores[0]`やゼロ除算でエラーになる可能性がある
- `main.py`のインポートや引用符など、書式を後でPEP 8寄りに整理できる
- 平均点と合格率は小数点以下が長いため、後で表示桁数を整える
- `main.py`のCSVパスは実行時のカレントディレクトリに依存している

これらは今すぐCodexがまとめて直さず、学習課題として1つずつユーザーに実装してもらう。


---

# 24. 次回最初に行う課題

次回は `get_latest_score(scores)` から再開する。

目的：

- CSVの末尾を最新の模試結果として扱う
- 負のインデックスを練習する

条件：

- `for`は使わない
- `scores[-1]`で最後の辞書を取得する
- 最後の辞書から`"score"`を取り出す
- 最新スコアを`return`する
- `main.py`でインポート、呼び出し、表示まで行う

期待値：

```text
最新スコア: 74
```


---

# 25. その後に予定している実装

第一段階の残りを、原則として以下の順で1機能ずつ進める。

1. `calculate_score_change(scores)`
   - `scores[-1]`と`scores[-2]`を使う
   - 最新点と前回点の差を返す
   - 現在の期待値は `+7`
2. 70点以上の模試を抽出する関数
   - `for`、`if`、`append()`を復習する
3. 合格ライン70点までの差を計算する関数
4. 平均点・合格率の表示桁数を整える
5. CSVが空の場合やデータ不足の場合の処理
6. `try / except`で`FileNotFoundError`や`ValueError`を扱う
7. `study_hours`を`float`、`weak_topics`を`int`、`passed`をboolへ変換する
8. 新しい模試結果をCSVへ追記する機能
   - 最初は手動入力でもよい
   - その後`csv.DictWriter`を練習する
9. 必要に応じてクラス化し、`self`、`__init__`、インスタンスを練習する
10. READMEに実行方法と機能一覧を書く

第一段階が完成してデータが増えた後、余裕があればscikit-learnによる予測へ進む。


---

# 26. 試験対策との組み合わせ

このアプリ作成は、基礎試験の以下の分野に直接つながっている。

- 制御構造
- データ構造
- 関数
- モジュール
- 入出力
- 標準ライブラリ

ただしアプリ開発だけでは選択式試験の全範囲を網羅できない。

今後は各機能の完成後に、次を短く実施する。

1. 使用した変数の型を確認する
2. 具体的な値で1行ずつトレースする
3. 関連する試験形式の小問題を1〜3問出す
4. `if`、`while`、例外、クラス、標準ライブラリなど未使用範囲も別途補う

試験予定日は2026年9月20日。
アプリ完成だけに偏らず、公式問題集や模擬問題による選択式問題の練習も並行する。
