import requests
# r = requests.post("http://localhost/post", data={'foo': 'bar'})
r = requests.get("http://127.0.0.1:5000/accounts")
# And done.
j=r.json()
i=0
for l in j:
    print(i)
    print(l) # displays the result body.
    i+=1
i=input()