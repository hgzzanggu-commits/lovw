from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# 데이터 저장소
data = {
    "records": [],
    "goal": 8
}

@app.route('/')
def index():
    # 현재 달성률 계산 (0~100)
    count = len(data["records"])
    goal = data["goal"]
    rate = round((count / goal * 100), 1) if goal > 0 else 0
    
    return render_template('index.html', 
                           count=count, 
                           goal=goal, 
                           rate=rate, 
                           records=data["records"])

@app.route('/drink', methods=['POST'])
def drink():
    now = datetime.now().strftime('%H:%M:%S')
    data["records"].append(now)
    return redirect(url_for('index'))

@app.route('/set_goal', methods=['POST'])
def set_goal():
    new_goal = request.form.get('goal', type=int)
    if new_goal and new_goal > 0:
        data["goal"] = new_goal
    return redirect(url_for('index'))

@app.route('/reset')
def reset():
    data["records"] = []
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)