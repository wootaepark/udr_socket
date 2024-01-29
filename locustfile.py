from locust import HttpUser, task

class User(HttpUser):
    @task
    def get_index(self):
        self.client.get('/')
