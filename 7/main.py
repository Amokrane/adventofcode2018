import sys
import re
import functools
from task import Task
from task_manager import TaskManager
from collections import defaultdict


MIN_DELAY_PER_TASK = 60 

def compute_tasks_order(input_file):
    lines = [line.rstrip('\n') for line in open(input_file)]

    graph = defaultdict(list) 
    init_graph(graph, lines) 

    task_queue = [] # queue of tasks that can be performed 
    extend_queue(task_queue, get_runnable_tasks(graph))
    
    result = ""
    while task_queue:
        task = poll_queue(task_queue) 
        result += task
        execute_task(graph, task)
        runnable_tasks = get_runnable_tasks(graph)
        extend_queue(task_queue, runnable_tasks) 
        sweep_enqueued_tasks(graph)

    print("Part 1: ", result)

    # part 2
    # fixme refactor (move to private method)
    graph = defaultdict(list) 
    init_graph(graph, lines)

    task_manager = TaskManager(5)
    task_queue = []
    completion_time = 0
    result = ""
    extend_queue(task_queue, get_runnable_tasks(graph))

    while task_queue or graph:
        available_workers = task_manager.get_available_workers() 
        tasks = poll_queue_n(task_queue, available_workers)

        for task in tasks:
            task_manager.assign_task(task, get_task_delay(task))

        t = task_manager.get_next_tasks()
        completion_time += t[1]
        finished_tasks = t[0]

        for finished_task in finished_tasks:
            result += finished_task
            execute_task(graph, finished_task)
            runnable_tasks = get_runnable_tasks(graph)

            # remove the tasks that are already assigned, before filling the task queue
            extend_queue(task_queue, list(set(runnable_tasks) - set(task_manager.get_assigned_tasks())))
            sweep_enqueued_tasks_by_task(graph, finished_task)

    
    print("Part 2: completion time = ", completion_time)
    print("Part 2: Result = ", result)


def init_graph(graph, dependencies):
    regex = "Step\s(\w)\smust\sbe\sfinished\sbefore\sstep\s(\w)\scan\sbegin."

    for dependency in dependencies:
        m = re.match(regex, dependency)
        # 2 needs 1 (1->2)
        task_1 = m.group(1)
        task_2 = m.group(2)
        graph[task_2].append(task_1)
        graph[task_1].extend([])


def get_task_delay(task):
    return MIN_DELAY_PER_TASK + (ord(task) - ord('A') + 1)


def get_runnable_tasks(graph):
    runnable_graph = { k: v for k, v in graph.items() if not v }
    return list(runnable_graph.keys())

def sweep_enqueued_tasks(graph):
    for key in graph.keys():
        if(not graph[key]):
            graph.pop(key, None)

def sweep_enqueued_tasks_by_task(graph, task):
    for key in graph.keys():
        if(key == task):
            graph.pop(key, None)

def execute_task(graph, task):
    graph.pop(task, None)
    executable_graph = { k: v for k, v in graph.items() if task in v }

    for key, value in executable_graph.iteritems():
        tasks = executable_graph[key] 
        tasks.remove(task)
        executable_graph[key] = tasks

def extend_queue(queue, list):
    for l in list:
        if not l in queue:
            queue.append(l)
    queue.sort()

def poll_queue(queue):
    res = queue[0]
    del queue[0]
    return res

def poll_queue_n(queue, n):
    if n > len(queue):
        n = len(queue)

    res = []
    for i in range(n):
        res.append(queue[i])

    for i in range(n):
        del queue[0]

    return res

if __name__ == "__main__":
    compute_tasks_order(sys.argv[1])

