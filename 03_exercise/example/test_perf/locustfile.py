import time
from locust import HttpUser, task, between
import random


class BasicOrder(HttpUser):
    wait_time = between(1, 2.5)

    @task
    def hello_world(self):
        self.client.get("/hello")
        self.client.get("/world")

    @task(3)
    def view_items(self):
        for item_id in range(10):
            path = f"/order?id={item_id}"
            self.client.post(inject_errors(path), name="/order")
            time.sleep(1)

    def on_start(self):
        self.client.post("/login", json={"username": "foo", "password": "bar"})


def inject_errors(path):
    db_sleep = "{:.2f}".format(random.random() * 3)
    srv_sleep = "{:.2f}".format(random.random() * 2)

    p_db_error = random.uniform(0, 1)

    if p_db_error < 0.7:
        is_db_error = "0"
    else:
        is_db_error = "1"

    p_srv_error = random.uniform(0, 1)
    if p_srv_error < 0.8:
        is_srv_error = "0"
    else:
        is_srv_error = "1"

    withSleep = f"{path}&db_sleep={db_sleep}&srv_sleep={srv_sleep}"
    withErrors = f"{withSleep}&is_db_error={is_db_error}&is_srv_error={is_srv_error}"
    return withErrors
