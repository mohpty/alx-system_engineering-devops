#!/usr/bin/python3
"""A simple module to make API Calls
and return the Responses. Then print them out to standard output
"""

from requests import get
from sys import argv

headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "User-Agent": "Thing Gecko/20100101 Firefox/102.0"
}
base_url = "https://jsonplaceholder.typicode.com/users/"


def get_task_status(user_id: str) -> None:
    """
    Get the task status for a certain user
    """
    emp_name = get("{}{}".format(base_url, user_id)).json().get("name")
    full_url = "{}{}/todos/".format(base_url, user_id)
    response = get(full_url, headers=headers).json()
    total_tasks = len(response)

    done_tasks = [task['title'] for task in response
                  if task['completed']]
    done_tasks_count = len(done_tasks)
    print("Employee {} is done with tasks({}/{}):".format(
        emp_name, done_tasks_count, total_tasks))
    [print("\t {}".format(task)) for task in done_tasks]


if __name__ == "__main__":
    get_task_status(argv[1])
