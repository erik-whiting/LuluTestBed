from LuluTest import *


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
