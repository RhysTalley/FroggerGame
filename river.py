import pygame, random
from log import Log

class River:

    SIZE = (600,30)
    SCREEN_DIMENSIONS = (600,500)

    def __init__(self, river_height: int, direction: str, number_of_logs: int):
        # Rivers information
        self.rect = pygame.Rect((0,river_height), River.SIZE)
        self.logs = []
        # number of logs
        self.add_logs(direction, number_of_logs, river_height+20)

    def add_logs(self, direction: str, number_of_logs: int, river_height: int):
        dp = []
        for _ in range(number_of_logs):
            while True:
                x_pos = random.randint(30, 570)
                valid = True
                for i in range(x_pos - 60, x_pos + 60):
                    if i in dp:
                        valid = False
                if valid:
                    dp.append(x_pos)
                    break
            self.logs.append(Log((x_pos, river_height), direction))