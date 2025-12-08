import os
import time
from datetime import datetime
for i in range(3):
    temps1 = time.time()
    os.system("wget -q -o /dev/null https://ash-speed.hetzner.com/100MB.bin ")
    temps2 = time.time()
    durada = temps2 -temps1
    moment = datetime.now()
    data = moment.strftime("%Y-%m-%d")
    hora = moment.strftime("%H:%M:%S")
    print(f"{data}, {hora},{durada:.2f}")
    time.sleep(10)