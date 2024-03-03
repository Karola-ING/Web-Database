from connect import execute_select, execute_insert


def fetch_details():
    query = """
          SELECT job_id, job_title, job_location, salary, currency FROM jobs 
          order by job_id
          """

    return execute_select(query)


def fetch_specific(job_id):
    query = """
            SELECT * FROM jobs
            WHERE job_id = %(job_id)s
            """

    return execute_select(query, {'job_id': job_id}, False)


def fetch_dashboard():
    query = """
          SELECT jobs.job_id, job_title, job_location AS job_location, salary AS salary, currency AS currency,
          dashboard.apply_date AS appy_date
          FROM jobs
          INNER JOIN dashboard ON jobs.job_id = dashboard.job_id
          order by dashboard.apply_date
          """

    return execute_select(query)


def apply_job(job_id, apply_date):
    execute_insert ("""
            INSERT INTO dashboard (job_id, apply_date) 
            VALUES
            (%(job_id)s, %(apply_date)s)
            """, {'job_id': job_id, 'apply_date': apply_date})


def add_user(user_password, user_name):
    execute_insert ("""
            INSERT INTO users (user_password, user_name) 
            VALUES
            (%(user_password)s, %(user_name)s)
            """, {'user_password': user_password, 'user_name': user_name})