from task_manager import TaskManager
from task import Task


def print_tasks(tasks, time):
    print("time = ", time)
    for task in tasks:
        print(task)

if __name__ == "__main__":

    time = 0
    task_manager = TaskManager(2)

    # assign C
    task_manager.assign_task("C", 3)
    tasks = task_manager.get_next_tasks()
    time += tasks[1]

    # assign A and F
    task_manager.assign_task("A", 1)
    task_manager.assign_task("F", 6)
    
    # consume A
    tasks = task_manager.get_next_tasks()
    time += tasks[1]

    # assign B
    task_manager.assign_task("B", 2)

    # consume B
    tasks = task_manager.get_next_tasks()
    time += tasks[1]

    # assign D
    task_manager.assign_task("D", 4)

    # consume F
    tasks = task_manager.get_next_tasks()
    time += tasks[1]

    # consume D
    tasks = task_manager.get_next_tasks()
    time += tasks[1]

    # assign E
    task_manager.assign_task("E", 5)

    # consume E 
    tasks = task_manager.get_next_tasks()
    time += tasks[1]

    print(time)
