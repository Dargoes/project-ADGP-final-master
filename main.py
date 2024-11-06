import pygame 
import config
# função para fechar o progama
from sys import exit
from classe import *


# inicia funções e variaveis do py game
pygame.init()

fps = pygame.time.Clock()
#troca o nome da janela
TELA = pygame.display.set_mode((config.LARGURA, config.ALTURA))
pygame.display.set_caption("Operation Capybara: Fish Tales")

check = Checkpoint()

def backg_colocar(img:pygame.surface.Surface):
    """Coloca a imagem do background na tela do jogo.

    Parâmetros:
    img -> Imagem a ser usada como background
    """
    TELA.blit(img,(0,0))

def button_local():
    """Coloca a imagem dos botões do jogo.
    """
    TELA.blit(config.BOTAO_POSI,(0,config.ALTURA-200))

def painel_colocar():
    """Coloca a imagem do painel onde os botões estão localizados.
    """
    TELA.blit(config.PAINEL_ITEN_LOCATION, (0,0))


peixe = Personagem(200,300,'peixe',360,200,3,TELA)

porco = Personagem(200,300,'porco',360,190,2,TELA)

aguia = Personagem(200,300,'aguia',360,150,3,TELA)

capivara = Personagem(200,300,'capivara',360,200,3,TELA)


rato = Personagem(600,300,'rato',1400,105,3,TELA)
jacare = Personagem(600,300,'jacare',1400,155,3,TELA)

batalha = Battle(peixe, 0)

creditos_class = Creditos(TELA, batalha)



def mudar_cura() -> object:
    """Checa a quantidade total e atual de curas de cada personagem
       e define um botão com imagem diferente para cada situação.

       Retorna os botões de cura de cada personagem.
    """
    if batalha.personagem_atual.cura_inicial == 3:
        if batalha.personagem_atual.quant_kit == 3:
            cura_botao = Botao(TELA,17,456,config.CURA_IMAGE_3_3, config.CURA_IMAGE_3_3_HOVER, 230,170, 5)
        elif batalha.personagem_atual.quant_kit == 2:
            cura_botao = Botao(TELA,17,456,config.CURA_IMAGE_3_2, config.CURA_IMAGE_3_2_HOVER, 230,170, 5)
        elif batalha.personagem_atual.quant_kit == 1:
            cura_botao = Botao(TELA,17,456,config.CURA_IMAGE_3_1, config.CURA_IMAGE_3_1_HOVER, 230,170, 5)
        elif batalha.personagem_atual.quant_kit == 0:
            cura_botao = Botao(TELA,17,456,config.CURA_IMAGE_3_0, config.CURA_IMAGE_3_0_HOVER, 230,170, 5)
    elif batalha.personagem_atual.cura_inicial == 2:
        if batalha.personagem_atual.quant_kit == 2:
            cura_botao = Botao(TELA,17,456,config.CURA_IMAGE_2_2, config.CURA_IMAGE_2_2_HOVER, 230,170, 5)
        elif batalha.personagem_atual.quant_kit == 1:
            cura_botao = Botao(TELA,17,456,config.CURA_IMAGE_2_1, config.CURA_IMAGE_2_1_HOVER, 230,170, 5)
        elif batalha.personagem_atual.quant_kit == 0:
            cura_botao = Botao(TELA,17,456,config.CURA_IMAGE_2_0, config.CURA_IMAGE_2_0_HOVER, 230,170, 5)
    return cura_botao


ataque_botao = Botao(TELA,247,456,config.ESPADA, config.ESPADA_HOVER, 230,170, 5)
restart = Botao(TELA,(config.LARGURA/2-115),(config.ALTURA/2-60),config.RESTART, config.RESTART_HOVER, 230,85, 5)

next1 = Botao(TELA,(config.LARGURA/2-115),(config.ALTURA/2-60),config.NEXT,config.NEXT_HOVER,230,85, 5)
next2 = Botao(TELA,(config.LARGURA/2-115),(config.ALTURA/2-60),config.NEXT,config.NEXT_HOVER,230,85, 5)
next3 = Botao(TELA,(config.LARGURA/2-115),(config.ALTURA/2-60),config.NEXT,config.NEXT_HOVER,230,85, 5)

peixe_botao = Botao(TELA,485,456,config.PEIXE,config.PEIXE_HOVER,230,85, 5)
porco_botao = Botao(TELA,715,456,config.PORCO,config.PORCO_HOVER,230,85, 5)
aguia_botao = Botao(TELA,485,541,config.AGUIA,config.AGUIA_HOVER,230,85, 5)
capivara_botao = Botao(TELA,715,541,config.CAPIVARA,config.CAPIVARA_HOVER,230,85, 5)

