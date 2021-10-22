import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.markers as m
import random
%matplotlib inline  

fig, ax = plt.subplots()
lim = -5.8, 5.7
ax.set(xlim = lim, ylim = lim)

min = 1
max = 6

class Dice(object):
  
  def __init__(self, size = 6, color = 'r', radius = 0.5):
    self.size = size
    self.color = color
    self.radius = radius

  def increase_length(self, l):
    self.size = self.size + l
    return (self.size)

  def drawsquare(self):
    plt.gca().add_patch(plt.Rectangle((0, 0), self.size, self.size, fc=self.color))
    plt.axis('scaled')
    plt.show()

  def roll(self, number = 1):
    self.number = number
    center = self.size/2
    plt.gca().add_patch(plt.Rectangle((0, 0), self.size, self.size, fc=self.color))

    plt.gca().add_patch(plt.Circle((0, 0), 0.1, fc='white'))
    plt.gca().add_patch(plt.Circle((0, self.size), 0.1, fc='white'))
    plt.gca().add_patch(plt.Circle((self.size, 0), 0.1, fc='white'))
    plt.gca().add_patch(plt.Circle((self.size, self.size), 0.1, fc='white'))    
    
    if self.number == 1:
      plt.gca().add_patch(plt.Circle((center, center), radius=self.radius, fc='white'))
    
    elif self.number == 2:
      plt.gca().add_patch(plt.Circle((2, 2), radius=self.radius, fc='white'))
      plt.gca().add_patch(plt.Circle((4, 4), radius=self.radius, fc='white'))

    elif self.number == 3:
      plt.gca().add_patch(plt.Circle((1.5, 1.5), radius=self.radius, fc='white'))
      plt.gca().add_patch(plt.Circle((4.5, 4.5), radius=self.radius, fc='white'))
      plt.gca().add_patch(plt.Circle((center, center), radius=self.radius, fc='white'))      

    elif self.number == 4:
      plt.gca().add_patch(plt.Circle((2, 2), radius=self.radius, fc='white'))
      plt.gca().add_patch(plt.Circle((4, 4), radius=self.radius, fc='white'))
      plt.gca().add_patch(plt.Circle((2, 4), radius=self.radius, fc='white'))
      plt.gca().add_patch(plt.Circle((4, 2), radius=self.radius, fc='white'))

    elif self.number == 5:
      plt.gca().add_patch(plt.Circle((center, center), radius=self.radius, fc='white'))
      plt.gca().add_patch(plt.Circle((1.5, 1.5), radius=self.radius, fc='white'))
      plt.gca().add_patch(plt.Circle((4.5, 4.5), radius=self.radius, fc='white'))
      plt.gca().add_patch(plt.Circle((1.5, 4.5), radius=self.radius, fc='white'))
      plt.gca().add_patch(plt.Circle((4.5, 1.5), radius=self.radius, fc='white'))

    elif self.number == 6:
      plt.gca().add_patch(plt.Circle((1.5, 1.5), radius=self.radius, fc='white'))
      plt.gca().add_patch(plt.Circle((1.5, 3), radius=self.radius, fc='white'))
      plt.gca().add_patch(plt.Circle((1.5, 4.5), radius=self.radius, fc='white'))
      plt.gca().add_patch(plt.Circle((4.5, 4.5), radius=self.radius, fc='white'))
      plt.gca().add_patch(plt.Circle((4.5, 3), radius=self.radius, fc='white'))
      plt.gca().add_patch(plt.Circle((4.5, 1.5), radius=self.radius, fc='white'))

    else:
      marker_obj = m.MarkerStyle('$?$')
      path = marker_obj.get_path().transformed(marker_obj.get_transform())
      patch = mpl.patches.PathPatch( path, facecolor="white", lw=2)
      ax.add_patch(patch)

    plt.axis('scaled')
    plt.show()

play = Dice()
play.roll(random.randint(min, max)) #Default is random, you can set specific number too
