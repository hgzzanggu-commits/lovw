from flask import Flask, render_template, request, redirect, url_for, jsonify
from datetime import datetime

app = Flask(__name__)

# 데이터는 마치 '거대한 도서관의 서고'처럼 체계적이다!
# 기존 data 딕셔너리에 'cups'를 추가하는 거다!!
data = {
    'count': 0,
    'goal': 20,
    'cups': 0,      # 물컵의 개수를 기억하는 새로운 저장소!!
    'history': []
}

@app.route('/add', methods=['POST'])
def add():
    current_goal = data.get('goal', 20)
    burst = False
    reset_happened = False 

    # 이미 100%라면 킹 크림슨!! 일단 잔혹하게 0으로 박살낸다!
    if data['count'] >= current_goal:
        data['count'] = 0 
        reset_happened = True
    
    # 그리고 목표가 몇이든 간에 무조건 1번의 파문을 쑤셔넣는다!
    data['count'] += 1

    # 방금 넣은 파문으로 목표에 도달했는지 공평하게 심판하는 거다!!
    if data['count'] >= current_goal:
        data['cups'] += 1           
        burst = True                

    rate = min((data['count'] / current_goal) * 100, 100)

    return jsonify({
        'count': data['count'],
        'goal': current_goal,
        'rate': rate,
        'cups': data['cups'],
        'burst': burst,
        'reset_happened': reset_happened 
    })

@app.route('/')
def index():
    current_goal = data.get('goal', 20)
    rate = min((data['count'] / current_goal) * 100, 100) if current_goal > 0 else 0
    return render_template('index.html', config=data, rate=rate)


@app.route('/set_goal', methods=['POST'])
def set_goal():
    new_goal = request.form.get('goal', type=int)
    if new_goal and new_goal > 0:
        data['goal'] = new_goal
        data['count'] = 0
        data['cups'] = 0  # 이 한 줄이 핵심!! 과거에 마신 컵 전리품도 0으로 날려버리는 거라고!!
        data['history'] = []
    return redirect(url_for('index'))
if __name__ == '__main__':
    app.run(debug=True, port=5000)