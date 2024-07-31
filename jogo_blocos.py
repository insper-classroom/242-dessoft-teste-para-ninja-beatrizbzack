import pygame
import sys
from gerador import gera_numeros
from config import *
import time
from telas import init, game_over

# Inicializa o Pygame
pygame.init()

# Configurações da tela
LARGURA, ALTURA = 800, 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo de Matemática")

# Cores
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)
PRETO = (0, 0, 0)
CINZA = (169, 169, 169)

# Tamanho dos quadrados
LADO_QUADRADO = 100
ESPACO_ENTRE_QUADRADOS = 20

# Posicionamento dos quadrados
x_centro = LARGURA // 2 - LADO_QUADRADO // 2
y_inicio = ALTURA // 2 - (3 * LADO_QUADRADO + 2 * ESPACO_ENTRE_QUADRADOS) // 2

# Plataforma
plataforma_altura = 20
plataforma_pos = (x_centro - 10, y_inicio + 3 * LADO_QUADRADO + 2 * ESPACO_ENTRE_QUADRADOS, LADO_QUADRADO + 20, plataforma_altura)

# Fonte para números
fonte = pygame.font.Font(None, 74)

# Inicializa a pontuação e números
pontuacao = 0
numero_alvo, numeros = gera_numeros()

# Função para desenhar elementos na tela
def desenha_jogo():
    TELA.fill(BRANCO)
    
    # Desenha a plataforma
    pygame.draw.rect(TELA, CINZA, plataforma_pos)
    
    # Desenha os quadrados e números
    cores = [VERMELHO, VERDE, AZUL]
    for i in range(3):
        y = y_inicio + i * (LADO_QUADRADO + ESPACO_ENTRE_QUADRADOS)
        pygame.draw.rect(TELA, cores[i], (x_centro, y, LADO_QUADRADO, LADO_QUADRADO))
        texto = fonte.render(str(numeros[i]), True, PRETO)
        TELA.blit(texto, (x_centro + LADO_QUADRADO // 2 - texto.get_width() // 2, y + LADO_QUADRADO // 2 - texto.get_height() // 2))
    
    # Exibe o número alvo no canto superior esquerdo
    numero_alvo_texto = fonte.render(f"Alvo: {numero_alvo}", True, PRETO)
    TELA.blit(numero_alvo_texto, (10, 10))
    
    # Exibe a pontuação
    pontuacao_texto = fonte.render(f"Pontuação: {pontuacao}", True, PRETO)
    TELA.blit(pontuacao_texto, (10, 50))
    
    pygame.display.flip()

# Loop principal do jogo
def main():
    global pontuacao, numero_alvo, numeros
    state = 'iniciar'

    while True:
        if state == 'iniciar':
            state = init(TELA)
        elif state == 'game_over':
            state = game_over(TELA)
        elif state == 'jogar':
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    x, y = evento.pos # Pega a posição do clique do mouse - para identificar em qual quadrado ele está
                    for i in range(3):
                        y_quadrado = y_inicio + i * (LADO_QUADRADO + ESPACO_ENTRE_QUADRADOS)
                        if x_centro <= x <= x_centro + LADO_QUADRADO and y_quadrado <= y <= y_quadrado + LADO_QUADRADO:

                            if numeros[i] != numero_alvo - numeros[(i + 1) % 3] and numeros[i] != numero_alvo - numeros[(i + 2) % 3]:
                                # Apaga o quadrado clicado
                                pygame.draw.rect(TELA, BRANCO, (x_centro, y_quadrado, LADO_QUADRADO, LADO_QUADRADO))
                                pygame.display.update((x_centro, y_quadrado, LADO_QUADRADO, LADO_QUADRADO))

                                acertou_texto = fonte.render("Acertou!", True, VERDE)
                                TELA.blit(acertou_texto, (x_centro - (LADO_QUADRADO/2), y_quadrado)) 
                                pygame.display.flip() 
                                time.sleep(1)
                                pontuacao += 1

                            else:
                                # Apaga o quadrado clicado
                                pygame.draw.rect(TELA, BRANCO, (x_centro, y_quadrado, LADO_QUADRADO, LADO_QUADRADO))
                                pygame.display.update((x_centro, y_quadrado, LADO_QUADRADO, LADO_QUADRADO))

                                acertou_texto = fonte.render("Errou :(", True, VERMELHO)
                                TELA.blit(acertou_texto, (x_centro - (LADO_QUADRADO/2), y_quadrado)) 
                                pygame.display.flip() 
                                time.sleep(1)
                                pontuacao = 0
                            
                            # Sorteia novos números para a próxima rodada
                            numero_alvo, numeros = gera_numeros()
            
            desenha_jogo()

if __name__ == "__main__":
    main()
