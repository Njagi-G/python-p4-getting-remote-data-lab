import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content

    def load_json(self):
        response = json.loads(self.get_response_body())
        return response


# Test the class for requests, responses and response formats

get_requester = GetRequester('https://learn-co-curriculum.github.io/json-site-example/endpoints/people.json')

result1 = get_requester.get_response_body()
print(f"\n Result Body: {result1}\n")

result2 = get_requester.load_json()
print(f"Result as list of dictionaries: {result2}")

