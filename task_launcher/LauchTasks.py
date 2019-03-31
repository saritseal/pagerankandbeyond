import concurrent.futures as Fut


def launch_task(task_function, tasks, parallel=5):
    with Fut.ThreadPoolExecutor(parallel) as parallel_threads:
        return parallel_threads.map(task_function, tasks )



