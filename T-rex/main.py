import pygame
import pygame.display
import random
from pygame.locals import *
import asyncio
import time

async def main():

    # Inicjalizacja Pygame
    pygame.init()

    # Ustawienie rozmiaru okna
    width = 800
    height = 600

    # Tworzenie okna
    screen = pygame.display.set_mode((width, height))

    # Tytuł okna
    pygame.display.set_caption("Dino Game")

    # Zmienne
    clock = pygame.time.Clock()

    # Kolor tła
    bg_color = (255, 255, 255)

    # Kolor dinozaura
    dino_color = (0, 128, 128)

    # Wymiary dinozaura
    dino_width = 40
    dino_height = 60

    # Położenie dinozaura
    dino_x = width // 2
    dino_y = height - dino_height

    # Prędkość dinozaura
    dino_vel = 10

    # Kolor przeszkód
    obstacle_color = (255, 0, 0)

    # Szerokość i wysokość przeszkód
    obstacle_width = 20
    obstacle_height = 100

    # Lista przeszkód
    obstacles = []

    # Częstotliwość pojawiania się przeszkód
    spawn_rate = 1000

    # Czas od ostatniego pojawienia się przeszkód
    last_spawn = 0

    #zmienna punktów
    punkty = 0
    tab_punkty = []
    lastScore = 0
    best_p = 0

    #Prędkość gry
    speed = 60

    # Funkcja rysująca dinozaura
    def draw_dino(x, y):
        pygame.draw.rect(screen, dino_color, (x, y, dino_width, dino_height))

    # Funkcja rysująca przeszkodę
    def draw_obstacle(x, y):
        pygame.draw.rect(screen, obstacle_color, (x, y, obstacle_width, obstacle_height))

    black = (0, 0, 0)
    white = (255, 255, 255)

    def text_objects(text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()

    def button(msg, x, y, w, h):
        smallText = pygame.font.SysFont("comicsansms", 20)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ((x + (w / 2)), (y + (h / 2)))
        screen.blit(textSurf, textRect)

    # Główna pętla gry

    running = True
    while running:
        # Sprawdzenie zdarzeń
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Aktualizacja położenia dinozaura
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            dino_y -= dino_vel
        if keys[pygame.K_DOWN]:
            dino_y += dino_vel
        if keys[pygame.K_LEFT]:
            dino_x -= dino_vel
        if keys[pygame.K_RIGHT]:
            dino_x += dino_vel
        if keys[pygame.K_ESCAPE]:
            running = False
        if keys[pygame.K_LSHIFT]:
            dino_height = 30

        # Ograniczenie położenia dinozaura na ekran
        # Ograniczenie położenia dinozaura na ekran
        if dino_x < 0:
            dino_x = 0
        if dino_x > width - dino_width:
            dino_x = width - dino_width
        if dino_y < 0:
            dino_y = 0
        if dino_y > height - dino_height:
            dino_y = height - dino_height

        # Aktualizacja położenia przeszkód
        for obstacle in obstacles:
            obstacle[0] -= 10

        # Usuwanie przeszkód po wyjściu poza ekran
        obstacles = [obstacle for obstacle in obstacles if obstacle[0] + obstacle_width > 0]

        # Pojawianie się przeszkód
        current_time = pygame.time.get_ticks()
        if current_time - last_spawn > spawn_rate:
            last_spawn = current_time
            obstacle_y = random.randint(0, height - obstacle_height)
            obstacles.append([width, obstacle_y])

        # Sprawdzanie kolizji z przeszkodami
        for obstacle in obstacles:
            if dino_x < obstacle[0] + obstacle_width and dino_x + dino_width > obstacle[0]:
                if dino_y < obstacle[1] + obstacle_height and dino_y + dino_height > obstacle[1]:
                    time.sleep(1)
                    # running = False
                    running = True
                    dino_height = 60
                    obstacles = []
                    dino_x = width // 2
                    dino_y = height - dino_height
                    last_spawn = pygame.time.get_ticks()
                    tab_punkty.append(punkty)
                    for score in tab_punkty:
                        if score > lastScore:
                            best_p = score
                        lastScore = score
                    punkty = 0
                    obstacle_height = 100
                    speed = 60

                    ## Ekran restartu, nie działa podczas symulacji pygbag
                    # screen.fill(white)
                    # largeText = pygame.font.Font('freesansbold.ttf', 115)
                    # TextSurf, TextRect = text_objects("Restart?", largeText)
                    # TextRect.center = ((width / 2), (height / 2))
                    # screen.blit(TextSurf, TextRect)
                    #
                    # button("GO! - R", 150, 450, 100, 50)
                    # button("Quit - E", 550, 450, 100, 50)
                    #
                    # pygame.display.update()
                    # pygame.event.clear()
                    # event = pygame.event.wait()
                    # if event.type == KEYDOWN:
                    #     if event.key == K_e:
                    #         running = False
                    #     if event.key == K_r:
                    #         running = True
                    #         obstacles = []
                    #         dino_x = width // 2
                    #         dino_y = height - dino_height
                    #         last_spawn = pygame.time.get_ticks()
                    #         punkty = 0
                    #         obstacle_height = 100
                    #         speed = 60
        #liczenie punktów
        for obstacle in obstacles:
            if dino_x < obstacle[0] + obstacle_width-19 and dino_x + dino_width-39 > obstacle[0]:
                punkty = punkty + 1
                if obstacle_height < 280:
                    obstacle_height = obstacle_height + 4
                    speed = speed + 0.5
                    dino_height = dino_height + 1
                    if dino_height < 60:
                        dino_height = dino_height + 10

        # Rysowanie tła
        screen.fill(bg_color)

        # Rysowanie dinozaura
        draw_dino(dino_x, dino_y)

        # Rysowanie przeszkód
        for obstacle in obstacles:
            draw_obstacle(obstacle[0], obstacle[1])

        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects(f"{punkty}", largeText)
        TextRect.center = ((width / 2), (height / 2))
        screen.blit(TextSurf, TextRect)

        smallText = pygame.font.SysFont("comicsansms", 40)
        textSurf, textRect = text_objects(f"Najlepszy wynik: {best_p}", smallText)
        textRect.center = ((width / 2), (height / 15))
        screen.blit(textSurf, textRect)


        # Aktualizacja ekranu
        pygame.display.update()

        # Regulacja szybkości gry
        clock.tick(speed)

        await asyncio.sleep(0)

# Zakończenie Pygame
pygame.quit()
asyncio.run(main())

# Udostępniona gra w internecie bez opcji restartu

# <iframe
# msallowfullscreen="true"
# allow="autoplay; fullscreen *; geolocation; microphone; camera; midi; monetization; " \
#       "xr-spatial-tracking; gamepad; gyroscope; accelerometer; xr; cross-origin-isolated"
# src="https://v6p9d9t4.ssl.hwcdn.net/html/7362272/index.html"
# frameborder="0"
# allowfullscreen="true"
# scrolling="no"
# id="game_drop"
# allowtransparency="true"
# webkitallowfullscreen="true"
# mozallowfullscreen="true">
# </iframe>