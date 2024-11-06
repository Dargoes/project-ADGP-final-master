import pygame
pygame.init()

LARGURA = 960
ALTURA = 640

TELA = pygame.display.set_mode((LARGURA, ALTURA))



QUANT_LUTADORES = 2
TEMP_ESPERA_1 = 5
TEMP_ESPERA_2 = 20
POCAO_CURA = 400
POCAO_CURA_BOT = 200


BACKGROUND1 = pygame.image.load('imagem/background/bg_round1.png').convert_alpha()

BACKGROUND2 = pygame.image.load('imagem/background/bg_round2.png').convert_alpha()

BACKGROUND3 = pygame.image.load('imagem/background/bg_round3.png').convert_alpha()

PAINEL_ITEN_LOCATION = pygame.image.load('imagem/icones/life_bar_icon.png')

AGUIA = pygame.image.load('imagem/botoes/aguia.png')
AGUIA_HOVER = pygame.image.load('imagem/botoes/aguia_hover.png')

CAPIVARA = pygame.image.load('imagem/botoes/capivara.png')
CAPIVARA_HOVER = pygame.image.load('imagem/botoes/capivara_hover.png')

PORCO = pygame.image.load('imagem/botoes/porco.png')
PORCO_HOVER = pygame.image.load('imagem/botoes/porco_hover.png')

PEIXE = pygame.image.load('imagem/botoes/peixe.png')
PEIXE_HOVER = pygame.image.load('imagem/botoes/peixe_hover.png')

CURA_IMAGE_3_3 = pygame.image.load('imagem/botoes/cura3_3.png')
CURA_IMAGE_3_3_HOVER = pygame.image.load('imagem/botoes/cura3_3_hover.png')
CURA_IMAGE_3_2 = pygame.image.load('imagem/botoes/cura3_2.png')
CURA_IMAGE_3_2_HOVER = pygame.image.load('imagem/botoes/cura3_2_hover.png')
CURA_IMAGE_3_1 = pygame.image.load('imagem/botoes/cura3_1.png')
CURA_IMAGE_3_1_HOVER = pygame.image.load('imagem/botoes/cura3_1_hover.png')
CURA_IMAGE_3_0 = pygame.image.load('imagem/botoes/cura3_0.png')
CURA_IMAGE_3_0_HOVER = pygame.image.load('imagem/botoes/cura3_0_hover.png')

CURA_IMAGE_2_2 = pygame.image.load('imagem/botoes/cura2_2.png')
CURA_IMAGE_2_2_HOVER = pygame.image.load('imagem/botoes/cura2_2_hover.png')
CURA_IMAGE_2_1 = pygame.image.load('imagem/botoes/cura2_1.png')
CURA_IMAGE_2_1_HOVER = pygame.image.load('imagem/botoes/cura2_1_hover.png')
CURA_IMAGE_2_0 = pygame.image.load('imagem/botoes/cura2_0.png')
CURA_IMAGE_2_0_HOVER = pygame.image.load('imagem/botoes/cura2_0_hover.png')

ESPADA = pygame.image.load('imagem/botoes/ataque.png')
ESPADA_HOVER = pygame.image.load('imagem/botoes/ataque_hover.png')

BOTAO_POSI = pygame.image.load('imagem/icones/painel.png')
BOTAO_POSI = pygame.transform.scale(BOTAO_POSI, (960,200))

GAME_OVER = pygame.image.load('imagem/icones/game_over.png')

VICTORY = pygame.image.load('imagem/icones/victory.png')

RESTART = pygame.image.load('imagem/botoes/restart.png')
RESTART_HOVER = pygame.image.load('imagem/botoes/restart_hover.png')

NEXT = pygame.image.load('imagem/botoes/next.png')
NEXT_HOVER = pygame.image.load('imagem/botoes/next_hover.png')

CONGRATULATIONS = pygame.image.load('imagem/background/congratulation.png').convert_alpha()
CONGRATULATIONS = pygame.transform.scale(CONGRATULATIONS, (LARGURA,ALTURA))

REINICIAR = pygame.image.load('imagem/botoes/reiniciar.png')
REINICIAR_HOVER = pygame.image.load('imagem/botoes/reiniciar_hover.png')

PLAY = pygame.image.load('imagem/botoes/play.png')
PLAY_HOVER = pygame.image.load('imagem/botoes/play_hover.png')

MENU = pygame.image.load('imagem/background/menu.png').convert_alpha()

CREDITOS_BOTAO = pygame.image.load('imagem/botoes/creditos.png')
CREDITOS_BOTAO_HOVER = pygame.image.load('imagem/botoes/creditos_hover.png')

SETA_BOTAO = pygame.image.load('imagem/botoes/seta.png')
SETA_BOTAO_HOVER = pygame.image.load('imagem/botoes/seta_hover.png')

CREDITOS = pygame.image.load('imagem/background/Credits.png')
