import pygame
from random import randint
from time import sleep
import config
# ========================================botão===================================================================
class Botao:
    """Representa um botão.

    Atributos:
        self.img_normal -> Carrega a imagem que vai ser usada como botão
        self.img_hover -> Carrega a imagem que vai ser usada como botão quando o mouse estiver sobre ele
        self.rect -> Pega as coordenadas do retangulo ao redor da imagem
        self.pressionado -> Vê se o botão está sendo pressionado
        self.y_original -> Coordenada y inicial do botão
        self.y_alterado -> Vê se a posição y foi alterada
    """
    def __init__(self, tela:pygame.surface.Surface, x:int, y:int, imagem:pygame.surface.Surface, img_hover:pygame.surface.Surface, tamanho_x:int, tamanho_y:int, hover_y:int):
        """Construtor.

        Parâmetros:
            tela -> Onde o botão será exibido
            x -> Posição x onde o botão será colocado
            y -> Posição y onde o botão será colocado
            imagem -> Imagem a ser usada como botão
            img_hover -> Imagem a ser usada como botão quando o mouse estiver sobre ele
            tamanho_x -> Largura da imagem
            tamanho_y -> Altura da imagem
        """
        self.img_normal = pygame.transform.scale(imagem, (tamanho_x , tamanho_y))
        self.img_hover = img_hover
        self.imagem = self.img_normal
        self.rect = self.imagem.get_rect()
        self.rect.topleft = (x,y)
        self.pressionado = False
        self.tela = tela
        self.y_original = y
        self.y_alterado = False
        self.hover_y = hover_y
    
    def botao_sistema_colocar(self) -> bool:
        """Coloca a imagem do botão na tela.

        Retorna se o botão foi clicado ou não.
        """
        self.acao = False

        #pega a posição do mouse
        mouse_posi = pygame.mouse.get_pos()

        self.imagem = self.img_normal
        #ver ação do mouse
        if self.rect.collidepoint(mouse_posi):
            self.imagem = self.img_hover
            if self.y_alterado == False:
                self.rect.y -= self.hover_y
                self.y_alterado = True
            
            if pygame.mouse.get_pressed()[0] == True and self.pressionado == False and self.acao == False:
                self.acao = True
                self.pressionado = True
                self.imagem = self.img_normal

        else:
            if self.y_alterado:
                self.rect.y = self.y_original
                self.y_alterado = False

        if pygame.mouse.get_pressed()[0]==0:
            self.pressionado = False

        #posicionar imagem
        self.tela.blit(self.imagem, (self.rect.x, self.rect.y))

        return self.acao
    
# ========================================barra de vida===================================================================
class Vida_qnt:
    """Representa uma barra de vida.
    """
    def __init__(self, x_inicial:int, y_inicial:int, x_final:int, y_final:int, vida_maxima:int, vida:int, tela:pygame.surface.Surface):
        """Construtor.

        Parâmetros:
            x_inicial -> Posição x onde começa a barra de vida
            y_inicial -> Posição y onde começa a barra de vida
            x_final -> Posição x onde termina a barra de vida
            y_final - > Posição y onde termina a barra de vida
            vida_maxima -> Valor máximo de vida que o personagem pode ter
            vida -> Quantidade de kit médicos disponíveis
            tela -> Onde a barra de vida será desenhada
        """
        self.x_inicial = x_inicial
        self.y_inicial = y_inicial
        self.x_final = x_final
        self.y_final = y_final
        self.vida_maxima = vida_maxima
        self.vida = vida
        self.tela = tela

    def posi(self, hp_personagem:int):
        """Calcula a vida atual do personagem e a desenha na tela.
        
        Parâmetros:
            hp_personagem -> Define a vida total do personagem
        """
        self.vida = hp_personagem
        pygame.draw.rect(self.tela,(255,0,0),(self.x_inicial, self.y_inicial, self.x_final, self.y_final))
        pygame.draw.rect(self.tela,(0,255,0),(self.x_inicial, self.y_inicial, self.x_final*(self.vida/self.vida_maxima), self.y_final)) 


# ========================================personagem===================================================================
def parado_save(name:str) -> list:
    """Armazena em uma lista cada imagem separada (sprite) do conjunto de imagens (spritesheet) da animação do personagem parado.

    Retorna a lista de imagens.

    Parâmetros:
        name -> Indica o nome do personagem a ser usado
    """
    list_parado = []

    img = pygame.image.load(f'imagem/personagens/{name}/parado.png')
    width = pygame.Surface.get_width(img)

    for parado in range(0,width,64):

        img = pygame.image.load(f'imagem/personagens/{name}/parado.png').subsurface((parado,0),(64,64))
        list_parado.append(img)
    return list_parado

