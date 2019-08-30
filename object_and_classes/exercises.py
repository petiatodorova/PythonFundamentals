class Exercise:
    def __init__(self, topic, course_name, judge_contest_link, problems):
        self.topic = topic
        self.course_name = course_name
        self.judge_contest_link = judge_contest_link
        self.problems = self.set_problems_list(problems)

    def set_problems_list(self, problems):
        temp_list = []
        temp_list.extend(problems)
        return temp_list


line = input().split(" -> ")

exercises_list = []

while not line[0] == "go go go":
    topic = line[0]
    course_name = line[1]
    judge_contest_link = line[2]
    problems = line[3].split(", ")
    current_exercise = Exercise(topic, course_name, judge_contest_link, problems)
    exercises_list.append(current_exercise)
    line = input().split(" -> ")

for exercise in exercises_list:
    print(f"Exercises: {exercise.topic}")
    print(f"Problems for exercises and homework for the \"{exercise.course_name}\" course @ SoftUni.")
    print(f"Check your solutions here: {exercise.judge_contest_link}")
    task_num = 1
    for task in exercise.problems:
        print(f"{task_num}. {task}")
        task_num += 1
