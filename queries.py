from connect import execute_select


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
