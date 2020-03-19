#! python3
# stopwatch.py - a simple stop watch program

import time

print('Press Enter to begin, then press enter to click and press ctrl-C to quit')

input()
print('Started/')
startTime = time.time()
lastTime = startTime
lapNum = 1

try:
  while True:
    input()
    lapTime = round(time.time()-lastTime, 2)
    totalTime = round(time.time()-startTime, 2)
    print('lap %s, total %s, lap time %s'%(lapNum, totalTime, lapTime), end='')
    lapNum += 1
    lastTime = time.time()
except KeyboardInterrupt:
  print('\ndone!')
