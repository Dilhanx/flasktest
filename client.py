import requests
# r = requests.post("http://localhost/post", data={'foo': 'bar'})
r = requests.get("http://127.0.0.1:5000")
# And done.
print(r.text) # displays the result body.