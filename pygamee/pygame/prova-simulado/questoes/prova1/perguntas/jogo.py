import pygame, time
from perguntas import perguntas,premios

#BASICO
import pygame
from perguntas import perguntas,premios

def inicializa():
    pygame.init()
    window = pygame.display.set_mode((640,480))
    pygame.display.set_caption('Jogo do milhão')
    assets = {}
    fonte_padrao = pygame.font.get_default_font()
    assets['perguntas'] = pygame.font.Font(fonte_padrao,16)

    botoes = [[(20,180),(600,180),(600,220),(20,220)],
    [(20,240),(600,240),(600,280),(20,280)],
    [(20,300),(600,300),(600,340),(20,340)],
    [(20,360),(600,360),(600,400),(20,400)]
    ]

    state={
        'botoes': botoes,
    }
    return window,assets,state

def recebe_eventos(state):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
                for botao in state['botoes']:
                    if botao[0][0] <= x <= botao[1][0] and botao[0][1] <= y <= botao[2][1]:
                        print(premios[0])
                        return False
    return True


def desenha(window,assets,state):
    window.fill((0,0,0))

    cor = (255,0,0)
    vertices = [(20,15),(600,15),(600,120),(20,120)]
    pygame.draw.polygon(window,cor,vertices)

    cor1 = (255,0,0)
    vertices1 = [(20,180),(600,180),(600,220),(20,220)]
    pygame.draw.polygon(window,cor1,vertices1)

    cor2 = (255,0,0)
    vertices2 = [(20,240),(600,240),(600,280),(20,280)]
    pygame.draw.polygon(window,cor2,vertices2)

    cor3 = (255,0,0)
    vertices3 = [(20,300),(600,300),(600,340),(20,340)]
    pygame.draw.polygon(window,cor3,vertices3)

    cor4 = (255,0,0)
    vertices4 = [(20,360),(600,360),(600,400),(20,400)]
    pygame.draw.polygon(window,cor4,vertices4)


    p = assets['perguntas']

    imagem_texto1 = p.render(perguntas[0]['enunciado'],True,(0,0,0))
    window.blit(imagem_texto1,(35,30))

    imagem_texto2 = p.render(f"1. {perguntas[0]['alternativas'][0]}",True,(0,0,0))
    window.blit(imagem_texto2,(35,195))

    imagem_texto3 = p.render(f"2. {perguntas[0]['alternativas'][1]}",True,(0,0,0))
    window.blit(imagem_texto3,(35,255))

    imagem_texto4 = p.render(f"3. {perguntas[0]['alternativas'][2]}",True,(0,0,0))
    window.blit(imagem_texto4,(35,315))

    imagem_texto5 = p.render(f"4. {perguntas[0]['alternativas'][3]}",True,(0,0,0))
    window.blit(imagem_texto5,(35,375))

    pygame.display.update()

def game_loop(window,assets,state):
    while recebe_eventos(state):
        desenha(window,assets,state)

w,a,s = inicializa()
game_loop(w,a,s)



#PROFICIENTE
def inicializa():
    pygame.init()
    window = pygame.display.set_mode((640,480))
    pygame.display.set_caption('Jogo do milhão')
    assets = {}
    fonte_padrao = pygame.font.get_default_font()
    assets['perguntas'] = pygame.font.Font(fonte_padrao,16)
    assets['premio'] = pygame.font.Font(fonte_padrao,16)
    assets['tempo'] = pygame.font.Font(fonte_padrao,16)

    botoes = [[(20,180),(600,180),(600,220),(20,220)],
    [(20,240),(600,240),(600,280),(20,280)],
    [(20,300),(600,300),(600,340),(20,340)],
    [(20,360),(600,360),(600,400),(20,400)]
    ]

    state={
        'botoes': botoes,
        'indice_pergunta': 0,
        'premio_obtido' : 0,
        'tempo_inicial': time.time(),
    }
    return window,assets,state

def recebe_eventos(state):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x,y = event.pos
                for i,botao in enumerate(state['botoes']):
                    if botao[0][0] <= x <= botao[1][0] and botao[0][1] <= y <= botao[2][1]:
                        if i == perguntas[state['indice_pergunta']]['correta']:
                            state['premio_obtido'] += premios[state['indice_pergunta']]
                            state['indice_pergunta'] += 1
                            if state['indice_pergunta'] >= len(perguntas):
                                print({state['premio_obtido']})
                                return False
                            state['tempo_inicial'] = time.time()
                        else:
                            print(0)
                            return False
    return True

def desenha(window,assets,state):
    window.fill((0,0,0))

    cor = (255,0,0)
    vertices = [(20,15),(600,15),(600,120),(20,120)]
    pygame.draw.polygon(window,cor,vertices)

    cor1 = (255,0,0)
    vertices1 = [(20,180),(600,180),(600,220),(20,220)]
    pygame.draw.polygon(window,cor1,vertices1)

    cor2 = (255,0,0)
    vertices2 = [(20,240),(600,240),(600,280),(20,280)]
    pygame.draw.polygon(window,cor2,vertices2)

    cor3 = (255,0,0)
    vertices3 = [(20,300),(600,300),(600,340),(20,340)]
    pygame.draw.polygon(window,cor3,vertices3)

    cor4 = (255,0,0)
    vertices4 = [(20,360),(600,360),(600,400),(20,400)]
    pygame.draw.polygon(window,cor4,vertices4)


    p = assets['perguntas']

    imagem_texto1 = p.render(perguntas[state['indice_pergunta']]['enunciado'],True,(0,0,0))
    window.blit(imagem_texto1,(35,30))

    for i, alternativa in enumerate(perguntas[state['indice_pergunta']]['alternativas']):
        imagem_texto = p.render(f'{i+1}. {alternativa}', True, (0,0,0))
        window.blit(imagem_texto,(35,195+i*60))

    premio = assets['premio']
    imagem_texto2 = premio.render(f'Prêmio:{state["premio_obtido"]}',True,(255,255,255))
    window.blit(imagem_texto2,(20,460))

    tempo = assets['tempo']
    tempo_restante = 10 - int(time.time() - state['tempo_inicial'])
    imagem_texto3 = tempo.render(f"tempo: {tempo_restante}", True, (255,255,255))
    window.blit(imagem_texto3,(540,460))

    pygame.display.update()

def game_loop(window,assets,state):
    while recebe_eventos(state):
        desenha(window,assets,state)

w,a,s = inicializa()
game_loop(w,a,s)
