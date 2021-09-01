tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]
# print list of uncompleted tasks

# def uncompleted_tasks(list):
#     uncompleted = []
#     for item in list:
#         if item["completed"] == False:
#             uncompleted.append(tasks)
#     return uncompleted

# print(uncompleted_tasks(tasks))

# print list of completed tasks

# def completed_tasks(list):
#     completed = []
#     for item in list:
#         if item["completed"] == True:
#             completed.append(tasks)
#     return completed

# print(completed_tasks(tasks))

# print task descriptions

def task_descriptions(list):
    descriptions = []
    for item in list:
        descriptions.append(item["description"])
    return descriptions

print(task_descriptions(tasks))


