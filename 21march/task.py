class Task():
    def __init__(self,taskId,taskName,priority):
        self.taskId=taskId
        self.taskName=taskName
        self.priority=priority

    def __repr__(self):
        return f"Task Id: {self.taskId}\nName: {self.taskName}\nPriority: {self.priority}" 