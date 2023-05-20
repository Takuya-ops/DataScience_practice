from flask import Flask, make_response, redirect, render_template, request
import pandas as pd
from problem import CarGroupProblem

app = Flask(__name__)

# リクエスト内容に学生と車のデータが含まれているか確認


def check_request(request):
    # ファイルの取得
    students = request.files["students"]
    cars = request.files["cars"]

    if students.filename == "":
        return False
    if cars.filename == "":
        return False

    return True


# 最適化結果をHTML形式に変換する関数


def postprocess(solution_df):
    solution_html = solution_df.to_html(header=True, index=False)
    return solution_html


@app.route("/", methods=["GET", "POST"])
def solve():
    # 最適化の実行と結果の表示
    if request.method == "GET":
        return render_template("index.html", solution_html=None)

    if not check_request(request):
        return redirect(request.url)

    # データの読み込み
    students_df, cars_df = process(request)
    # 最適化実行
    solution_df = CarGroupProblems(students_df, cars_df).solve()
    # 最適化結果をHTMLに表示できるようにする
    solution_html = postprocess(solution_df)
    return render_template("index.html", solution_html=solution_html)


@app.route("/download", methods=["POST"])
def download():
    """リクエストに含まれるHTMLの表形式データをcsv形式に変換してダウンロードする関数"""
    solution_html = request.form.get("solution_html")
    solution_df = pd.read_html(solution_html)[0]
    solution_csv = solution_df.to_csv(index=False)
    response = make_response()
    response.data = solution_csv
    response.headers["Content-Type"] = "text/csv"
    response.headers["Content-Disposition"] = "attachment; filename=solution.csv"
    return response
