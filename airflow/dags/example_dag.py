from datetime import datetime, timedelta
from numpy import random
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python_operator import PythonOperator

from python_script_airflow import compute_squares

################### ---Define Parameters--- ###################

# default args dictionary, passed onto the DAG
default_args = {
        'depends_on_past': False,
        'email': ['airflow@example.com'],
        'email_on_failure': False,
        'email_on_retry': False,
        'retries': 3,
        'retry_delay': timedelta(minutes=1),
        # 'end_date': datetime(2016, 1, 1),
        # 'on_failure_callback': some_function,
        # 'on_success_callback': some_other_function,
    }

schedule_interval = '0 5 * * *'  # minute hour day month year -> 5AM each day
# schedule_interval=timedelta(days=1)


###################### ---Define DAG--- ######################

dag = DAG(
    dag_id='sample_dag',
    default_args=default_args,
    description='An easy DAG to describe a minimal example',
    schedule_interval=schedule_interval,
    start_date=datetime(2022, 8, 22),
    tags=['sample dag']
)


###################### ---Define Tasks--- ######################

python_task = PythonOperator(
    dag=dag,
    task_id='python_task',
    python_callable=compute_squares,
    op_kwargs={'number_list': random.randint(100, size=(5))}
)

success = BashOperator(
    dag=dag,
    task_id="success",
    bash_command="echo 'we were successful'"
)

too_large = BashOperator(
    dag=dag,
    task_id="too_large",
    bash_command="echo 'we were successful but the numbers were too large'"
)

fail = BashOperator(
    dag=dag,
    task_id="fail",
    bash_command="echo 'we were not successful'"
)

sleep_task = BashOperator(
    dag=dag,
    task_id='sleep',
    bash_command='sleep 5'
)


###################### ---Create Pipeline--- ######################

python_task >> [success, too_large, fail] >> sleep_task

    