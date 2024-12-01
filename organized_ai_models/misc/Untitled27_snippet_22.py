import schedule
import time

def job():
    api_urls = [
        "https://jsonplaceholder.typicode.com/todos/1",
        "https://jsonplaceholder.typicode.com/todos/2"
    ]
    fetch_and_store_multiple(api_urls, firebase_config)

# Schedule the job every hour
schedule.every(1).hours.do(job)

print("Starting the scheduler...")
while True:
    schedule.run_pending()
    time.sleep(1)
