import pygame

pygame.init()
clock=pygame.time.Clock()
screen = pygame.display.set_mode((400,600))

pygame.display.set_caption("Shooting Spaceship")
background_image = pygame.image.load("bg2.jpg").convert()

# Load the image for the player and name it as 'player_image'
player_image = pygame.image.load("s4.png").convert_alpha()


player=pygame.Rect(200,200,30,30)

WHITE=(255,255,255)
enemy=pygame.Rect(100,100,30,30)
xvel=2
yvel=3

# Create the variables 'angle' and 'change'
# Assign the value '0' to them
angle=0
change=0

while True:
  screen.blit(background_image,[0,0])
  
  # Events handling
  for event in pygame.event.get():
    # Event handling for closing the window
    if event.type == pygame.QUIT:
      pygame.quit()
    
    # Event handling if any key is pressed
    if event.type == pygame.KEYDOWN:
       # Checking if the pressed key is 'K_UP'
       if event.key == pygame.K_UP:
          change = 
       # Checking if the pressed key is 'K_DOWN'  
       if event.key ==pygame.K_DOWN:
          change = 
          
    # Event handling if any key is released
    if event.type == pygame.KEYUP:
      # Checking if the released key is 'K_UP' or 'K_DOWN'
      if event.key ==           or event.key ==             :
          change = 0
      
  
  enemy.x=enemy.x + xvel
  enemy.y=enemy.y + yvel 
  
  if enemy.x < -250 or enemy.x > 650 :
    xvel = -1*xvel
  
  if enemy.y < -250 or enemy.y > 850:  
    yvel = -1*yvel
    
  # Update the new 'angle' value by incrementing it with 'change'
  angle = angle + change
  # Rotating the 'player_image' to the 'angle' value
  newimage=pygame.transform.rotate(player_image,angle) 
  # Displaying the new rotated image for the player
  screen.blit(newimage ,player)
  
  
  pygame.draw.rect(screen,WHITE,enemy)

  pygame.display.update()
  clock.tick(30)
  
  
