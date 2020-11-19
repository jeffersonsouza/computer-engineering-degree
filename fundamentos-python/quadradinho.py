import pygame, random

pygame.init()

largura, altura = 800, 600

# define as cores dos quadradinhos
lightBlue = (11, 158, 217)
blue = (3, 44, 166)
darkBlue = (2, 24, 89)
white = (255,255,255)
black = (0,0,0)
pink = (242, 92, 162)
cores = [lightBlue, blue, darkBlue, white, pink]

clock = pygame.time.Clock()
tela = pygame.display.set_mode((largura, altura))

# variaveis de controle
clocks = 0
pontos = 0
segundos = 5
terminou = False

def gera_cor_aleatoria():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def gera_posicao_aleatoria(tamanho):
    return random.randint(0, largura - tamanho), random.randint(0, altura - tamanho)

def gera_quadrado_aletorio(tamanho):
    x, y = gera_posicao_aleatoria(tamanho)
    return pygame.Rect(x,y, tamanho, tamanho)

def mostra_tempo(tempo, pontos):
    fonte = pygame.font.SysFont('comicsansms', 18)
    texto = fonte.render(f"Tempo: {str(tempo)}s | Pontuação: {str(pontos)}", 1, white)
    posicao = texto.get_rect(centerx=tela.get_width()//2)
    tela.blit(texto, posicao)

def mostra_pontuacao(tela, pontos):
    fonte = pygame.font.SysFont('comicsansms', 36)
    texto = fonte.render(f"Pontuação: {str(pontos)} quadradinhos", 1, white)
    posicao = texto.get_rect(center=(tela.get_width()//2, tela.get_height()//2))
    tela.blit(texto, posicao)

quadradinhos = []

while not terminou:
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            position = pygame.mouse.get_pos()

            for quadrado in quadradinhos:
                if quadrado.collidepoint(position):
                    quadradinhos.remove(quadrado)
                    pontos = pontos + 1

    clocks += 1
    if clocks == 50:
        tela.fill(black)

        if segundos > 0:
            segundos -= 1
            clocks = 0

            for n in range(0, 20):
                quadrado = gera_quadrado_aletorio(25)
                pygame.draw.rect(tela, gera_cor_aleatoria(), quadrado)
                quadradinhos.append(quadrado)

            mostra_tempo(segundos, pontos)
        else:
            for quadrado in quadradinhos:
                quadradinhos.remove(quadrado)

            mostra_pontuacao(tela, pontos)

    pygame.display.update()

    # Configura 50 atualizações de tela por segundo
    clock.tick(50)

pygame.display.quit()
pygame.quit()
