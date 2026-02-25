import pygame
import sys
from config import *
from button import Button
from game import HangmanGame

pygame.init()

try:
    pygame.mixer.init()
except:
    print("Sound disabled")

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Professional Hangman")

clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 40)

def fade_in():
    fade = pygame.Surface((WIDTH, HEIGHT))
    fade.fill((0, 0, 0))
    for alpha in range(0, 255):
        fade.set_alpha(alpha)
        screen.blit(fade, (0, 0))
        pygame.display.update()
        pygame.time.delay(5)

def main():
    game = HangmanGame()

    start_button = Button("START", 350, 250, 200, 60, font)
    quit_button = Button("QUIT", 350, 350, 200, 60, font)
    restart_button = Button("RESTART", 350, 350, 200, 60, font)
    hint_button = Button("HINT (-1 Life)", 600, 500, 250, 60, font)

    state = "menu"
    running = True

    while running:
        clock.tick(FPS)
        screen.fill(GRAY)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if state == "menu":
                if start_button.is_clicked(event):
                    state = "game"
                    fade_in()
                if quit_button.is_clicked(event):
                    running = False

            elif state == "game":
                if event.type == pygame.KEYDOWN:
                    letter = event.unicode.lower()
                    if letter.isalpha():
                        game.guess_letter(letter)
                        if hint_button.is_clicked(event):
                            game.use_hint()

            elif state in ["won", "lost"]:
                if restart_button.is_clicked(event):
                    game.reset_game()
                    state = "game"

        # Draw states
        if state == "menu":
            start_button.draw(screen)
            quit_button.draw(screen)

        elif state == "game":
            game.draw(screen, font)
            hint_button.draw(screen)

            if game.is_won():
                state = "won"
                game.play_sound(game.win_sound)

            if game.is_lost():
                state = "lost"
                game.play_sound(game.lose_sound)

        elif state == "won":
            text = font.render("YOU WON!", True, GREEN)
            screen.blit(text, (350, 250))
            restart_button.draw(screen)

        elif state == "lost":
            text = font.render("YOU LOST!", True, RED)
            screen.blit(text, (350, 250))
            restart_button.draw(screen)

        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
