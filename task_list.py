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

# def task_descriptions(list):
#     descriptions = []
#     for item in list:
#         descriptions.append(item["description"])
#     return descriptions

# print(task_descriptions(tasks))

# Print a list of tasks where time_taken is at least a given time

# def given_time(list, time):
#     given_time_tasks = []
#     for item in list:
#         if item["time_taken"] >= time:
#             given_time_tasks.append(item)
#     return given_time_tasks
# print(given_time(tasks, 10))


# print task for given descripton


def given_description(list, desc):
    given_desc = []
    for item in list:
        if item["description"] == desc:
            given_desc.append(item)
    return given_desc
print(given_description(tasks, "Feed Cat"))

