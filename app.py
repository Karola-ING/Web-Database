from datetime import datetime
from flask import Flask, render_template, request, redirect
from queries import fetch_details, fetch_specific, fetch_dashboard, apply_job, add_user

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    jobs = fetch_details()
    return render_template('jobs.html', jobs=jobs)


@app.route('/jobs/<job_id>')
def job_detailed_view(job_id):
    detailed_view = fetch_specific(job_id)
    return render_template('detailed-view.html', job=detailed_view)


@app.route('/jobs', methods=['GET', 'POST'])
def dashboard_insert():
    if request.method == 'POST':
        apply_date = datetime.now()
        apply_date.strftime("%d/%m/%y")
        applied_job_id = int(request.form.get('add_item_index', 0))
        apply_job(applied_job_id, apply_date)
        return redirect('home')


@app.route('/dashboard')
def dashboard():
    dashboard_list = fetch_dashboard()
    return render_template('dashboard.html', jobs=dashboard_list)


@app.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')


@app.route('/create-user', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        user_name = request.form.get('username')
        user_password = request.form.get('psw')
        add_user(user_password, user_name)

    return redirect('home')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8000)
