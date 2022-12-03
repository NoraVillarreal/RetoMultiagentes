import mesa
import numpy as np
import time

class agenteCarroV(mesa.Agent):
  # An agent with fixed initial wealth.

  def __init__(self, unique_id, model):
    super().__init__(unique_id, model)
    self.tipo = "carroV"

  def step(self):
    self.move()
    self.clean()

  def move(self):
      var = 0
      for i in self.model.middle:
        x, y = i
        if (x, y) == self.pos:
          var = 1

      x, y = self.pos
      x = x + 1
      self.newpos = (x, y)
      if (x == 4 or x == 5):
        if self.model.semaforo() or var == 1:
          if self.newpos in self.model.middle:
            if not (x == 10 or y == 10):
              if self.model.dirty_matrix[x][y] != 0:
                self.model.setClean(self.pos)
                self.model.grid.move_agent(self, self.newpos)
            else:
              x = 0
              if self.model.dirty_matrix[x][y] != 0:
                self.model.setClean(self.pos)
                self.model.grid.move_agent(self, self.newpos)
          else:
            self.model.setClean(self.pos)
            self.model.grid.move_agent(self, self.newpos)
      else:
        if not (x == 10 or y == 10):
          if self.model.dirty_matrix[x][y] != 0:
            self.model.setClean(self.pos)
            self.model.grid.move_agent(self, self.newpos)
        else:
          x = 0
          if self.model.dirty_matrix[x][y] != 0:
            self.model.setClean(self.pos)
            self.model.grid.move_agent(self, self.newpos)

      self.model.actPos(self.pos, self.unique_id)
    
  # verificar si singlegrid es suficiente para que no choquen

  def clean(self):
    if self.model.isDirty(self.pos):
      self.model.setDirty(self.pos)
    pass

class agenteCarroH(mesa.Agent):
  # An agent with fixed initial wealth.

  def __init__(self, unique_id, model):
    super().__init__(unique_id, model)
    self.tipo = "carroH"

  def step(self):
    self.move()
    self.clean()

  def move(self):
      var = 0
      for i in self.model.middle:
        x, y = i
        if (x, y) == self.pos:
          var = 1

      x, y = self.pos
      y = y + 1
      self.newpos = (x, y)
      if (y == 4 or y == 5):
        if (not self.model.semaforo()) or var == 1:
          if self.newpos in self.model.middle:
            if not (x == 10 or y == 10):
              if self.model.dirty_matrix[x][y] != 0:
                self.model.setClean(self.pos)
                self.model.grid.move_agent(self, self.newpos)
            else:
              y = 0
              if self.model.dirty_matrix[x][y] != 0:
                self.model.setClean(self.pos)
                self.model.grid.move_agent(self, self.newpos)
          else:
            self.model.setClean(self.pos)
            self.model.grid.move_agent(self, self.newpos)
      else:
        if not (x == 10 or y == 10):
          if self.model.dirty_matrix[x][y] != 0:
            self.model.setClean(self.pos)
            self.model.grid.move_agent(self, self.newpos)
        else:
          y = 0
          if self.model.dirty_matrix[x][y] != 0:
            self.model.setClean(self.pos)
            self.model.grid.move_agent(self, self.newpos)

      self.model.actPos(self.pos, self.unique_id)

  def clean(self):
    if self.model.isDirty(self.pos):
      self.model.setDirty(self.pos)
    pass


