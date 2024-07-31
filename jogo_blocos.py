import pygame
import sys
from gerador import gera_numeros
from config import *
import time
from telas import init, game_over

# Inicializa o Pygame
pygame.init()

# Inicializa a pontuação e números e vidas
pontuacao = 0
numero_alvo, numeros = gera_numeros()
vidas = 3 


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

    # Exibe as vidas 
    vidas_texto = fonte.render(f"Vidas: {vidas}", True, PRETO)
    TELA.blit(vidas_texto, (10, 90)) 
    
    pygame.display.flip()

# Loop principal do jogo
def main():
    global pontuacao, numero_alvo, numeros, vidas 
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
                                vidas -= 1 
                                time.sleep(1)
                                pontuacao = 0

                            if vidas == 0:
                                state = 'game_over'
                                vidas = 3
                                break 
                            
                            # Sorteia novos números para a próxima rodada
                            numero_alvo, numeros = gera_numeros()
            
            desenha_jogo()

if __name__ == "__main__":
    main()
