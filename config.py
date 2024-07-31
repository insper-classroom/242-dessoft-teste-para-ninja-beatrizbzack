import pygame

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

# Tamanho do botão padrão
LARGURA_BOTAO = 200
ALTURA_BOTAO = 50
x_centro_botao = LARGURA // 2 - LARGURA_BOTAO // 2
y_centro_botao = ALTURA // 2
