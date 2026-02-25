import pygame

class Button:
    def __init__(self, text, x, y, width, height, font):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.font = font
        self.base_color = (70,70,70)
        self.hover_color = (120,120,120)

    def draw(self, screen):
        mouse_pos = pygame.mouse.get_pos()
        color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.base_color
        pygame.draw.rect(screen, color, self.rect, border_radius=12)

        text_surface = self.font.render(self.text, True, (255,255,255))
        screen.blit(
            text_surface,
            (self.rect.x + self.rect.width//2 - text_surface.get_width()//2,
             self.rect.y + self.rect.height//2 - text_surface.get_height()//2)
        )

    def is_clicked(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                return True
        return False