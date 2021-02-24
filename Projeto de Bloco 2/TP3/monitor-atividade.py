import psutil
import pygame
import cpuinfo
from collections import namedtuple


class Monitor():
    # control
    running = False

    # Colors
    background = (232, 232, 232)
    background_contrast = (196, 182, 182)
    dark_blue = (48, 71, 94)
    dark_grey = (34, 40, 49)
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (240, 84, 84)

    pygame.display.set_caption('Monitor de Atividades')

    # Screen
    Coordinate = namedtuple('Coordinate', ['x', 'y'])
    screen_size = Coordinate(x=800, y=600)
    screen = pygame.display.set_mode(screen_size)

    surfaces_size = Coordinate(x=800, y=600)
    main_surface = pygame.surface.Surface(surfaces_size)

    def __init__(self):
        # Game init
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.Font(None, 32)

        self.loop()

    def draw_memory_usage(self, position: Coordinate, color):
        self.main_surface.fill(self.background)

        memory = psutil.virtual_memory()
        memory_total = round(psutil.virtual_memory().total/(1024*1024*1024), 2)

        width = self.main_surface.get_width() - 2 * 20
        percentage_used = width * memory.percent/100

        self.draw_text(self.main_surface, f"Uso de memória (total: {str(memory_total)}GB): {memory.percent}%", color, position)
        self.draw_bar_chart(self.main_surface, self.background_contrast, self.dark_blue, percentage_used, position.x, position.y + 25, width)
        self.screen.blit(self.main_surface, (0, 0))


    def draw_cpu_usage(self, position: Coordinate, color):
        cpu_percent = psutil.cpu_percent(interval=1)

        width = self.screen_size.x - 2 * 20
        percentage_used = width * cpu_percent/100

        self.draw_text(self.main_surface, f"Uso de CPU: {cpu_percent}%", self.dark_grey, position)
        self.draw_bar_chart(self.main_surface, self.background_contrast, color, percentage_used, position.x, position.y + 25, width)
        self.screen.blit(self.main_surface, (0, 0))

    def draw_cpu_info(self, position: Coordinate, color):
        info = cpuinfo.get_cpu_info()

        self.draw_text(self.main_surface, f"Informações do Processador:", color, position)
        self.draw_text(self.main_surface, f"Processador: {info['brand_raw']}", color, self.Coordinate(x=position.x, y=position.y + 30))
        self.draw_text(self.main_surface, f"Arquitetura: {info['arch_string_raw']}", color, self.Coordinate(x=position.x, y=position.y + 50))
        self.draw_text(self.main_surface, f"Tamanho da Palavra: {info['bits']} bits", color, self.Coordinate(x=position.x, y=position.y + 70))
        self.draw_text(self.main_surface, f"Cores: {psutil.cpu_count(logical=False)} físicos | {psutil.cpu_count()} lógicos", color, self.Coordinate(x=position.x, y=position.y + 90))

    def draw_disk_usage(self, position: Coordinate, color):
        hard_drive = psutil.disk_usage('.')
        hard_drive_percent = hard_drive.percent

        width = self.screen_size.x - 2 * 20
        percentage_used = width * hard_drive_percent/100

        self.draw_text(self.main_surface, f"Uso de Disco: {hard_drive_percent}%", self.dark_grey, position)
        self.draw_bar_chart(self.main_surface, self.background_contrast, color, percentage_used, position.x, position.y + 25, width)
        self.screen.blit(self.main_surface, (0, 0))

    def draw_ip_info(self, position: Coordinate, color):
        """
        Este método desenha no pygame o IP atual do usuário
        """
        addr = psutil.net_if_addrs()['en0'][0].address
        self.draw_text(self.main_surface, f"IP atual: {addr}", color, position)
        self.screen.blit(self.main_surface, (0, 0))

    def draw_bar_chart(self, surface, background, contrast, percentage_used, x, y, width, height = 50):
        pygame.draw.rect(surface, background, (x, y, width, height))
        pygame.draw.rect(surface, contrast, (x, y, percentage_used, height))

    def draw_text(self, surface, text, color, position: Coordinate):
        text = self.font.render(text, True, color)
        surface.blit(text, position)

    def loop(self):
        # Game loop
        self.running = True
        clock = pygame.time.Clock()
        while self.running:
            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # paint the screen
            self.screen.fill(self.background)

            self.draw_memory_usage(self.Coordinate(x=20, y=30), self.dark_grey)
            self.draw_cpu_usage(self.Coordinate(x=20, y=130), self.dark_blue)
            self.draw_cpu_info(self.Coordinate(x=20, y=330), self.dark_blue)
            self.draw_disk_usage(self.Coordinate(x=20, y=230), self.dark_blue)
            self.draw_ip_info(self.Coordinate(x=self.screen_size.x - 270, y=self.screen_size.y - 40), self.dark_grey)

            # Update the display
            pygame.display.update()

            # Update the display
            clock.tick(150)

        pygame.display.quit()


monitor = Monitor()
