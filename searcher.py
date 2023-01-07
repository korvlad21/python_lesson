import os
import time

spisok = []

for adress, dirs, files in os.walk('/Users/vladislavkorobkin/Desktop'):
    for file in files:
        full = os.path.join(adress ,file)
        if time.time() - os.path.getctime(full) < 86400:
            spisok.append(full)
print(spisok)