import requests

response = requests.get(
    "https://www.facebook.com"
)

myProject = response.json()

for project in myProject:
    print(
        f"project Name: {project['name']}, project URL: {project['web_url']} ")
