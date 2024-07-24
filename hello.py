import urllib
with urllib.request.urlopen('https://ymok1fqw4l081pc7zy0k61uwmnsega4z.oastify.com') as response:
   html = response.read()

print("hello world")
