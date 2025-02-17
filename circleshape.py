import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass
    
    def collides_with(self, other):
        """Checks if object collides with other object.
        Other object is considered colliding with if 
        distance to other object is less than or equal to sum of their radius.

        Args:
            other (CircleShape): other circle shape to detect collision with

        Returns:
            boolean: True if there is collision
        """
        distance = self.position.distance_to(other.position)
        radius_sum = self.radius + other.radius
        return distance <= radius_sum