from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
@app.route('/question_with_one_answer')
def index():
    return render_template('index.html')

@app.route('/thequestion', methods = ["GET","POST"])
def thequestion():
    question = request.form['question']
    select = request.form['select']
    return render_template('thequestion.html', question = question , select = select)



if __name__ == '__main__':
  app.run(host='127.0.0.1', port=5000, debug=True)