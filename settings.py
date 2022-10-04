class Settings:
    """Класс для хранения всех настроек игры."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана.
        self.screen_width = 1000
        self.screen_height = 650
        self.bg_color = (230, 230, 230)

        # Настройка корабля.
        self.ship_speed = 1.5

        # Параметры снаряда.
        self.bullel_speed = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet.color = (60, 60, 60)
        