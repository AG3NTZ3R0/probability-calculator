import copy
import random
# Consider using the modules imported above.

class Hat:
  """Represent a ball probability experiment."""

  def __init__(self, **kwargs):
    """Initialize attributes for ball probability."""
    self.__dict__.update(kwargs)
    tmp_dict = self.__dict__.copy()
    self.contents = []
    for key, value in tmp_dict.items():
      for i in range(value):
        self.contents.append(key)

  def draw(self, num_balls):
    """Randomly select n ball(s) from the hat."""
    selection = []
    for i in range(num_balls):
      ball = random.choice(self.contents)
      self.contents.remove(ball)
      selection.append(ball)
      if len(self.contents) == 0:
        break
    return selection


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count = 0
  for i in range(num_experiments):
    expected_copy = copy.deepcopy(expected_balls)
    hat_copy = copy.deepcopy(hat)
    colors_gotten = hat_copy.draw(num_balls_drawn)
    for color in colors_gotten:
      if(color in expected_copy):
        expected_copy[color]-=1
    
    if(all(x <= 0 for x in expected_copy.values())):
      count += 1
  probability = count / num_experiments
  return probability