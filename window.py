import pygame
import math


class Window():
  (WIDTH, HEIGHT) = (800, 600)
  BACKGROUND_COLOR = (255, 255, 255)
  RUNNING = True
  UNIT_SIZE = 100
  (CENTER_X, CENTER_Y) = (WIDTH/2, HEIGHT/2)
  (PLANE_WIDTH, PLANE_HEIGHT) = (10, 10)
  
  def __init__(self, title):
    self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
    pygame.display.set_caption(title)
    self.screen.fill(self.BACKGROUND_COLOR)

    self.update()


  def run(self):
    while self.RUNNING:
      self.draw_components()
      self.handle_events()

  def draw_components(self):
    self.screen.fill(self.BACKGROUND_COLOR)
    self.draw_coordinates()
    self.draw_robot((0, 0, 0), 0.25, (0, 0, 0))
    self.update()

  def draw_coordinates(self):
    color_line = (200, 200, 200)
    for y in range(-self.PLANE_HEIGHT, self.PLANE_HEIGHT+1):
      x1 = self.CENTER_X - (self.UNIT_SIZE * self.PLANE_WIDTH)
      y1 = self.CENTER_Y + (y * self.UNIT_SIZE)
      x2 = self.CENTER_X + (self.UNIT_SIZE * self.PLANE_WIDTH)
      y2 = self.CENTER_Y + (y * self.UNIT_SIZE)
      pygame.draw.line(self.screen, color_line, (x1, y1), (x2, y2),width=3)
    for x in range(-self.PLANE_WIDTH, self.PLANE_WIDTH+1):
      x1 = self.CENTER_X + (x * self.UNIT_SIZE)
      y1 = self.CENTER_Y - (self.UNIT_SIZE * self.PLANE_HEIGHT)
      x2 = self.CENTER_X + (x * self.UNIT_SIZE)
      y2 = self.CENTER_Y + (self.UNIT_SIZE * self.PLANE_HEIGHT)
      pygame.draw.line(self.screen, color_line, (x1, y1), (x2, y2),width=3)
    color_line = (255, 0, 0)
    pygame.draw.line(self.screen, color_line, (self.CENTER_X, self.CENTER_Y), (self.CENTER_X, self.CENTER_Y - self.UNIT_SIZE), width=3)
    color_line = (0, 0, 255)
    pygame.draw.line(self.screen, color_line, (self.CENTER_X, self.CENTER_Y), (self.CENTER_X + self.UNIT_SIZE, self.CENTER_Y), width=3)


  def draw_robot(self, robot_pose, robot_radius, robot_color):
    (x, y, theta) = robot_pose
    x = self.CENTER_X + (x * self.UNIT_SIZE)
    y = self.CENTER_Y - (y * self.UNIT_SIZE)
    rad = robot_radius * self.UNIT_SIZE
    x1 = x - (math.cos(theta) * rad)
    y1 = y + (math.sin(theta) * rad)
    x2 = x + (math.cos(theta) * rad)
    y2 = y - (math.sin(theta) * rad)
    pygame.draw.circle(self.screen, center=(x, y), radius=(robot_radius * self.UNIT_SIZE), color=(robot_color), width=5)
    pygame.draw.line(self.screen, robot_color, (x1, y1), (x2, y2), width=5)
    x1 = x2
    y1 = y2
    x2 = x + (math.cos(theta + 0.3) * rad * 0.6)
    y2 = y - (math.sin(theta + 0.3) * rad * 0.6)
    x3 = x + (math.cos(theta - 0.3) * rad * 0.6)
    y3 = y - (math.sin(theta - 0.3) * rad * 0.6)
    pygame.draw.polygon(self.screen, color=(robot_color), points=[(x1, y1), (x2, y2), (x3, y3)])


    




  def handle_events(self):
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.RUNNING = False

      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_i:
          self.UNIT_SIZE *= 2

        if event.key == pygame.K_o:
          self.UNIT_SIZE /= 2

        if event.key == pygame.K_LEFT:
          self.CENTER_X -= 10

        if event.key == pygame.K_RIGHT:
          self.CENTER_X += 10

        if event.key == pygame.K_UP:
          self.CENTER_Y -= 10

        if event.key == pygame.K_DOWN:
          self.CENTER_Y += 10
    


  def update(self):
    pygame.display.flip()


    
