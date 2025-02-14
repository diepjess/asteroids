import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0

    # in the player class, provided by Boot.dev
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        """Draw player character that looks like a triangle

        Args:
            screen (pygame.Surface): the surface to draw on

        Returns:
            pygame.Rect: Rect bounding the changed pixels
        """
        color = "white"
        points = self.triangle()
        line_width = 2
        return pygame.draw.polygon(screen, color, points, line_width)