def atacando_save(name:str) -> list:
    """Armazena em uma lista cada imagem separada (sprite) do conjunto de imagens (spritesheet) da animação do personagem atacando.

    Retorna a lista de imagens.

    Parâmetros:
        name -> Indica o nome do personagem a ser usado
    """
    list_atacando = []

    img = pygame.image.load(f'imagem/personagens/{name}/atacando.png')
    width = pygame.Surface.get_width(img)

    for atacando in range(0,width,64):

        img = pygame.image.load(f'imagem/personagens/{name}/atacando.png').subsurface((atacando,0),(64,64))
        list_atacando.append(img)
    return list_atacando

def morrendo_save(name:str) -> list:
    """Armazena em uma lista cada imagem separada (sprite) do conjunto de imagens (spritesheet) da animação do personagem morrendo.

    Retorna a lista de imagens.

    Parâmetros:
        name -> Indica o nome do personagem a ser usado
    """
    list_morrendo = []

    img = pygame.image.load(f'imagem/personagens/{name}/morrendo.png')
    width = pygame.Surface.get_width(img)

    for morrendo in range(0,width,64):

        img = pygame.image.load(f'imagem/personagens/{name}/morrendo.png').subsurface((morrendo,0),(64,64))
        list_morrendo.append(img)
    return list_morrendo

def tomando_save(name:str) -> list:
    """Armazena em uma lista cada imagem separada (sprite) do conjunto de imagens (spritesheet) da animação do personagem tomando dano.

    Retorna a lista de imagens.

    Parâmetros:
        name -> Indica o nome do personagem a ser usado
    """
    list_tomando = []

    img = pygame.image.load(f'imagem/personagens/{name}/tomando.png')
    width = pygame.Surface.get_width(img)

    for tomando in range(0,width,64):

        img = pygame.image.load(f'imagem/personagens/{name}/tomando.png').subsurface((tomando,0),(64,64))
        list_tomando.append(img)
    return list_tomando

def all_sprite_save(name:str) -> list:
    """Armazena em uma lista todas as listas contendo os conjuntos de imagem das animações separadamente do estado do personagem.

    Retorna a lista de listas de imagens.

    Parâmetros:
        name -> Indica o nome do personagem a ser usado
    """
    total_sprite_save = []

    parado_temp = parado_save(name)
    atacando_temp = atacando_save(name)
    morrendo_temp = morrendo_save(name)
    tomando_temp = tomando_save(name)

    total_sprite_save = [parado_temp, atacando_temp, morrendo_temp, tomando_temp]
    return total_sprite_save

