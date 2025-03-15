import pygame
import random


pygame.init()

# Screen settings
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Collision Game")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)

# Player settings
player = pygame.Rect(300, 200, 50, 50)
speed = 5

# Enemy settings
num_enemies = 7
enemies = [pygame.Rect(random.randint(0, WIDTH-50), random.randint(0, HEIGHT-50), 50, 50) for _ in range(num_enemies)]

# Score
score = 0
font = pygame.font.Font(None, 36)

# Game loop
running = True
while running:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > 0:
        player.x -= speed
    if keys[pygame.K_RIGHT] and player.x < WIDTH - 50:
        player.x += speed
    if keys[pygame.K_UP] and player.y > 0:
        player.y -= speed
    if keys[pygame.K_DOWN] and player.y < HEIGHT - 50:
        player.y += speed

    # Collision detection
    for enemy in enemies:
        if player.colliderect(enemy):
            score += 1
            enemy.x, enemy.y = random.randint(0, WIDTH-50), random.randint(0, HEIGHT-50)  # Respawn enemy

    # Drawing
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, player)
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

    # Display score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    pygame.display.update()

pygame.quit()
