from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
@app.route('/question_with_one_answer')
def index():
    # return render_template('index.html')
    return "ala"
if __name__ == '__main__':
  app.run(host='127.0.0.1', port=5000, debug=True)
 