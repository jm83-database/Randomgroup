from flask import Flask, request, render_template_string, send_file
import random
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        num_groups = int(request.form['num_groups'])
        groups = [f'{i+1}조' for i in range(num_groups)]
        random.shuffle(groups)
        return render_template_string(TEMPLATE, groups=groups)
    return render_template_string(TEMPLATE)

@app.route('/background')
def background():
    return send_file('연성대학교 AI-X 해커톤 배경.png', mimetype='image/png')

TEMPLATE = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <title>발표 순서 추첨</title>
    <style>
      body {
        background-image: url('/background');
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        margin: 0;
      }
      .container {
        background-color: rgba(255, 255, 255, 0.8);
        padding: 40px;
        border-radius: 10px;
        text-align: center;
      }
      ul {
        list-style: none;
        padding: 0;
      }
      ul li {
        background: #f0f0f0;
        margin: 10px 0;
        padding: 10px;
        border-radius: 5px;
        display: flex;
        align-items: center;
      }
      ul li::before {
        content: '✔️';
        margin-right: 10px;
        color: green;
      }
      h1 {
        font-size: 5em; /* 폰트 크기를 크게 조정 */
      }
    </style>
  </head>
  <body>
    <div class="container">
      <h1>발표 순서 추첨</h1>
      <form method="post">
        <label for="num_groups">발표할 조의 숫자를 입력해주세요:</label>
        <input type="number" id="num_groups" name="num_groups" required>
        <button type="submit">랜덤추첨 시작</button>
      </form>
      {% if groups %}
        <h2>랜덤 추첨된 발표 순서입니다.</h2>
        <ul>
          {% for group in groups %}
            <li>{{ group }}</li>
          {% endfor %}
        </ul>
      {% endif %}
    </div>
  </body>
</html>

'''


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
