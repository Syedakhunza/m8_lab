#syeda khunza fatima
# 14th nov, 2024

# In this  checks whether your game character has picked up all the items.



def check_task_requirements(task_number):
    items = ["pan", "paper", "idea", "rope", "groceries"]
    weaknesses = ["slow"]

    task_requirements = {
        1: {"items": ["rope", "coat", "first aid kit"], "weakness": "slow"},
        2: {"items": ["pan", "groceries"], "weakness": "small"},
        3: {"items": ["pen", "paper", "idea"], "weakness": "confusion"}
    }

    required_items = task_requirements[task_number]["items"]
    required_weakness = task_requirements[task_number]["weakness"]

    has_all_items = all(item in items for item in required_items)

    has_weakness = required_weakness in weaknesses

    
    if has_all_items and not has_weakness:
        print(f"Task {task_number} requirements met. You can perform the task!")
    else:
        print(f"Task {task_number} requirements not met. Check your items or weaknesses.")

check_task_requirements(1)  # Expected output: Task 1 requirements not met. Check your items or weaknesses.
check_task_requirements(2)  # Expected output: Task 2 requirements met. You can perform the task!
check_task_requirements(3)  # Expected output: Task 3 requirements not met. Check your items or weaknesses.
