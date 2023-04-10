import time
class StopWatch:
 def __init__(self):
  self.start_time = time.time()
 def start(self):
  self.start_time = time.time()
 def stop(self):
  self.end_time = time.time()
 def elapsed_time(self):
  return (self.end_time - self.start_time)*1000
sum=0
sw = StopWatch()
sw.start()
for i in range(1000001):
 sum+=i
sw.stop()
print(f"Time taken:{round(sw.elapsed_time(),2)}ms")
