import requests
# r = requests.post("http://localhost/post", data={'foo': 'bar'})
r = requests.get("http://kappaorbanned.azurewebsites.net/")
# And done.
print(r.text)
