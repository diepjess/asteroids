import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot


class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0

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
        pygame.draw.polygon(screen, color, points, line_width)
    
    def rotate(self, dt):
        """Update rotation value based on delta time

        Args:
            dt (float): delta time since last frame drawn
        """
        self.rotation += (PLAYER_TURN_SPEED * dt)
    
    def update(self, dt):
        """Update player based on key press

        Args:
            dt (float): delta time since last frame drawn
        """
        self.shoot_timer -= dt
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    
    def shoot(self):
        if self.shoot_timer > 0:
            return
        self.shoot_timer = PLAYER_SHOOT_COOLDOWN
        shot = Shot(self.position.x, self.position.y)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOOT_SPEED