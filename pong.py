import pygame
import sys

# Inicialização do Pygame 
pygame.init()

# Configurações da tela
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Pong-Game")

# Cores do jogo
preto = (0, 0, 0)
branco = (255, 255, 255)

# Variáveis da raquete
raquete_largura = 10
raquete_altura = 100
raquete_velocidade = 10

# Variáveis da bola
tamanho_bolinha = 20
bolinha_velocidade_x = 7
bolinha_velocidade_y = 7

# Posições iniciais
player1_x = 50
player1_y = (altura_tela - raquete_altura) // 2
player2_x = largura_tela - 50 - raquete_largura
player2_y = (altura_tela - raquete_altura) // 2
bolinha_x = (largura_tela - tamanho_bolinha) // 2
bolinha_y = (altura_tela - tamanho_bolinha) // 2

# Placar
player1_placar = 0
player2_placar = 0
font = pygame.font.Font(None, 74)

# Loop principal
rodando = True
clock = pygame.time.Clock()

while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Verificação de teclas pressionadas do player 1
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1_y > 0:
        player1_y -= raquete_velocidade
    if keys[pygame.K_s] and player1_y < altura_tela - raquete_altura:
        player1_y += raquete_velocidade
    if keys[pygame.K_UP] and player2_y > 0:
        player2_y -= raquete_velocidade
    if keys[pygame.K_DOWN] and player2_y < altura_tela - raquete_altura:
        player2_y += raquete_velocidade

    bolinha_x += bolinha_velocidade_x
    bolinha_y += bolinha_velocidade_y

    # Colisões com a parede superior e inferior
    if bolinha_y <= 0 or bolinha_y >= altura_tela - tamanho_bolinha:
        bolinha_velocidade_y *= -1

    # Colisões com as raquetes
    if (bolinha_x <= player1_x + raquete_largura and player1_y < bolinha_y < player1_y + raquete_altura) or (bolinha_x >= player2_x - tamanho_bolinha and player2_y < bolinha_y < player2_y + raquete_altura):
        bolinha_velocidade_x *= -1

    # Verificar se a bola passou das raquetes 1 e 2
    if bolinha_x <= 0:
        player2_placar += 1
        bolinha_x, bolinha_y = (largura_tela - tamanho_bolinha) // 2, (altura_tela - tamanho_bolinha) // 2
        bolinha_velocidade_x = 7
        bolinha_velocidade_y = 7

    if bolinha_x >= largura_tela - tamanho_bolinha:
        player1_placar += 1
        bolinha_x, bolinha_y = (largura_tela - tamanho_bolinha) // 2, (altura_tela - tamanho_bolinha) // 2
        bolinha_velocidade_x = -7
        bolinha_velocidade_y = 7

    # Preenchimento da tela
    tela.fill(preto)

    # Desenhando o player 1
    pygame.draw.rect(tela, branco, (player1_x, player1_y, raquete_largura, raquete_altura))

    # Desenhando o player 2
    pygame.draw.rect(tela, branco, (player2_x, player2_y, raquete_largura, raquete_altura))

    # Desenhando a Bolinha 
    pygame.draw.ellipse(tela, branco, (bolinha_x, bolinha_y, tamanho_bolinha, tamanho_bolinha))

    # Desenhando linha central
    pygame.draw.aaline(tela, branco, (largura_tela // 2, 0), (largura_tela // 2, altura_tela))

    # Placar Player 1
    player1_text = font.render(str(player1_placar), True, branco)
    tela.blit(player1_text, (largura_tela // 4, 20))

    # Placar Player 2 
    player2_text = font.render(str(player2_placar), True, branco)
    tela.blit(player2_text, (largura_tela - largura_tela // 4, 20))

    # Atualização da tela
    pygame.display.flip()

    # Controle de FPS
    clock.tick(60)    

# Encerramento do Código
pygame.quit()
sys.exit()