# ==================================personagem============================
class Personagem():
    """Representa um personagem.

    Atributos:
        self.vivo -> Estado do personagem, se está vivo ou morto
        self.time_att -> Taxa de atualização de frames
        self.action_animation_list -> Recebe a lista com todas as listas de conjuntos de imagem das animações do personagem
        self.atual_action -> Diz em qual animação o personagem está
        self.animation_frame -> Representa em qual imagem está no conjunto de imagens
        self.imagem -> Carrega a imagem atual do conjunto de imagens
        self.rect -> Posição x e y do quadrado ao redor da imagem
    """
    def __init__(self,x:int, y:int, nome:str, vida:int, força:int, qnt_potion:int, tela:pygame.surface.Surface):
        """Construtor.

        Parâmetros:
            x -> Posição x da imagem
            y -> Posição y da imagem
            nome -> Nome do personagem a ser armazenado as imagens de suas animações
            vida -> Vida do personagem
            força -> Quantidade de força que o personagem vai ter ao atacar
            qnt_potion -> Quantidade de kit médicos que o personagem vai ter
            tela -> Onde o personagem vai ser inserido
        """
        self.nome = nome
        self.vida_max = vida
        self.vida = self.vida_max
        self.força = força
        self.vivo = True
        self.quant_kit = qnt_potion
        self.cura_inicial = qnt_potion
        self.time_att = pygame.time.get_ticks()

        self.tela = tela

        self.action_animation_list = all_sprite_save(self.nome)
        self.atual_action = 0 #0 parado, 1 atacando, 2 morrendo, 3 tomando dano
        self.animation_frame = 0

        self.x = x
        self.y = y

        #onde a imagem vai ficar
        self.imagem = self.action_animation_list[self.atual_action][self.animation_frame]
        self.imagem = pygame.transform.scale(self.imagem,(256,256))
        self.rect = self.imagem.get_rect()
        self.rect = ((self.x,self.y))

    def damage_self(self):
        """Define a animação do personagem tomando dano.
        """
        self.atual_action = 3
        self.animation_frame = 0
        self.time_att = pygame.time.get_ticks()

    def morto(self):
        """Define a animação do personagem morrendo e declara que ele está morto.
        """
        self.atual_action = 2
        self.animation_frame = 0
        self.time_att = pygame.time.get_ticks()
        self.vivo = False

    def parado_animation(self):
        """Define a animação do personagem parado.
        """
        self.atual_action = 0
        self.animation_frame = 0
        self.time_att = pygame.time.get_ticks()

    def atacar(self, alvo:object):
        """Define a animação do personagem atacando e sorteia a força do ataque do personagem.
        """
        self.atual_action = 1
        self.animation_frame = 0
        dano_sorte = randint(0,30)
        dano = self.força + dano_sorte
        alvo.vida -= dano
        alvo.damage_self()
        if alvo.vida <= 0:
            alvo.vivo = False
            alvo.morto()

    def update(self):
        """Atualiza o frame atual da animação do personagem.
        """
        tempo_animacao = 100

        self.imagem = self.action_animation_list[self.atual_action][self.animation_frame]
        self.imagem = pygame.transform.scale(self.imagem,(128,128))

        if pygame.time.get_ticks() - self.time_att > tempo_animacao:
            self.time_att=pygame.time.get_ticks()
            self.animation_frame += 1

        if self.animation_frame>= len(self.action_animation_list[self.atual_action]):
            #deixar so na fase inicial pois so vai ter um personagem, isso prende a animação do personagem para ele ficar morto
            if self.atual_action == 2:
                self.animation_frame = len(self.action_animation_list[self.atual_action])-1
            else:
                self.parado_animation()
                
    def colocar(self, fliper:bool):
        """Insere o personagem na tela do jogo.

        Parâmetros:
            fliper -> Define se o personagem está virado pra esquerda ou direita.
        """
        if fliper == True:
            self.imagem = pygame.transform.flip(self.imagem,True,False)
            self.tela.blit(self.imagem,self.rect)
        else:
            self.tela.blit(self.imagem,self.rect)

    def reset(self):
        """Reseta as informações dos personagens ao reiniciar uma rodada.
        """
        self.vivo = True
        self.quant_kit = self.cura_inicial
        self.vida = self.vida_max
        self.animation_frame = 0
        self.atual_action = 0
        self.time_att = pygame.time.get_ticks()


# ========================================checkpoint===================================================================
class Checkpoint():
    ''' Representa o salvamento das fases que o jogador parou.

    Atributos:
        self.round_complet -> Representa quais rounds foram completos
    '''
    def __init__(self):
        '''Construtor.
        '''
        self.round_complet = 0

    def check_round(self) -> int :
        ''' Checa qual round o jogador parou no arquivo checkpoint.

        Retorna o número inteiro em relação a fase que o jogador parou.
        '''
        arquivo = open('checkpoint.txt', 'a', encoding='utf-8')
        arquivo.close()
        arquivo = open('checkpoint.txt', 'r', encoding='utf-8')
        arquivo_conteudo = arquivo.read()
        if arquivo_conteudo != '':
            return int(arquivo_conteudo)
        else:
            return  0
    
    def carregar_save(self, check_round:int, map_true:object, batalha:object):
        '''Carrega o local que o jogador parou em ralação a checagem.

        Parâmetros:
            check_round -> O round que o jogador parou
            map_true -> Representa o mapa do jogo
            batalha -> Simboliza a batalha do jogo
        '''
        if check_round == int(1):
            map_true.round_complet = 1
            map_true.round1_win = True
            map_true.vitoria1 = True
        elif check_round == int(2):
            map_true.round_complet = 2
            map_true.round2_win = True
            map_true.vitoria1 = True
            map_true.vitoria2 = True
        elif check_round == int(3):
            # batalha.congratulation = True
            map_true.round_complet = 3
            map_true.round3_win = True
            map_true.vitoria1 = True
            map_true.vitoria2 = True
            map_true.vitoria3 = True

        
    def aumento_check(self, round_complet):
        ''' Salva no arquivo o ultimo round completado.

        Parâmetros:
            round_complet -> O round completado
        '''
        arquivo = open('checkpoint.txt', 'w', encoding='utf-8')
        arquivo.write(f"{round_complet}")
        