class agenteCarroHR(mesa.Agent):
  # An agent with fixed initial wealth.

  def __init__(self, unique_id, model):
    super().__init__(unique_id, model)
    self.tipo = "carroH"

  def step(self):
    self.move()
    self.clean()

  def move(self):
      var = 0
      for i in self.model.middle:
        x, y = i
        if (x, y) == self.pos:
          var = 1

      x, y = self.pos
      y = y - 1
      self.newpos = (x, y)
      if (y == 4 or y == 5):
        if (not self.model.semaforo()) or var == 1:
          if self.newpos in self.model.middle:
            if not (x == -1 or y == -1):
              if self.model.dirty_matrix[x][y] != 0:
                self.model.setClean(self.pos)
                self.model.grid.move_agent(self, self.newpos)
            else:
              y = 9
              if self.model.dirty_matrix[x][y] != 0:
                self.model.setClean(self.pos)
                self.model.grid.move_agent(self, self.newpos)
          else:
            self.model.setClean(self.pos)
            self.model.grid.move_agent(self, self.newpos)
      else:
        if not (x == -1 or y == -1):
          if self.model.dirty_matrix[x][y] != 0:
            self.model.setClean(self.pos)
            self.model.grid.move_agent(self, self.newpos)
        else:
          y = 9
          if self.model.dirty_matrix[x][y] != 0:
            self.model.setClean(self.pos)
            self.model.grid.move_agent(self, self.newpos)

      self.model.actPos(self.pos, self.unique_id)

  def clean(self):
    if self.model.isDirty(self.pos):
      self.model.setDirty(self.pos)
    pass

class agenteCarroVR(mesa.Agent):
  # An agent with fixed initial wealth.

  def __init__(self, unique_id, model):
    super().__init__(unique_id, model)
    self.tipo = "carroV"

  def step(self):
    self.move()
    self.clean()

  def move(self):
      var = 0
      for i in self.model.middle:
        x, y = i
        if (x, y) == self.pos:
          var = 1

      x, y = self.pos
      x = x - 1
      self.newpos = (x, y)
      if (x == 4 or x == 5):
        if self.model.semaforo() or var == 1:
          if self.newpos in self.model.middle:
            if not (x == 10 or y == 10):
              if self.model.dirty_matrix[x][y] != 0:
                self.model.setClean(self.pos)
                self.model.grid.move_agent(self, self.newpos)
            else:
              x = 9
              if self.model.dirty_matrix[x][y] != 0:
                self.model.setClean(self.pos)
                self.model.grid.move_agent(self, self.newpos)
          else:
            self.model.setClean(self.pos)
            self.model.grid.move_agent(self, self.newpos)
      else:
        if not (x == -1 or y == -1):
          if self.model.dirty_matrix[x][y] != 0:
            self.model.setClean(self.pos)
            self.model.grid.move_agent(self, self.newpos)
        else:
          x = 9
          if self.model.dirty_matrix[x][y] != 0:
            self.model.setClean(self.pos)
            self.model.grid.move_agent(self, self.newpos)

      self.model.actPos(self.pos, self.unique_id)
    
  # verificar si singlegrid es suficiente para que no choquen

  def clean(self):
    if self.model.isDirty(self.pos):
      self.model.setDirty(self.pos)
    pass


