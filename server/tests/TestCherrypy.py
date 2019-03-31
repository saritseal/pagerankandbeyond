from locust import HttpLocust, TaskSet, task
import unittest

class TestCherryPySet(TaskSet, unittest.TestCase):
    @task(1)
    def default_get(self):
        response = self.client.get("/text/sarit")
        # print("Response:" , response)

    # @task(1)
    # def about(self):
    #     self.client.get("/about/")

class StartLocust(HttpLocust):
    task_set = TestCherryPySet
    min_wait = 0
    max_wait = 0
