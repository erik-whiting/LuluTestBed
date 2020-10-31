import random, time

class CustomerProfile:
  # For testing purposes, I am making the wait times much shorter than
  # they probably would be in a real life situation.
  def __init__(self):
    self.description = 'Typical customer usage'
  
  def linger(self):
    time.sleep(random.randrange(1, 5))

  def get_distracted(self):
    time.sleep(random.randrange(3, 7))
  
  def go_to_bathroom(self):
    time.sleep(random.randrange(5, 9))
  
  def go_to_lunch(self):
    time.sleep(random.randrange(7, 11))
