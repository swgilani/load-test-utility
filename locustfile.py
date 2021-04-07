from locust import HttpUser, task, between



class NewtonLoadTesting(HttpUser):

    #Setting up the test for the GET request
    @task
    def  test_1(self):
        self.client.get(url="/dashboard/api/assets/", name="Newton GET Request")

    #Setting up the test for the POST request with JSON data
    @task
    def  test_2(self):
        post_data = { "currency_pair":"XLM_CAD", "period": "1HR" }
        self.client.post(url="/dashboard/api/chart/",data=post_data, name="Newton POST Request")

    