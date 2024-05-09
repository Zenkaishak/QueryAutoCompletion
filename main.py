import json
import requests

completion_query = input("Please write a completion query : \n\n")

headers = {
    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
}


response = requests.get(f'http://google.com/complete/search?client=chrome&q={completion_query}')


for completion in json.loads(response.text)[1]:
    print(completion)