reiniciar = Botao(TELA, 365,400 ,config.REINICIAR,config.REINICIAR_HOVER,230,85, 5)
creditos_botao = Botao(TELA, 365,220 ,config.CREDITOS_BOTAO,config.CREDITOS_BOTAO_HOVER,230,85, 5)

play = Botao(TELA, 365,320 ,config.PLAY,config.PLAY_HOVER,230,85, 5)

seta = Botao(TELA, 0,0 ,config.SETA_BOTAO,config.SETA_BOTAO_HOVER,66,50, 5)
 
# Ver as dimensões das imagem dps para funcionar
# peixe_icon=pygame.image.load('imagem/personagens/peixe/peixe_icon.png')
# peixe_icon=pygame.transform.scale(peixe_icon,(100,100))

rato_barra = Vida_qnt(rato.x+2, rato.y-10, 150, 10 , rato.vida_max, rato.vida,TELA)

person_vida = Vida_qnt(86, 27,303,30,batalha.personagem_atual.vida_max, batalha.personagem_atual.vida,TELA)

objeto_mapa = Mapa(TELA)


def all_button_att():
    """Atualiza as imagens dos botões da batalha.
    """
    peixe_botao.botao_sistema_colocar()
    porco_botao.botao_sistema_colocar()
    aguia_botao.botao_sistema_colocar()
    capivara_botao.botao_sistema_colocar()
    cura_botao = mudar_cura()
    cura_botao.botao_sistema_colocar()
    ataque_botao.botao_sistema_colocar()

def check_action() -> tuple[bool, bool]:
    """Checa se o personagem fez alguma ação.

    Retorna uma tupla contendo o valor se ele fez a ação de ataque ou de cura.
    """
    ataque_action = False
    cura_action = False

    batalha.personagem_atual.update()
    batalha.personagem_atual.colocar(False)
    person_vida.posi(batalha.personagem_atual.vida)
    cura_botao = mudar_cura()
    if cura_botao.botao_sistema_colocar():
        all_button_att()
        cura_action = True

    elif ataque_botao.botao_sistema_colocar():
        all_button_att()
        ataque_action = True
    
    return ataque_action, cura_action

def troca_personagem():
    '''Realiza a troca de personagens do jogo.
    '''
    if peixe_botao.botao_sistema_colocar() and batalha.derrota==0 and batalha.round_atual==1:
        all_button_att()
        batalha.personagem_atual = peixe
        person_vida.vida_maxima=batalha.personagem_atual.vida_max
        person_vida.vida=batalha.personagem_atual.vida
        
    elif porco_botao.botao_sistema_colocar() and batalha.derrota==0 and batalha.round_atual==1:
        all_button_att()
        batalha.personagem_atual = porco
        person_vida.vida_maxima=batalha.personagem_atual.vida_max
        person_vida.vida=batalha.personagem_atual.vida

    elif aguia_botao.botao_sistema_colocar() and batalha.derrota==0 and batalha.round_atual==1:
        all_button_att()
        batalha.personagem_atual = aguia
        person_vida.vida_maxima=batalha.personagem_atual.vida_max
        person_vida.vida=batalha.personagem_atual.vida

    elif capivara_botao.botao_sistema_colocar() and batalha.derrota==0 and batalha.round_atual==1:
        all_button_att()
        batalha.personagem_atual = capivara
        person_vida.vida_maxima=batalha.personagem_atual.vida_max
        person_vida.vida=batalha.personagem_atual.vida

def personagem_action(inimigo:object):
    """Define o personagem do jogo e realiza as ações dele.

    Parâmetros:
        inimigo -> Qual inimigo o personagem vai atacar
    """
    ataque_action, cura_action = check_action()

    if batalha.derrota == 0:
        if batalha.personagem_atual.vivo == True and batalha.round_atual == 1:
            batalha.contagem_acao += 1
            if batalha.contagem_acao >= config.TEMP_ESPERA_1:
                if ataque_action == True:
                    batalha.personagem_atual.atacar(inimigo)
                    batalha.round_atual += 1
                    batalha.contagem_acao = 0
                    
                if cura_action == True and batalha.personagem_atual.quant_kit > 0:
                    if batalha.personagem_atual.vida_max - batalha.personagem_atual.vida > config.POCAO_CURA:
                        cura = config.POCAO_CURA

                    else:
                        cura = batalha.personagem_atual.vida_max - batalha.personagem_atual.vida
                    batalha.personagem_atual.vida += cura
                    batalha.personagem_atual.quant_kit -= 1
                    batalha.round_atual += 1
                    batalha.contagem_acao = 0

        elif peixe.vivo != True and capivara.vivo != True and porco.vivo != True and aguia.vivo != True:
            batalha.derrota = -1

