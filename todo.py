import pandas as pd
import sys
import numpy as np

class todo_crud():
    def __init__(self, csv_file):
        self.todolist = pd.read_csv(csv_file)
        self.ongoingtodos = list(self.todolist['ongoing'])
        self.completedtodos = list(self.todolist['completed'])
        self.updated_todo = None

    def addTodo(self, newTodo):
        self.ongoingtodos.append(newTodo)
        print(self.ongoingtodos, "added", newTodo)

    def removeTodo(self, removetodo):
        self.ongoingtodos.remove(removetodo)
        print(self.ongoingtodos, "removed", removetodo)

    def createNewtodo(self):
        ongoing_count = len(self.ongoingtodos)
        completed_count = len(self.completedtodos)
        while completed_count > ongoing_count:
                ongoing_count += 1
                self.ongoingtodos.append(np.nan)
        while completed_count < ongoing_count:
                completed_count += 1
                self.completedtodos.append(np.nan)
        self.updated_todo = pd.DataFrame(data={"ongoing": self.ongoingtodos, "completed": self.completedtodos})
        self.updated_todo = self.updated_todo.to_csv(r"D:/jedha/todo_app/todolist.csv", sep=',', index=False)

    def showOngoing(self):
        print(self.ongoingtodos)

    def showCompleted(self):
        print(self.completedtodos)


mylist = todo_crud('todolist.csv')

try:
    addOrComplete = sys.argv[1]
    if addOrComplete == "add":
        todo = sys.argv[2]
        mylist.addTodo(todo)
        mylist.createNewtodo()
    elif addOrComplete == "remove":
        todo = sys.argv[2]
        mylist.removeTodo(todo)
        mylist.createNewtodo()
    elif addOrComplete == "completed":
        mylist.showCompleted()
    elif addOrComplete == "ongoing":
        mylist.showOngoing()
except:
    print('no arguments provided')
'''
try:
    newtodo = sys.argv[1]
    mylist.addTodo(newtodo)
except:
    print('no todo to add provided')

try:
    removetodo = sys.argv[2]
    mylist.removeTodo(removetodo)
except:
    print('no todo to remove provided')
'''