class TrafficModel(mesa.Model):
  """A model with some number of agents."""

  def __init__(self, N, width, height, percent):
    self.num_agents = N
    self.grid = mesa.space.SingleGrid(width, height, True)
    self.schedule = mesa.time.RandomActivation(self)
    self.celdas_suc = int(round((width * height) * percent))
    self.celdas_lim = (width * height) - self.celdas_suc
    self.dirty_matrix = np.zeros([width, height])
    self.sem = True
    self.middle = np.array([[4,4],[5,4],[4,5],[5,5]])
    self.intercept = np.array([(3,4),(4,3),(3,5),(4,6),(5,6),(6,5),(6,4),(5,3)])
    self.initial = np.array([(0,4),(4,0),(9,5),(5,9),(4,1),(1,4),(5,8),(8,5),(2,4),(4,2),(5,7),(7,5)])
    countw = 0
    counth = 0
    var = 1
    self.start = time.time()

    countcs = self.celdas_suc
    for x in self.dirty_matrix:
      if width < countcs:
        while counth < height and var == 1:
          countw = 0
          while countw < width and var == 1:
            if countcs > 0:
              self.dirty_matrix[countw][counth] = 1
              countw = countw + 1
              countcs = countcs - 1
            else:
              var = 0
          counth = counth + 1
      else:
        while countw < width and var == 1:

          if countcs > 0:
            self.dirty_matrix[countw][counth] = 1
            countw = countw + 1
            countcs = countcs - 1
            if countcs <= 0:
              var = 0
              pass
          else:
            var = 0
    counth = 0
    countw = 0
    if width < height:
      while countw < width:
        np.random.shuffle(self.dirty_matrix[countw])
        countw = countw + 1
      self.printarray()
    else:
      while counth < height:
        np.random.shuffle(self.dirty_matrix[counth])
        counth = counth + 1
      self.printarray()

    self.width = width
    self.height = height
    countag = 1
    #posagv = 1
    #posagh = 0

    for i in self.initial:
      x, y = i
      self.dirty_matrix[x][y] = 0

    self.ps = []
    
    a = agenteCarroV(countag, self)
    countag=countag+1
    b = agenteCarroH(countag, self)
    countag=countag+1
    self.schedule.add(a)
    self.schedule.add(b)
    self.grid.place_agent(a, (0, 4))
    self.ps.append([0,4])
    self.grid.place_agent(b, (4, 0))
    self.ps.append([4,0])
    c = agenteCarroVR(countag, self)
    countag=countag+1
    d = agenteCarroHR(countag, self)
    countag=countag+1
    self.schedule.add(c)
    self.schedule.add(d)
    self.grid.place_agent(c, (9, 5))
    self.ps.append([0,5])
    self.grid.place_agent(d, (5, 9))
    self.ps.append([5,0])
    e = agenteCarroV(countag, self)
    countag=countag+1
    f = agenteCarroH(countag, self)
    countag=countag+1
    self.schedule.add(e)
    self.schedule.add(f)
    self.grid.place_agent(e, (1, 4))
    self.ps.append([1,4])
    self.grid.place_agent(f, (4, 1))
    self.ps.append([4,1])
    g = agenteCarroVR(countag, self)
    countag=countag+1
    h = agenteCarroHR(countag, self)
    countag=countag+1
    self.schedule.add(g)
    self.schedule.add(h)
    self.grid.place_agent(g, (8, 5))
    self.ps.append([1,5])
    self.grid.place_agent(h, (5, 8))
    self.ps.append([5,1])
    i = agenteCarroV(countag, self)
    countag=countag+1
    j = agenteCarroH(countag, self)
    countag=countag+1
    self.schedule.add(i)
    self.schedule.add(j)
    self.grid.place_agent(i, (2, 4))
    self.ps.append([2,4])
    self.grid.place_agent(j, (4, 2))
    self.ps.append([4,2])
    k = agenteCarroVR(countag, self)
    countag=countag+1
    l = agenteCarroHR(countag, self)
    countag=countag+1
    self.schedule.add(k)
    self.schedule.add(l)
    self.grid.place_agent(k, (7, 5))
    self.ps.append([2,5])
    self.grid.place_agent(l, (5, 7))
    self.ps.append([5,2])
    

    """
    for i in range(self.num_agents):
      a = agenteCarroV(countag, self)
      countag=countag+1
      b = agenteCarroH(countag, self)
      countag=countag+1
      self.schedule.add(a)
      self.schedule.add(b)
      self.grid.place_agent(a, (0, i+4))
      self.grid.place_agent(b, (i+4, 0))
      """
      

  def step(self):
    self.schedule.step()
      

  def semaforo(self):
    if time.time() > self.start + 10:
      self.sem = not self.sem
      self.start = time.time()

    return self.sem

  def isDirty(self, new_position):
    if new_position != None:
      x, y = new_position
      if self.dirty_matrix[x][y] == 1:
        return True
      else:
        return False

  def setDirty(self, new_position):
    x, y = new_position
    self.celdas_suc = self.celdas_suc - 1
    self.celdas_lim = self.celdas_lim + 1
    self.dirty_matrix[x][y] = 0

  def setClean(self, new_position):
    x, y = new_position
    self.celdas_suc = self.celdas_suc + 1
    self.celdas_lim = self.celdas_lim - 1
    self.dirty_matrix[x][y] = 1

  def printarray(self):
    print(self.dirty_matrix)

  def porcentaje_celdas_limpias(self):
    return (self.celdas_lim / (self.width * self.height)) * 100
    pass

  def actPos(self, new_position, id):
    x,y = new_position
    self.ps[id-1] = [x,y]
    # print(self.ps)
    
