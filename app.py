from flask import Flask, render_template
from database import fetch_details, fetch_specific

app = Flask(__name__)


@app.route('/')
def home():
    jobs = fetch_details()
    return render_template('jobs.html', jobs=jobs)


@app.route('/jobs/<job_id>')
def job_detailed_view(job_id):
    detailed_view = fetch_specific(job_id)
    return render_template('detailed-view.html', job = detailed_view)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8000)
