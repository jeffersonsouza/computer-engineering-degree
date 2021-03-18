import psutil
import pygame
import cpuinfo
import sys
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

    views = ['memory', 'cpu', 'network', 'disk']
    current_view = 1

    surfaces_size = Coordinate(x=800, y=600)
    cpu_surface = pygame.surface.Surface(surfaces_size)
    memory_surface = pygame.surface.Surface(surfaces_size)
    disc_surface = pygame.surface.Surface(surfaces_size)
    network_surface = pygame.surface.Surface(surfaces_size)

    def __init__(self):
        # Game init
        pygame.init()
        pygame.font.init()
        self.font = pygame.font.Font(None, 32)
        self.font_normal = pygame.font.Font(None, 20)

        self.loop()

    def draw_memory_usage(self, position: Coordinate, color):
        self.memory_surface.fill(self.background)

        memory = psutil.virtual_memory()
        memory_total = round(psutil.virtual_memory().total / (1024 * 1024 * 1024), 2)

        width = self.memory_surface.get_width() - 2 * 20
        percentage_used = width * memory.percent / 100

        self.draw_text(self.memory_surface, f"Uso de memória (total: {str(memory_total)}GB): {memory.percent}%", color,
                       position)
        self.draw_bar_chart(self.memory_surface, self.background_contrast, self.dark_blue, percentage_used, position.x,
                            position.y + 25, width)
        self.screen.blit(self.memory_surface, (0, 0))

    def draw_cpu_usage(self, position: Coordinate, color):
        self.cpu_surface.fill(self.background)
        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_percent_per_cores = psutil.cpu_percent(interval=1, percpu=True)

        width = self.screen_size.x - 2 * 20
        percentage_used = width * cpu_percent / 100

        self.draw_text(self.cpu_surface, f"Uso de CPU: {cpu_percent}%", self.dark_grey, position)
        self.draw_bar_chart(self.cpu_surface, self.background_contrast, color, percentage_used, position.x, position.y + 25, width)

        cores_initial_x = position.x
        width_per_core = (self.screen_size.x - (len(cpu_percent_per_cores) * 10) - (position.x * 2)) / len(cpu_percent_per_cores)

        for counter, core_usage in enumerate(cpu_percent_per_cores, start=1):
            percentage_used_per_core = 200 * core_usage / 100
            self.draw_bar_chart(
                self.cpu_surface,
                color,
                self.background_contrast,
                percentage_used_per_core,
                cores_initial_x,
                position.y + 175,
                width_per_core,
                200,
                'y',
                f"   {counter} ",
                f"{percentage_used_per_core}%"
            )
            cores_initial_x += width_per_core + 10

        self.screen.blit(self.cpu_surface, (0, 0))

    def draw_cpu_info(self, position: Coordinate, color):
        info = cpuinfo.get_cpu_info()

        self.draw_text(self.cpu_surface, f"Informações do Processador:", color, position)
        self.draw_text(self.cpu_surface, f"Processador: {info['brand_raw']}", color,
                       self.Coordinate(x=position.x, y=position.y + 30))
        self.draw_text(self.cpu_surface, f"Arquitetura: {info['arch_string_raw']}", color,
                       self.Coordinate(x=position.x, y=position.y + 50))
        self.draw_text(self.cpu_surface, f"Tamanho da Palavra: {info['bits']} bits", color,
                       self.Coordinate(x=position.x, y=position.y + 70))
        self.draw_text(self.cpu_surface,
                       f"Cores: {psutil.cpu_count(logical=False)} físicos | {psutil.cpu_count()} lógicos", color,
                       self.Coordinate(x=position.x, y=position.y + 90))

    def draw_disk_usage(self, position: Coordinate, color):
        self.disc_surface.fill(self.background)
        hard_drive = psutil.disk_usage('.')
        hard_drive_percent = hard_drive.percent

        width = self.screen_size.x - 2 * 20
        percentage_used = width * hard_drive_percent / 100

        self.draw_text(self.disc_surface, f"Uso de Disco: {hard_drive_percent}%", self.dark_grey, position)
        self.draw_bar_chart(self.disc_surface, self.background_contrast, color, percentage_used, position.x,
                            position.y + 25, width)
        self.screen.blit(self.disc_surface, (0, 0))

    def draw_ip_info(self, position: Coordinate, color):
        self.network_surface.fill(self.background)

        addr = psutil.net_if_addrs()['en0'][0].address
        self.draw_text(self.network_surface, f"IP atual: {addr}", color, position)
        self.screen.blit(self.network_surface, (0, 0))

    def draw_bar_chart(self, surface, background, contrast, percentage_used, x, y, width, height=50, axys='x',
                       top_label='', bottom_label=''):
        pygame.draw.rect(surface, background, (x, y, width, height))
        pygame.draw.rect(
            surface,
            contrast,
            (x, y, percentage_used if axys == 'x' else width, percentage_used if axys == 'y' else height)
        )

        if axys == 'y':
            if top_label:
                self.draw_text(surface, top_label, contrast, self.Coordinate(x=x, y=y - 25))
            if bottom_label:
                self.draw_text(surface, bottom_label, contrast, self.Coordinate(x=x, y=(y + height + 15)), 'normal')

    def draw_text(self, surface, text, color, position: Coordinate, font_size='title'):
        text = self.font_normal.render(text, True, color) if font_size == 'normal' else self.font.render(text, True,
                                                                                                         color)
        surface.blit(text, position)

    def handle_keys(self, event):
        if event.key == pygame.K_RIGHT:
            self.current_view = self.current_view + 1 if self.current_view < len(self.views) - 1 else 0
        if event.key == pygame.K_LEFT:
            self.current_view = self.current_view - 1 if self.current_view > 0 else len(self.views) - 1

    def handle_quit(self):
        self.running = False
        sys.exit()

    def loop(self):
        # Game loop
        self.running = True
        clock = pygame.time.Clock()
        while self.running:
            # events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.handle_quit()
                if event.type == pygame.KEYDOWN:
                    self.handle_keys(event)

            # paint the screen
            self.screen.fill(self.background)
            # print(self.views[self.current_view], self.current_view)
            if self.views[self.current_view] == 'memory':
                self.draw_memory_usage(self.Coordinate(x=20, y=30), self.dark_grey)
            if self.views[self.current_view] == 'disk':
                self.draw_disk_usage(self.Coordinate(x=20, y=230), self.dark_blue)
            if self.views[self.current_view] == 'network':
                self.draw_ip_info(self.Coordinate(x=self.screen_size.x - 270, y=self.screen_size.y - 40),
                                  self.dark_grey)
            if self.views[self.current_view] == 'cpu':
                self.draw_cpu_info(self.Coordinate(x=20, y=330), self.dark_blue)
                self.draw_cpu_usage(self.Coordinate(x=20, y=130), self.dark_blue)

            # Update the display
            pygame.display.update()

            # Update the display
            clock.tick(150)

        pygame.display.quit()


monitor = Monitor()
