import pygame
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