from task import Task

class TaskManager:

    def __init__(self, capacity):
       self.__workers = [Task(".", 0) for i in range(capacity)]


    def get_available_workers(self):
        available_workers = 0

        for worker in self.__workers:
            if(worker.name == "."):
                available_workers += 1

        return available_workers
        
    def assign_task(self, task_name, task_delay):
        available_worker_index = self.__get_first_worker_available()

        if available_worker_index < 0:
            return False

        self.__workers[available_worker_index] = Task(task_name, task_delay)

    def get_next_tasks(self):
        next_task_delay = self.__get_next_task_delay()

        for task in self.__workers:
            if(task.name != "."):
                task.delay = task.delay - next_task_delay 

        finished_tasks_indexes = []
        finished_tasks_names = []
        
        for i in range(len(self.__workers)):
            if(self.__workers[i].delay == 0 and self.__workers[i].name != "."):
                finished_tasks_indexes.append(i)
                finished_tasks_names.append(self.__workers[i].name)

        # free the workers that are done
        for i in finished_tasks_indexes: 
            self.__workers[i] = Task(".", 0)


        return (finished_tasks_names, next_task_delay)
       
    def get_assigned_tasks(self):
        assigned_tasks = []
        for task in self.__workers:
            if(task.name != "."):
                assigned_tasks.append(task.name)

        return assigned_tasks

    def __get_first_worker_available(self):

        for i in range(len(self.__workers)):
            if self.__workers[i].name == "." and self.__workers[i].delay ==  0:
                return i

        return -1

    def __get_next_task_delay(self):

        non_zero_delay_task = next( (t for t in self.__workers if t.delay != 0), Task(".", 0))
        if non_zero_delay_task == Task(".", 0):
            return None

        next_task_delay = non_zero_delay_task.delay

        for task in self.__workers:
            if task.delay != 0 and task.delay < next_task_delay:
                next_task_delay = task.delay

        return next_task_delay

    def __log_workers(self):
        for task in self.__workers:
            print(task.name, "->", task.delay)

        

