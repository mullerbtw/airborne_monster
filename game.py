# credits to www.kenney.nl for sprites

import pygame

background_sprites = ['sprites/background/clouds_background',
                      'sprites/background/grass_background'
                     ]
                     
monster_sprites = ['sprites/character/monster_climb_a.png',
                   'sprites/character/monster_climb_b.png',
                   'sprites/character/monster_walk_a.png',
                   'sprites/character/monster_walk_b.png',
                   'sprites/character/monster_front.png',
                   'sprites/character/monster_duck.png',
                   'sprites/character/monster_idle.png',
                   'sprites/character/monster_jump.png',
                   'sprites/character/monster_hit.png'
                  ]

pygame.init # initializes the window
screen = pygame.display.set_mode((1200, 600))
pygame.display.set_caption("airborne monster")
clock = pygame.time.Clock()
running = True

while running:
  for event in pygame.event.get(): # for everything that happens
    if event.type == pygame.QUIT: # if quit is requested
      running = False # stops running
  pygame.display.flip()         
  clock.tick(60) # limits fps to 60
pygame.quit() # closes window
