from __future__ import annotations


import pendulum


from datetime import timedelta, datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.dummy import DummyOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator

n_dags = 1000

for i in range(n_dags):
    with DAG(
        dag_id=f"subdag_{i}",
        schedule_interval="@daily",
        start_date=pendulum.datetime(2021, 1, 1, tz="UTC")
    ) as subdag:
        print_5 = PythonOperator(
            task_id='print_5',
            python_callable=lambda: print(5),
        )

dag = DAG(
    dag_id="benchmark_dag",
    catchup=False,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    schedule="*/10 * * * *",
    tags=["produces", "dataset-scheduled"],

) 
start = DummyOperator(
        task_id='start',
        dag=dag,
    )

end = DummyOperator(
        task_id='end',
        dag=dag,
    )

# Dynamically create 100 subDAGs
for i in range(n_dags):
    subdag = TriggerDagRunOperator(
        task_id=f'trigger_subdag_{i}',
        trigger_dag_id=f"subdag_{i}",
        dag=dag,
    )

    start >> subdag >> end