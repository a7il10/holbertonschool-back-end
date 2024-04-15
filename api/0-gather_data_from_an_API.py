import requests

def todo_list_progress(employee_id):
    # Get the employee data
    employee = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}').json()
    # Get the TODOs for the employee
    todos = requests.get(f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos').json()

    # Calculate the progress
    total_tasks = len(todos)
    done_tasks = len([todo for todo in todos if todo['completed']])
    done_tasks_titles = [todo['title'] for todo in todos if todo['completed']]

    # Print the progress
    print(f"Employee {employee['name']} is done with tasks({done_tasks}/{total_tasks}):")
    for title in done_tasks_titles:
        print(f"\t {title}")

# Test the function with an example employee ID
todo_list_progress(1)
