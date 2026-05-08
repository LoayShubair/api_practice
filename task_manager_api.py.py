import requests
import time

def log_call(func):
    def wrapper(*args, **kwargs):
        print(f"Callings: {func.__name__}")
        print(f"Args: {args}, Kwargs: {kwargs}")
        return func(*args, **kwargs)
    return wrapper


class Timer:
    def __enter__(self):
        self.start = time.time()
    def __exit__(self, exc_type, exc_val, exc_tb):
        end = time.time()
        print(f"Execution time: {end - self.start:.4f} seconds")


class task:
    def __int__(self,title, description, status="open" , owner=None):
        self.title = title
        self.description = description
        self.status = status
        self.owner = owner
    
    def __str__(self):
        owner = self.owner if self.owner else "No owner"
        return f"{self.title} | {self.status} | {owner}"
    
@log_call
def fetch_tasks():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    data = response.json()
    tasks = [Task(item["title"],item["body"]) for item in data[:5]]
    return tasks
def filter_tasks(tasks, **kwargs):
    result tasks
    
    if "status" in kwargs:
        result = [t for t in result if t.status ==kwargs["status"]]

    if "owner" in kwargs:
        result = [t for t in result if t.owner == kwargs["owner"] ]
        return result
    
def main():
    with Timer():
        tasks = fetch_tasks()

    tasks[0].status = "done"
    tasks[1].status = "done"
    tasks[0].owner = "Ali"

    done_tasks = filter_tasks(tasks, status="done")

    print("\nFiltered Tasks:")
    for t in done_tasks:
        print(t)

if __name__ =="__main__":
    main()

   
    

          

