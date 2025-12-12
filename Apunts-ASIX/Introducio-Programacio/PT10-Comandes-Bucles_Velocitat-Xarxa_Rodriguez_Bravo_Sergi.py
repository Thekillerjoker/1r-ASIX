import os
import time
from datetime import datetime
for i in range(3):
    temps1 = time.time()
    os.system("wget -q -o /dev/null https://ash-speed.hetzner.com/100MB.bin ")
    temps2 = time.time()
    durada = temps2 - temps1
    moment = datetime.now()
    data = moment.strftime("%Y-%m-%d")
    hora = moment.strftime("%H:%M:%S")
    print(f"{data}, {hora},{durada:.2f}") # con .2f te obliga a que el valor de la durada te la mueste con dos decimales
    time.sleep(10)