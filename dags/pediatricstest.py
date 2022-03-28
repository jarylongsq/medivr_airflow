from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator
from textwrap import dedent


default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022, 3, 1),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def extract_playfab():
    return "Works"

with DAG(
    'pediatricstest',
    default_args = default_args,
    description='ETL pipeline for pediatrics interventions',
    schedule_interval=timedelta(days=1),
) as dag:

    extract = PythonOperator(
        task_id = 'extract_from_playfab',
        python_callable = extract_playfab,
    )