def bot_atual(inimigos:list[object, object]) -> object:
    """Define as ações dos bots.

    Retorna o inimigo que está em campo.

    Parâmetros:
        inimigos -> lista dos inimigos que serão enfrentados
    """
    batalha.inimigo_list = inimigos

    inimigos_quant= len(inimigos)
    
    if inimigos[batalha.inimigo].vivo == True:
        pass
    elif inimigos_quant-1 == batalha.inimigo:
        pass
    else:
        batalha.inimigo += 1
    return inimigos[batalha.inimigo]
    
def bot_action(bot:object):
    """Define as ações do bot do jogo e realiza as ações dele.

    Parâmetros:
        bot -> Qual personagem terá as ações realizadas
    """
    bot.update()
    bot.colocar(False)
    rato_barra.posi(bot.vida)

    if batalha.round_atual == 2:
            if bot.vivo == True:
                batalha.contagem_acao += 1
                if batalha.contagem_acao >= config.TEMP_ESPERA_2:
                    if (bot.vida / bot.vida_max) < 0.60 and bot.quant_kit > 0:

                        if bot.vida_max - bot.vida > config.POCAO_CURA:
                            cura = config.POCAO_CURA_BOT
                        else:
                            cura = bot.vida_max - bot.vida
                        bot.vida += cura
                        bot.quant_kit -= 1

                        batalha.round_atual = 1
                        batalha.contagem_acao = 0
                    else:
                        bot.atacar(batalha.personagem_atual)
                        batalha.round_atual = 1
                        batalha.contagem_acao = 0
            else:
                batalha.derrota=1

def reset_all():
    '''Reseta todos os personagens ao seu estado original.
    '''
    peixe.reset()
    capivara.reset()
    porco.reset()
    aguia.reset()
    rato.reset()
    jacare.reset()

def button_reset():
    """Reseta o estado dos botões do mapa para não clicados.
    """
    objeto_mapa.andando1 = False
    objeto_mapa.andando2 = False
    objeto_mapa.andando3 = False

def reset_all_parametro():
    """Reseta os bots e as ações da batalha.
    """
    reset_all()
    batalha.round_atual = 1
    batalha.contagem_acao = 0
    batalha.derrota = 0
    batalha.inimigo = 0

def reset_game():
    """Reseta os bots, as ações da batalha, o estado dos botões do mapa para não clicados e roda o mapa.
    """
    reset_all_parametro()
    button_reset()
    objeto_mapa.rodar_mapa()
    batalha.in_battle = False

def reset_map():
    """Reseta os atributos do mapa que guardam informações de posição e vitória ou derrota.
    """
    objeto_mapa.x = 70
    objeto_mapa.y = 445 - 64
    objeto_mapa.round1_win = False
    objeto_mapa.round2_win = False
    objeto_mapa.round3_win = False
    objeto_mapa.vitoria1 = False
    objeto_mapa.vitoria2 = False
    objeto_mapa.vitoria3 = False
    objeto_mapa.round2_concluido = False
    objeto_mapa.round3_concluido = False
    objeto_mapa.round2_concluido = False


def resultado_round():
    """Checa se o personagem ganhou ou perdeu para o bot e exibe uma tela de vitória ou derrota.
    """
    if batalha.derrota != 0:
        if batalha.derrota == 1:
            TELA.blit(config.VICTORY, (config.LARGURA/2-128, 60))
            if objeto_mapa.vitoria1 == False:
                if next1.botao_sistema_colocar():
                    objeto_mapa.round1_win = True
                    check.round_complet = 1
                    reset_game()

            if objeto_mapa.vitoria1 == True and objeto_mapa.vitoria2 == False:
                if objeto_mapa.round2_concluido:
                    if next2.botao_sistema_colocar():
                        objeto_mapa.round2_win = True
                        check.round_complet = 2
                        reset_game()

            if objeto_mapa.vitoria2 == True and objeto_mapa.vitoria1 == True:
                if objeto_mapa.round3_concluido:
                    if next3.botao_sistema_colocar():
                        objeto_mapa.round3_win = True
                        check.round_complet = 3
                        reset_game()

        if batalha.derrota == -1:
            TELA.blit(config.GAME_OVER, (config.LARGURA/2-128, 60))
            if restart.botao_sistema_colocar():
                reset_all_parametro()

