
from datetime import datetime 

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

with open('readme.txt', 'w') as f:
    f.write(f"Last Update = {current_time}\n")