from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)

DATA_FILE = 'data.json'

def load_data():
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/save', methods=['POST'])
def save_progress():
    data = load_data()
    user_id = 'user1'  # hardcoded for now
    new_intervals = request.json['intervals']
    video_duration = request.json['duration']

    if user_id not in data:
        data[user_id] = {
            'intervals': [],
            'progress': 0
        }

    all_intervals = data[user_id]['intervals'] + new_intervals
    all_intervals.sort()

    merged = []
    for interval in all_intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    total_unique = sum(end - start for start, end in merged)
    progress = round((total_unique / video_duration) * 100, 2)

    data[user_id]['intervals'] = merged
    data[user_id]['progress'] = progress

    save_data(data)
    return jsonify({'progress': progress, 'intervals': merged})

@app.route('/load')
def load_progress():
    data = load_data()
    user_id = 'user1'
    user_data = data.get(user_id, {'intervals': [], 'progress': 0})
    return jsonify(user_data)

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

