from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
@app.route('/question_with_one_answer')
def index():
    return render_template('index.html')

@app.route('/thequestion', methods = ["POST"])
def thequestion():
    question1 = request.form.get('question1')
    question2 = request.form.get('question2')
    return render_template('thequestion.html', question1 = question1 , question2 = question2)



if __name__ == '__main__':
  app.run(host='127.0.0.1', port=5000, debug=True)