# Imports 
import pygame
from os import path
import time 
from config import * 
import sys

def init(screen):
    running = True

    while running:
        # Fundo da tela
        screen.fill(BRANCO)
        texto1 = fonte.render("Jogo de Matemática", True, PRETO)
        texto2 = fonte.render("Encontre o número Intruso", True, AZUL)
        screen.blit(texto1, (LARGURA // 2 - texto1.get_width() // 2, ALTURA // 2 - texto1.get_height() - 100))
        screen.blit(texto2, (LARGURA // 2 - texto2.get_width() // 2, ALTURA // 2 - texto2.get_height()))

        # Botão de iniciar
        pygame.draw.rect(screen, VERMELHO, (x_centro_botao, y_centro_botao, LARGURA_BOTAO, ALTURA_BOTAO))
        texto_botao = fonte.render("Iniciar", True, BRANCO)
        screen.blit(texto_botao, (x_centro_botao + (LARGURA_BOTAO - texto_botao.get_width()) // 2, y_centro_botao + (ALTURA_BOTAO - texto_botao.get_height()) // 2))

        # Texto explicativo
        texto_explicativo = pygame.font.Font(None, 36).render("Aperte ESPAÇO ou clique no botão para iniciar", True, PRETO)
        screen.blit(texto_explicativo, (LARGURA // 2 - texto_explicativo.get_width() // 2, y_centro_botao + ALTURA_BOTAO + 20))

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    running = False
                    return 'jogar'
            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = evento.pos
                if x_centro_botao <= x <= x_centro_botao + LARGURA_BOTAO and y_centro_botao <= y <= y_centro_botao + ALTURA_BOTAO:
                    running = False
                    return 'jogar'
                
def game_over(screen):

    running = True

    while running:
            
        # Fundo da tela
        screen.fill(PRETO)
        texto = fonte.render("Game Over", True, BRANCO)
        screen.blit(texto, (LARGURA // 2 - texto.get_width() // 2, ALTURA // 2 - texto.get_height() - 100))

        # Botão de reiniciar
        pygame.draw.rect(screen, VERMELHO, (x_centro_botao, y_centro_botao, LARGURA_BOTAO, ALTURA_BOTAO))
        texto_botao = fonte.render("Jogar", True, BRANCO)
        screen.blit(texto_botao, (x_centro_botao + (LARGURA_BOTAO - texto_botao.get_width()) // 2, y_centro_botao + (ALTURA_BOTAO - texto_botao.get_height()) // 2))

        # Texto explicativo
        texto_explicativo = pygame.font.Font(None, 36).render("Aperte ESPAÇO ou clique no botão para REINICIAR o jogo", True, BRANCO)
        screen.blit(texto_explicativo, (LARGURA // 2 - texto_explicativo.get_width() // 2, y_centro_botao + ALTURA_BOTAO + 20))

        pygame.display.flip()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    running = False
                    return 'jogar'
            if evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = evento.pos
                if x_centro_botao <= x <= x_centro_botao + LARGURA_BOTAO and y_centro_botao <= y <= y_centro_botao + ALTURA_BOTAO:
                    running = False
                    return 'jogar'