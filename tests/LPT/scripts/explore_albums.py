import random
from LuluTest import *

from vars import Vars
from customer_profile import CustomerProfile

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
