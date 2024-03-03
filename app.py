from flask import Flask, render_template

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'IT Desktop Support Junior Specialist',
    'location': 'Cracow, Małopolskie, Poland',
    'company': 'Zurich Insurance',
    'salary': '10,000 PLN'
  },
  {
    'id': 2,
    'title': 'IT Service Support Analyst',
    'location': 'Gniezno, Wielkopolskie, Poland',
    'company': 'LKQ Europe',
    'salary': '7,000 PLN'
  },
  {
    'id': 3,
    'title': 'Administrator IT',
    'location': 'Wrocław, Dolnośląskie, Poland',
    'company': 'Polska Grupa Farmaceutyczna S.A.',
    'salary': '5,000 PLN'
  }
]


@app.route('/')
def home():
    return render_template('jobs.html', jobs=JOBS)


@app.route('/register')
def register():
    return render_template('register.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8000)
