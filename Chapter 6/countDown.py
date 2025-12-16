# Goal:
# Print a countdown before something "exciting" happens (like "Launching Rocket").

import time
 
count= int(input("Enter the counter num: "))

print("\nCountdown Starts Now: ")

for i in range(count,0,-1):
    print(i)
    time.sleep(3)

print("\nWOHOOO! Happy New Year....")