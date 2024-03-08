from dagster import FilesystemIOManager, graph, op, repository, schedule, job, DynamicOut, DynamicOutput
from dagster_docker import docker_executor


@op(out=DynamicOut())
def start():
    for idx, piece in enumerate(range(1000)):
        yield DynamicOutput(f"test_{idx}", mapping_key=str(idx))

@op
def compute(idx):
    return idx

@op
def finish(outputs):
    return outputs

@job
def dynamic_graph():
    indexes = start()
    results = indexes.map(compute)
    finish(results.collect())




# @schedule(cron_schedule="* * * * *", job=my_job, execution_timezone="US/Central")
# def my_schedule(_context):
#     return {}


# @repository
# def deploy_docker_repository():
#     return [my_job, my_step_isolated_job, my_schedule]
