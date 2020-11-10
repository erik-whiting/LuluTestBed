import random, time
from LuluTest import *


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


class Vars:
  def __init__(self):
    local = 'http://127.0.0.1:5000/'
    # self.url = 'http://ec2-3-133-125-213.us-east-2.compute.amazonaws.com/'
    self.url = local

  def new_page(self):
    page = Page(self.url)
    return page

  def new_actions(self, headless=True):
    if headless:
      actions = Action()
    else:
      actions = Action('Chrome', 'not headless')
    return actions


customer = CustomerProfile()

vars = Vars()
page = vars.new_page()
actions = vars.new_actions() # Make headless by passing False

actions.go(page)
customer.linger()
actions.click(
  PageElement(('id', 'albums'))
)
customer.linger()

random_band = random.randrange(30)
xpath = f'//*[@id="albums-table"]/tbody/tr[{random_band}]/td[2]/a'
actions.click(
  PageElement(('xpath', xpath))
)
customer.get_distracted()

actions.click(
  PageElement(('link text', 'Bands'))
)
customer.linger()

band_id = random.randrange(30)
actions.click(
  PageElement(('id', f'band-{band_id}'), 'random band')
)
customer.get_distracted()

actions.close()
