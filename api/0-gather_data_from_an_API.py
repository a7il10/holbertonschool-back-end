import requests

def get_employee_todo_progress(employee_id):
    # Get the employee's details
    employee = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}').json()
    # Get the employee's todos
    todos = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos').json()

    # Calculate the progress
    total_tasks = len(todos)
    done_tasks = len([task for task in todos if task['completed']])
    
    # Print the progress
    print(f"Employee {employee['name']} is done with tasks({done_tasks}/{total_tasks}):")
    for task in todos:
        if task['completed']:
            print(f"\t {task['title']}")

# Test the function with an example employee ID
get_employee_todo_progress(1)
