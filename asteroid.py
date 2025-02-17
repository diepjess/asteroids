import random
import pygame
from constants import *
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        
    def draw(self, screen):
        """Draw asteroid represented as a circle

        Args:
            screen (pygame.Surface): the Surface to draw on

        Returns:
            pygame.Rect: Rect bounding the changed pixels
        """
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        """Update position of asteroid to move in straight line

        Args:
            dt (float): delta time since last frame drawn
        """
        self.position += (self.velocity * dt)
    
    def split(self):
        """Split and asteroid
        If asteroid is smallest size, return
        Create two new asteroids with new radius stepped down
        Velocity angle of asteroids at random angle in opposite directions
        Speed of new asteroids scaled up to be faster
        """
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # randomize angle fo the split
        random_angle = random.uniform(20, 50)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        a_velocity = self.velocity.rotate(random_angle)
        b_velocity = self.velocity.rotate(-random_angle)
        
        asteroid_a = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_a.velocity =  a_velocity * 1.2
        asteroid_b = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_b.velocity =  b_velocity * 1.2