def find_task_order(tasks):
    order = []
    remaining_tasks = list(tasks.keys())

    while remaining_tasks:
        task_completed = False
        for task_id in remaining_tasks:
            if set(tasks[task_id]["prerequisites"]).issubset(order):
                order.append(task_id)
                remaining_tasks.remove(task_id)
                task_completed = True
                break

        if not task_completed:
            return None

    return [tasks[task]["name"] for task in order]