# ==========================================batalha====================================================================
class Battle:
    """Define as ações da batalha.

    Atributos:
        self.round_atual -> Define de quem é o round para realizar uma ação
        self.contagem_acao -> Um tempo para realizar uma ação e o jogo não ficar extremamente rapido
        self.derrota -> Define se algum dos personagens está incapacitado
        self.inimigo_list -> define a lista de inimigos
        self.congratulation -> define se a tela de parabenização está aberta
        self.menu -> define se o menu esta aberto
    """
    def __init__(self, peixe:object, inimigo:int):
        '''Construtor.

        Parâmetros:
            peixe -> Qual personagem jogável está em campo
            inimigo -> Indica qual índice da lista que o inimigo está
        '''
        self.round_atual = 1
        self.contagem_acao = 0
        self.derrota = 0
        self.personagem_atual = peixe
        self.inimigo = inimigo
        self.inimigo_list = []
        self.congratulation = False
        self.menu=True
        self.in_battle = False
        self.creditos = False
        

# ========================================mapa===================================================================
class Mapa:
    """Representa o mapa inicial do jogo.

    Atributos:
        self.x -> Posição x do peixe no mapa
        self.y -> Posição y do peixe no mapa
        self.andando1 -> Estado do peixe, se ele está movimentando ou não, referente ao botão da fase 1
        self.andando2 -> Estado do peixe, se ele está movimentando ou não, referente ao botão da fase 2
        self.andando3 -> Estado do peixe, se ele está movimentando ou não, referente ao botão da fase 3
        self.round1_win -> Representa se o jogador ganhou o round 1, para poder definir o x e y do personagem no mapa
        self.round2_win -> Representa se o jogador ganhou o round 2, para poder definir o x e y do personagem no mapa
        self.vitoria1 -> Guarda a informação se o jogador ganhou o round 1 ou não
        self.vitoria2 -> Guarda a informação se o jogador ganhou o round 2 ou não
        self.round2_concluido -> Guarda a informação se o jogador já ganhou o round 2,
        para poder posicionar o personagem no mapa após ganhar o round 2
        self.round3_concluido -> Guarda a informação se o jogador já ganhou o round 3.
        para poder posicionar o congratulations.
    """
    def __init__(self, tela:pygame.surface.Surface):
        """Construtor.

        Parâmetros:
            tela -> Onde as imagens serão colocadas
        """
        self.x = 70
        self.y = 445 - 64
        self.andando1 = False
        self.andando2 = False
        self.andando3 = False
        self.tela = tela
        self.round1_win = False
        self.round2_win = False
        self.round3_win = False
        self.vitoria1 = False
        self.vitoria2 = False
        self.vitoria3 = False
        self.round2_concluido = False
        self.round3_concluido = False


    def mapa_colocar(self) -> tuple[object, object, object]:
        """Insere na tela a imagem do background.

        Retorna a informação de onde estarão os botões das fases.
        """
        pygame.display.update()
        bg = pygame.image.load("imagem/background/bg_mapa.png")
        img = pygame.image.load("imagem/botoes/botao_fase.png")
        img_hover = pygame.image.load("imagem/botoes/botao_fase_hover.png")
        self.tela.blit(bg,(0,0))
        fase_1 = Botao(self.tela, 420, 445, img, img_hover, 46, 32, 0)
        fase_2 = Botao(self.tela, 420, 160, img, img_hover, 46, 32, 0)
        fase_3 = Botao(self.tela, 785, 160, img, img_hover, 46, 32, 0)

        return fase_1, fase_2, fase_3

    def colocar_peixe_mapa(self, x:int, y:int):
        """Coloca a imagem do peixe na tela.

        Parâmetros:
            x -> Posição x em que a imagem será inserida
            y -> Posição y em que a imagem será inserida
        """
        img = pygame.image.load(f'imagem/personagens/peixe/peixe_aquario.png')
        img = pygame.transform.scale(img,(128,128))
        x_real = x
        y_real = y
        self.tela.blit(img,(x_real, y_real))

    def colocar_fases(self):
        """Insere na tela os botões das fases com a checagem de clique.
        """
        fases = self.mapa_colocar()        
        if fases[0].botao_sistema_colocar():
            self.andando1 = True
        if fases[1].botao_sistema_colocar():
            self.andando2 = True
        if fases[2].botao_sistema_colocar():
            self.andando3 = True

    def colocar_fases_star(self):
        """Coloca um icone para cada fase e adiciona uma estrela quando aquela fase é concluída.
        """
        fase1 = pygame.image.load("imagem/icones/fase1.png")
        fase2 = pygame.image.load("imagem/icones/fase2.png")
        fase3 = pygame.image.load("imagem/icones/fase3.png")
        star = pygame.image.load("imagem/icones/star.png")
        self.tela.blit(fase1, (400,500))
        self.tela.blit(fase2, (400,50))
        self.tela.blit(fase3, (760,225))
        if self.vitoria1:
            self.tela.blit(star, (400,500))
        if self.vitoria2:
            self.tela.blit(star, (400,50))
        if self.vitoria3:
            self.tela.blit(star, (760,225))

    def win_check(self):
        """Checa se o personagem já ganhou os rounds.
        """
        if self.round1_win == True:
            self.x = 386
            self.y = 445 - 64
            self.vitoria1 = True
            self.round1_win = False
        elif self.round2_win == True:
            self.x = 385
            self.y = 91
            self.vitoria2 = True
            self.round2_win = False
        elif self.round3_win == True:
            self.x = 751
            self.y = 89
            self.vitoria3 = True
            self.round3_win = False

    def rodar_mapa(self):
        """Realiza a movimentação do peixe pela tela.
        """
        self.colocar_fases()
        self.colocar_fases_star()
        self.win_check()
        if self.andando1 == True and self.vitoria1 == False:
            self.x += 5
            if self.x == 385:
                sleep(1)
                self.andando1 = False
        elif self.andando2 == True:
            if self.vitoria1 == True and self.vitoria2 == False:
                self.y -= 5
                if self.y == 91:
                    sleep(1)
                    self.andando2 == False
        elif self.andando3 == True and self.vitoria1 == True and self.vitoria2 == True and self.vitoria3 == False:
            self.x += 5
            if self.x == 750:
                sleep(1)
                self.andando3 = False
        self.colocar_peixe_mapa(self.x, self.y)

    def retornar_rodada(self) -> tuple[bool, bool, bool]:
        """Checa em qual posição o peixe está.

        Retorna uma tupla com a informação se ele está na posição destinada para a fase 1, 2 ou 3.
        """
        self.rodada1 = False
        self.rodada2 = False
        self.rodada3 = False
        if self.x == 385 and self.y == 445 - 64:
            self.rodada1 = True
        elif self.x == 386 and self.y == 91:
            self.rodada2 = True
        elif self.x == 750 and self.y == 91:
            self.rodada3 = True
        return self.rodada1, self.rodada2, self.rodada3
    