def congratulations(TELA:pygame.surface.Surface):
    '''Exibe a imagem de parabenizações e reseta o jogo todo.

    Parâmetros:
        TELA -> Onde a imagem vai ser exibida
    '''
    TELA.blit(config.CONGRATULATIONS,(0,0))
    if creditos_botao.botao_sistema_colocar():
        button_reset()
        reset_map()
        batalha.congratulation = False
        check.round_complet = 0 
        check.aumento_check(check.round_complet)
        batalha.menu = True
        reset_all_parametro()
        batalha.personagem_atual = peixe
        batalha.creditos = True
        pygame.Surface.fill(TELA, (0,0,0))
        
def menu_colocar():
    """Coloca o menu inicial na tela e checa se o jogo vai começar após clicar no botão.
    """
    pygame.Surface.fill(TELA, (0,0,0))
    TELA.blit(config.MENU,(230,0))
    if play.botao_sistema_colocar():
        pygame.mixer.music.load('musica/batalha.mp3')
        pygame.mixer.music.play(-1)
        batalha.menu=False



def congratulations_botao():
    '''Desenha o botao para levar a tela de parabenização
    '''
    if reiniciar.botao_sistema_colocar() and batalha.congratulation==False:
        batalha.congratulation = True
        pygame.mixer.music.load('musica/hyrule.mp3')
        pygame.mixer.music.play(-1)
    
def round1():
    """Executa as funções de colocar na tela o background, o painel, os botões, os personagens e o resultado do round 1.
    """
    batalha.in_battle = True
    backg_colocar(config.BACKGROUND1)

    painel_colocar()

    button_local()

    troca_personagem()
    bot_atual([rato])
    personagem_action(batalha.inimigo_list[batalha.inimigo])
    bot_atual([rato])
    bot_action(batalha.inimigo_list[batalha.inimigo])
    resultado_round()
    check.aumento_check(check.round_complet)

def round2():
    """Executa as funções de colocar na tela o background, o painel, os botões, os personagens e o resultado do round 2.
    """
    batalha.in_battle = True

    backg_colocar(config.BACKGROUND2)

    painel_colocar()

    button_local()

    troca_personagem()

    bot_atual([jacare])
    personagem_action(batalha.inimigo_list[batalha.inimigo])
    bot_atual([jacare])
    bot_action(batalha.inimigo_list[batalha.inimigo])
    resultado_round()
    check.aumento_check(check.round_complet)

def round3():
    """Executa as funções de colocar na tela o background, o painel, os botões, os personagens e o resultado do round 3.
    """
    batalha.in_battle = True
 
    backg_colocar(config.BACKGROUND3)

    painel_colocar()

    button_local()

    troca_personagem()

    bot_atual([rato, jacare])
    personagem_action(batalha.inimigo_list[batalha.inimigo])
    bot_atual([rato, jacare])
    bot_action(batalha.inimigo_list[batalha.inimigo])
    resultado_round()
    check.aumento_check(check.round_complet)



def abrir_jogo():
    """Checa qual cena deve ser exibida na tela e as exibe.
    """
    if objeto_mapa.retornar_rodada()[0] == True and batalha.congratulation == False and batalha.menu == False and batalha.creditos == False:
        round1()

    elif objeto_mapa.retornar_rodada()[1] == True and batalha.congratulation == False and batalha.menu == False and batalha.creditos == False:
        round2()
        objeto_mapa.round2_concluido = True

    elif objeto_mapa.retornar_rodada()[2] == True and batalha.congratulation == False and batalha.menu == False and batalha.creditos == False:
        round3()
        objeto_mapa.round3_concluido = True
        
    elif batalha.congratulation == True and batalha.menu == False and batalha.creditos == False:
        congratulations(TELA)

    elif batalha.creditos == True:
        creditos_class.creditos_colocar()

    elif batalha.menu == True and batalha.creditos == False:
        menu_colocar()

    else:
        objeto_mapa.rodar_mapa()
    
    if objeto_mapa.vitoria3 == True and objeto_mapa.vitoria2 == True and objeto_mapa.vitoria1 == True and batalha.menu == False and batalha.congratulation == False:
        congratulations_botao()


def fechar_jogo():
    """Checa se o botão de fechar a janela do jogo foi clicada e se for, fecha o jogo.
    """
        #identificador de ações 
    for event in pygame.event.get():
        #fechar pygame
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

check.carregar_save(check.check_round(), objeto_mapa, batalha)

pygame.mixer.music.load('musica/sumeru.mp3')
pygame.mixer.music.play()
if  __name__ == '__main__':


    while True:
        fps.tick(30)
        abrir_jogo()
        fechar_jogo()


        #atualiza a tela
        pygame.display.flip()