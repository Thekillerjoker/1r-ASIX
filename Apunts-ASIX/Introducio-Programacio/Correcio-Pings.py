import os
stream = os.popen("ping -c 2 8.8.8.8 | grep received")
print("Ping a 8.8.8.8:")
print(stream.read())

google = os.popen("ping -c 2 google.com | grep received")
print("Ping a google.com:")
print(google.read())
# correcto
