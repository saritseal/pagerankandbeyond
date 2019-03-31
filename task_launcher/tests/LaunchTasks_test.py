import unittest
import task_launcher.LauchTasks as launch_tasks
import requests

class LaunchTask_Test(unittest.TestCase):

    def task_function(self, task):
        print("URL", task)
        [print(line) for line in requests.get(task).iter_lines()]

    def test_launchtask(self):
        launch_tasks.launch_task(self.task_function, ["http://www.ndtv.com", "http://www.discoversdk.com/blog/10-interesting-python-modules-to-learn-in-2016"])

if __name__ == "__main__":
    unittest.main()