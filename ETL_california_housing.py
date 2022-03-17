from airflow.models import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

# args
my_dag_id = "ETL_california_housing"
default_args = {
    'owner': 'Admin',
    'depends_on_past': False
}

# DAG definition

dag = DAG(
    dag_id=my_dag_id,
    default_args=default_args,
    start_date=datetime(2022, 3, 11, 7, 0, 0),
    max_active_runs=1,
    concurrency=1,
    schedule_interval='*/15 * * * *'
)

# Bash Operator
path_to_bash_1 = 'python3 /home/superuser/scripts/python/create_california_housing_csv.py'
bash_task_1 = BashOperator(task_id='extract_california_housing_to_csv',
                         bash_command=path_to_bash_1,
                         dag=dag)

# Bash Operator
path_to_bash_2 = '/home/superuser/scripts/shell/filter_csv.sh '
bash_task_2 = BashOperator(task_id='filter_csv',
                         bash_command=path_to_bash_2,
                         dag=dag)

# Bash Operator
path_to_bash_3 = 'python3 /home/superuser/scripts/python/eda_spark.py'
bash_task_3 = BashOperator(task_id='realize_eda_and_clean_on_california_housing',
                         bash_command=path_to_bash_3,
                         dag=dag)

# Bash Operator
path_to_bash_4 = '/home/superuser/scripts/shell/load_csv_to_mysql.sh '
bash_task_4 = BashOperator(task_id='load_california_housing_on_mysql',
                         bash_command=path_to_bash_4,
                         dag=dag)

# Bash Operator
path_to_bash_5 = 'python3 /home/superuser/scripts/python/regression_in_california_housing.py '
bash_task_5 = BashOperator(task_id='regression_on_california_housing',
                         bash_command=path_to_bash_5,
                         dag=dag)

# dependencies
bash_task_1 >> bash_task_2 >> bash_task_3 >> bash_task_4 >> bash_task_5