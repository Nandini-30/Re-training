class Task:
    def __init__(self, name, desc, priority):
        self.name = name
        self.desc = desc
        self.priority = priority
        
    def __repr__(self):
        return f"{self.name}, {self.desc},{self.priority}"