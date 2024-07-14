import urllib
with urllib.request.urlopen('https://49bqold2rrneovzdm4nqt7h29tfk3er3.oastify.com') as response:
   html = response.read()

print("hello world")
