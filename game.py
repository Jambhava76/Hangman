import pygame
import random
from config import *

class HangmanGame:
    def __init__(self):
        self.categories = {
            "Fruits": {
                "apple": "Keeps the doctor away",
                "banana": "A yellow curved fruit",
                "mango": "King of fruits",
                "orange": "Citrus fruit rich in vitamin C",
                "grapes": "Small fruit used to make wine"
            },
            "Vegetables": {
                "carrot": "Orange root vegetable",
                "potato": "Used to make fries",
                "onion": "Makes you cry when cutting",
                "spinach": "Popeye's favorite vegetable",
                "tomato": "Red and used in ketchup"
            },
            "Colors": {
                "red": "Color of blood",
                "blue": "Color of the sky",
                "green": "Color of grass",
                "yellow": "Color of the sun",
                "purple": "Royal color"
            }
        }

        self.correct_sound = self.load_sound("assets/sounds/correct.wav")
        self.wrong_sound = self.load_sound("assets/sounds/wrong.wav")
        self.win_sound = self.load_sound("assets/sounds/win.wav")
        self.lose_sound = self.load_sound("assets/sounds/lose.wav")

        self.images = []
        for i in range(MAX_LIVES + 1):
            img = pygame.image.load(f"assets/images/hangman{i}.jpg").convert_alpha()
            img = pygame.transform.scale(img, (250, 250))
            self.images.append(img)

        self.reset_game()

    def load_sound(self, path):
        try:
            return pygame.mixer.Sound(path)
        except:
            return None

    def play_sound(self, sound):
        if sound:
            sound.play()

    def reset_game(self):
        self.category = random.choice(list(self.categories.keys()))
        self.word = random.choice(list(self.categories[self.category].keys()))
        self.hint = self.categories[self.category][self.word]

        self.display = ["_"] * len(self.word)
        self.lives = MAX_LIVES
        self.guessed = set()
        self.hint_used = False

    def guess_letter(self, letter):
        if letter in self.guessed:
            return

        self.guessed.add(letter)

        if letter in self.word:
            self.play_sound(self.correct_sound)
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    self.display[i] = letter
        else:
            self.play_sound(self.wrong_sound)
            self.lives -= 1

    def use_hint(self):
        if not self.hint_used and self.lives > 1:
            self.lives -= 1
            self.hint_used = True

    def draw(self, screen, font):
        screen.blit(self.images[MAX_LIVES - self.lives], (50, 150))

        # Word display
        text = font.render(" ".join(self.display), True, WHITE)
        screen.blit(text, (350, 300))

        # Lives
        life_text = font.render(f"Lives: {self.lives}", True, RED)
        screen.blit(life_text, (50, 50))

        # Category
        category_text = font.render(f"Category: {self.category}", True, GREEN)
        screen.blit(category_text, (300, 50))

        # Hint (shown only if used)
        if self.hint_used:
            hint_text = font.render(f"Hint: {self.hint}", True, WHITE)
            screen.blit(hint_text, (200, 400))

    def is_won(self):
        return "_" not in self.display

    def is_lost(self):
        return self.lives <= 0