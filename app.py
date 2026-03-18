from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# 데이터 저장 (간단하게 리스트로)
records = []
goal = 8  # 하루 목표 (8잔)

@app.route('/')
def index():
    return render_template('index.html', count=len(records), goal=goal)

@app.route('/drink', methods=['POST'])
def drink():
    time = datetime.now().strftime('%H:%M:%S')
    records.append(time)
    return redirect(url_for('index'))

@app.route('/result')
def result():
    count = len(records)
    rate = (count / goal) * 100
    return render_template('result.html', count=count, goal=goal, rate=rate)

if __name__ == '__main__':
    app.run(debug=True)