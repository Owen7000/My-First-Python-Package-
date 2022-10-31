__version__ = '0.1.0'

class Pet:
  def __init__(self, name, type, age):
    self.name = name
    self.type = type
    self.age = age
    
  def name(self):
    return self.name