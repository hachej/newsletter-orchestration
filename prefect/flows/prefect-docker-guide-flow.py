from prefect import task, Flow
from prefect.executors import LocalDaskExecutor

@task
def print_number(number):
    print(number)

# Define the main flow
with Flow("parallel_print_flow") as flow:
    # Create 100 tasks that will execute in parallel
    for _ in range(100):
        print_number(5)


# Run the flow
if __name__ == "__main__":
    flow.run()