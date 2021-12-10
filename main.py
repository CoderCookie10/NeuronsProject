class Neuron: 
  def __init__(self, ntype='interneuron', threshold=3, name='N1'):
    self.type = ntype
    self.threshold = threshold
    self.connect_axon = []
    self.connect_dendrite = []
    self.name = name

  def rconnect(self, neuron):
    self.connect_dendrite.append(neuron)
    neuron.connect_axon.append(self)

  def receive(self, strength, fromn):
    print(f"{self.name}: Signal Received... Undergoing Action Potential...")
    if self.threshold <= strength:
      print(f"{self.name}: Action Potential Success!!!")
      self.fire(strength, fromn)
    else:
      print("Action Potential Fail.")

  def fire(self, strength, received=None):
    for neuron in self.connect_axon:
      if neuron == received:
        pass
      else:
        print(f"{self.name}: Firing...")
        neuron.receive(strength, self)

class Muscle:
  def __init__(self, threshold=3, name='M1'):
    self.threshold = threshold
    self.connect_axon = []
    self.connect_dendrite = []
    self.name = name

  def rconnect(self, neuron):
    self.connect_dendrite.append(neuron)
    neuron.connect_axon.append(self)

  def receive(self, strength, fromn):
    print(f"{self.name}: Signal Received!")
    if self.threshold <= strength:
      print("Muscle Moved!")
    else:
      print("Threshold too high.")

n1 = Neuron('interneuron', 2)
n2 = Neuron('motor', 3, 'N2')
m = Muscle()
n2.rconnect(n1)
m.rconnect(n2)

n1.fire(4)
