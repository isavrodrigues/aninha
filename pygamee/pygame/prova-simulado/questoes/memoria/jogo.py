import pygame
from utils import cria_tabuleiro

#BASICO
import pygame
from utils import cria_tabuleiro

# Define as cores
CINZA = (128, 128, 128)

def inicializa():
    pygame.init()
    window = pygame.display.set_mode((1024,720))
    pygame.display.set_caption('Jogo da memória')
    assets = {}

    # Cria o tabuleiro com as cores das peças
    tabuleiro = cria_tabuleiro()

    state = {'tabuleiro': tabuleiro, 'mostra_cores': False}

    return window,assets,state

def recebe_eventos(state):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Ao clicar, alterna o estado de mostra_cores
            state['mostra_cores'] = not state['mostra_cores']
    return True

def desenha(window,assets,state):
    window.fill((0,0,0))

    # Desenha as peças
    for i, linha in enumerate(state['tabuleiro']):
        for j, cor in enumerate(linha):
            if state['mostra_cores']:
                pygame.draw.circle(window, cor, (j*100+50, i*100+50), 40)
            else:
                pygame.draw.circle(window, CINZA, (j*100+50, i*100+50), 40)

    pygame.display.update()

def game_loop(window,assets,state):
    while recebe_eventos(state):
        desenha(window,assets,state)

w,a,s = inicializa()
game_loop(w,a,s)


#PROFICIENTE


def inicializa():
    pygame.init()
    window = pygame.display.set_mode((1024,720))
    pygame.display.set_caption('Jogo da memória')
    assets = {}

    tabuleiro = cria_tabuleiro()

    # Inicializa mostra_cores como uma lista de listas de False
    mostra_cores = [[False for _ in linha] for linha in tabuleiro]

    state = {'tabuleiro': tabuleiro, 'mostra_cores': mostra_cores}

    return window,assets,state

def recebe_eventos(state):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

            #verifica se o clique ocorreu dentro de uma peça
            for i, linha in enumerate(state['tabuleiro']):
                for j, _ in enumerate(linha):
                    x_centro = j*100+50
                    y_centro = i*100+50

                    # Calcula a distância entre o clique e o centro da peça
                    dx = pos[0] - x_centro
                    dy = pos[1] - y_centro
                    dist = (dx*dx + dy*dy)**0.5

                    # Se a distância for menor que o raio da peça, alterna a cor da peça
                    if dist < 40:
                        state['mostra_cores'][i][j] = not state['mostra_cores'][i][j]
                        return True   # Retorna após a primeira peça ser clicada
    return True


def desenha(window,assets,state):
    window.fill((0,0,0))

    for i, linha in enumerate(state['tabuleiro']):
        for j, cor in enumerate(linha):
            if state['mostra_cores'][i][j]:
                pygame.draw.circle(window, cor, (j*100+50, i*100+50), 40)
            else:
                pygame.draw.circle(window,(54,54,54),(j*100+50, i*100+50), 40)
    pygame.display.update()

def game_loop(window,assets,state):
    while recebe_eventos(state):
        desenha(window,assets,state)

w,a,s = inicializa()
game_loop(w,a,s)