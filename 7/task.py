class Task:

    def __init__(self, name, delay):
        self.name = name
        self.delay = delay 

    def __str__(self):
        return self.name + ", " + str(self.delay)




