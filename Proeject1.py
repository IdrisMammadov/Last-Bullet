"""
to_do_list = ["Listening", "Swiming", "Reading", "Writing"]


yes = "y"
no = "n"
task1 = input(f"Did you do {to_do_list[0]}: ")
task2 = input(f"Did you do {to_do_list[1]}: ")
task3 = input(f"Did you do {to_do_list[2]}: ")
task4 = input(f"Did you do {to_do_list[3]}: ")

if task1 == "y" and task2 == "n" and task3 == "n" and task4 == "n" :
    print("You have done 1/4")
elif task1 =="y" and task2 =="y" and task3 =="n" and task4 =="n" :
    print("You have done 2/4")
elif task1 =="y" and task2 =="y" and task3 =="y" and task4 =="n" :
        print("You have done 3/4")
elif task1 =="y" and task2 =="y" and task3 =="y" and task4 =="y" :
        print("You have done 4/4")
else:
      ("Copmlete please")
"""

"""

task_number = input("Write your tasks: ")
task_number1= task_number.split(",")
index = 0
while index < len(task_number1):
  letter= task_number1[index]
  print(f" {index}.{letter}")
  index += 1


to_do_list = input(f'if you\' have done your tasks write  "y" if not write  "n" \n' )
tasks = to_do_list.split(",")


if tasks[0] == "y":
    print(f"{task_number1[0]}  is done")
else:
    print(f"You need to check {task_number1[0]} again")

if tasks[1] == "y":
    print(f"{task_number1[1]} is done")
else:
    print(f"You need to check {task_number1[1]} again")

if tasks[2] == "y":
    print(f"{task_number1[2]} is done")
else:
    print(f"You need to check {task_number1[2]} again")

if tasks[3] == "y":
    print(f"{task_number1[3]} is done")
else:
    print(f"You need to check {task_number1[3]} again")
"""

 



    


  
        
    