class Creditos:
    '''Representa o mapa inicial do jogo.

    Atributos:
        self.eixo_y -> onde vai ser colocado no eixo y
        self.tela -> onde os creditos vai ser desenhado
        self.batalha -> classe onde fica as variaveis do game
        self.seta -> botão de voltar para o menu
    '''
    def __init__(self, Tela:pygame.surface.Surface, batalha:object) -> None:
        """Construtor.

        Parâmetros:
            tela -> Onde as imagens serão colocadas
            batalha -> classe batalha onde está as variaveis do jogo
        """
        self.eixo_y = 0
        self.tela = Tela
        self.batalha = batalha
        self.seta = Botao(self.tela, 0,0 ,config.SETA_BOTAO,config.SETA_BOTAO_HOVER,66,50, 5)

    def creditos_colocar(self):
        '''Desenha os creditos na tela junto com o botão de retornar ao menu
        '''
        self.tela.blit(config.CREDITOS, (0,self.eixo_y))
        if self.seta.botao_sistema_colocar() == True:
            pygame.mixer.music.load('musica/sumeru.mp3')
            pygame.mixer.music.play(-1)
            self.batalha.creditos = False
            pygame.Surface.fill(self.tela, (0,0,0))
        if self.eixo_y >= -config.CREDITOS.get_height():
            self.eixo_y -= 1
        else:
            pygame.mixer.music.load('musica/sumeru.mp3')
            pygame.mixer.music.play(-1)
            self.batalha.menu = True
            self.batalha.creditos = False
            pygame.Surface.fill(self.tela, (0,0,0))


