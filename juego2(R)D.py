import pygame
import sys
import random
from pygame.locals import *


class Zang(pygame.sprite.Sprite):
    def __init__(self, sheet):
        """Funcion que crea el objeto de protagonista y marca sus
        animaciones de comportamiento
        Args:
            sheet (class 'pygame.Surface'): Imagenes del protagonista
        """

        # Carga el constructor de la clase padre (pygame.sprite.Sprite)
        pygame.sprite.Sprite.__init__(self)

        self.zang_sheet = sheet
        self.i_zang = 0  # Indice de la posicion de cada sprite
        self.espera = 0  # Contador de espera para animaciones
        self.velocidad = 6  # Velocidad de la animacion de correr

        # Lista con las posiciones de cada sprite en la sprite sheet.
        # 0-3: Animacion de correr, 4: ascenso, 5: Punto medio de salto
        # 6: Descenso del salto, 7: Colision
        self.mueve = {0: (2, 2, 101, 81), 1: (113, 8, 99, 75),
                      2: (224, 2, 99, 81), 3: (336, 8, 96, 75),
                      4: (543, 3, 101, 85), 5: (659, 8, 96, 75),
                      6: (766, 1, 89, 95), 7: (450, 5, 84, 87)}

        self.image = self.zang_sheet.subsurface(self.mueve[self.i_zang])
        self.image.set_colorkey(self.image.get_at((0, 0)), pygame.RLEACCEL)

        self.rect = self.image.get_rect().inflate(-17, -8)

    def corre(self):
        """Actualiza la imagen del sprite para animar la accion de
        correr
        """
        self.espera += 1

        if self.espera > self.velocidad:
            self.i_zang += 1
            self.espera = 0
            if self.i_zang > 3:
                self.i_zang = 0

            self.image = self.zang_sheet.subsurface(self.mueve[self.i_zang])
            self.image.set_colorkey(self.image.get_at((0, 0)), pygame.RLEACCEL)

    def salta(self, direccion=""):
        """Actualiza la imagen del protagonista para animar la accion
        de saltar
        Args:
            direccion (String): "arriba", "abajo", ""
        """
        if direccion == "arriba":
            self.image = self.zang_sheet.subsurface(self.mueve[4])
            self.image.set_colorkey(self.image.get_at((0, 0)), pygame.RLEACCEL)

        elif direccion == "abajo":
            self.image = self.zang_sheet.subsurface(self.mueve[6])
            self.image.set_colorkey(self.image.get_at((0, 0)), pygame.RLEACCEL)

        else:
            self.image = self.zang_sheet.subsurface(self.mueve[5])
            self.image.set_colorkey(self.image.get_at((0, 0)), pygame.RLEACCEL)

    def golpe(self):
        """Muestra la animacion de golpe
        """
        self.image = self.zang_sheet.subsurface(self.mueve[7])
        self.image.set_colorkey(self.image.get_at((0, 0)), pygame.RLEACCEL)
        pygame.mixer.music.pause()


class Ratt1(pygame.sprite.Sprite):
    def __init__(self, foto1):
        """Funcion que crea el objeto de enemigo y marca sus
        animaciones de comportamiento
        Args:
            foto1 (class 'pygame.Surface'): Imagenes de enemigo
        """

        # Carga el constructor de la clase padre (pygame.sprite.Sprite)
        pygame.sprite.Sprite.__init__(self)

        self.sprite_foto1 = foto1
        self.r1_sprite = 0  # Indice de la posicion de cada sprite
        self.siguiente = 0  # Contador de espera para animaciones
        self.rapidez = 6  # Velocidad de la animacion de correr

        # Lista con las posiciones de cada sprite en la sprite foto1.
        self.r1 = {0: (2, 2, 87, 60), 1: (95, 5, 90, 57), 2: (191, 2, 72, 60)}

        self.image = self.sprite_foto1.subsurface(self.r1[self.r1_sprite])
        self.image.set_colorkey(self.image.get_at((0, 0)), pygame.RLEACCEL)

        # self.rect = self.image.get_rect()
        self.rect = self.image.get_rect().inflate(-15, -5)

    def camina1(self):
        """Actualiza la imagen del sprite para animar la accion de
        correr
        """
        self.siguiente += 1

        if self.siguiente > self.rapidez:
            self.r1_sprite += 1
            self.siguiente = 0
            if self.r1_sprite > 2:
                self.r1_sprite = 0

            self.image = self.sprite_foto1.subsurface(self.r1[self.r1_sprite])
            self.image.set_colorkey(self.image.get_at((0, 0)), pygame.RLEACCEL)


class Ratt2(pygame.sprite.Sprite):
    def __init__(self, foto2):
        """Funcion que crea el objeto de enemigo y marca sus
        animaciones de comportamiento
        Args:
            foto2 (class 'pygame.Surface'): Imagenes de enemigo
        """

        # Carga el constructor de la clase padre (pygame.sprite.Sprite)
        pygame.sprite.Sprite.__init__(self)

        self.sprite_foto2 = foto2
        self.r2_sprite = 0  # Indice de la posicion de cada sprite
        self.siguiente = 0  # Contador de espera para animaciones
        self.rapidez = 6  # Velocidad de la animacion de correr

        # Lista con las posiciones de cada sprite en la sprite foto2.
        self.r2 = {0: (2, 2, 72, 60), 1: (80, 2, 87, 60), 2: (173, 5, 90, 57)}

        self.image = self.sprite_foto2.subsurface(self.r2[self.r2_sprite])
        self.image.set_colorkey(self.image.get_at((0, 0)), pygame.RLEACCEL)

        # self.rect = self.image.get_rect()
        self.rect = self.image.get_rect().inflate(-15, -5)

    def camina2(self):
        """Actualiza la imagen del sprite para animar la accion de
        correr
        """
        self.siguiente += 1

        if self.siguiente > self.rapidez:
            self.r2_sprite += 1
            self.siguiente = 0
            if self.r2_sprite > 2:
                self.r2_sprite = 0

            self.image = self.sprite_foto2.subsurface(self.r2[self.r2_sprite])
            self.image.set_colorkey(self.image.get_at((0, 0)), pygame.RLEACCEL)


# Variables globales

# Dimenciones de la pantalla
ANCHO = 800
ALTO = 420

# Posicion del personaje
pos_x = 25
pos_y = 242

# Tiempo que permanece en el aire.
SALTO_DIST = 20
SALTO_LARGO_DIST = 50

# Posicion inicial y velocidad con la que se mueve el fondo
fondo_x = 0
tiempo = 2

pause = False
comienza = 1

# Ticks que se ignora el boton de Pausa, para impedir que se utilice
# para alentar el juego.
tiempo_pausa = 0

# Flags que determinan el estado del salto del personaje y el tiempo
# que permanece ahi.
salto = False
salto_largo = False
caida = False
salto_espera = 0

# Posicion y velocidad inicial de los enemigos
bloque_x1 = 900
bloque_x2 = -500
vel_bloque1 = 4
vel_bloque2 = 4

# Cantidad de vidas, estado de niveles y enemigos
vidas = 3
nivel_1 = True
nivel_2 = False
contador_nivel = 0
pasa_rata = 1


def intro():
    """Funcion que se muestra al principio del juego, haciendo de
    "interruptor" para iniciar el juego
    """
    global comienza

    texto_inicio = pygame.font.SysFont(None, 55)
    pantalla_inicio = texto_inicio.render("Pesione espacio para iniciar", True,
                                          pygame.Color("white"))
    centro_inicio = pantalla_inicio.get_rect(center=pantalla.get_rect().center)
    pantalla.blit(pantalla_inicio, centro_inicio)

    texto_tecla = pygame.font.SysFont(None, 38)
    pantalla_tecla = texto_tecla.render("[X] salto corto || [C] salto largo",
                                        True, pygame.Color("white"))
    pantalla.blit(pantalla_tecla, [185, 235])

    pygame.display.update()

    while comienza > 0:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    comienza = 0

    fps.tick(0.5)


def iniciar():
    """Iniciacion de modulos importados, pantalla, reloj, variables,
    musica, se ejecuta una unica vez al inicio del programa.
    """
    global pantalla, fps

    pygame.init()

    pygame.mixer.music.load('Big_Blue.mp3')
    pygame.mixer.music.play(0, 0)

    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Zangoose run")
    fps = pygame.time.Clock()

    cargar()
    return


def cargar():
    """Carga archivos que se utilizan en el juego
    """
    global fondo, zangoose, rattata1, rattata2, sprite_lista, bloque_lista

    fondo = pygame.image.load("fondo.png")

    sprite_lista = pygame.sprite.Group()

    zangoose = Zang(pygame.image.load("derecha.png").convert())
    sprite_lista.add(zangoose)

    rattata1 = Ratt1(pygame.image.load("enemigo1.png").convert())
    rattata2 = Ratt2(pygame.image.load("enemigo2.png").convert())
    sprite_lista.add(rattata1)
    sprite_lista.add(rattata2)

    bloque_lista = pygame.sprite.Group()
    bloque_lista.add(rattata1)
    bloque_lista.add(rattata2)

    return


def actualizar():
    """Metodos que se llaman cada ciclo del juego durante su ejecucion.
    Incluye eventos de teclado, actualizacion de graficos y enemigos, y
    colisiones
    """
    tecla()

    mover_zangoose()

    mover_rattata1()

    mover_rattata2()

    detectar_colision()

    sprite_lista.draw(pantalla)
    pygame.display.flip()

    # Si hay ciclos que saltar, descuenta uno por ciclo
    global tiempo_pausa
    if tiempo_pausa > 0:
        tiempo_pausa -= 1

    return


def nivel():
    """Pone fin al nivel uno mostrando una pantalla de "NIVEL 2" y
    prepara el siguiente nivel de dificultad, reubicando las
    pocisiones del personaje y de los enemigos.
    """
    global nivel_2, bloque_x1, bloque_x2
    global pos_y, pos_x, caida, salto, salto_largo, salto_espera

    texto_mas = pygame.font.SysFont(None, 90)
    pantalla_mas = texto_mas.render("NIVEL 2", True, pygame.Color("white"))
    centro_mas = pantalla_mas.get_rect(center=pantalla.get_rect().center)
    pantalla.blit(pantalla_mas, centro_mas)

    nivel_2 = True
    bloque_x1 = random.randrange(900, 1500)
    bloque_x2 = random.randrange(-1100, -500)
    salto = False
    salto_largo = False
    caida = False
    salto_espera = 0
    pos_x = 325
    pos_y = 242
    zangoose.i_sprite = 0

    pygame.display.update()
    fps.tick(1)


def final():
    """ Texto que se muestra al completar el objetivo del juego
    """
    texto_final = pygame.font.SysFont(None, 90)
    pantalla_final = texto_final.render("FIN", True, pygame.Color("white"))
    centro_final = pantalla_final.get_rect(center=pantalla.get_rect().center)

    pantalla.blit(pantalla_final, centro_final)

    pygame.mixer.music.pause()

    while True:
        pygame.display.update()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


def mover_zangoose():
    """Actualilza el numero de vidas extras del personaje, movimiento
    del fondo y del personaje junto con su accion, dependiendo de lo
    que este haciendo ("correr" o saltar)
    """
    global salto, caida, fondo_x, tiempo, salto_largo, salto_espera
    global pos_x, pos_y, vidas, v_r

    # Movimiento del fondo
    if fondo_x == -1083 or fondo_x == -1084:
        fondo_x = -84
        pantalla.blit(fondo, (fondo_x, 0))
    else:
        pantalla.blit(fondo, (fondo_x, 0))
        fondo_x = fondo_x - tiempo

    # Muestra las vidas extras del personaje (v_r).
    texto_vidas = pygame.font.SysFont(None, 30)
    if vidas == 3:
        v_r = texto_vidas.render("Vidas extra: 2", True, pygame.Color("brown"))
    if vidas == 2:
        v_r = texto_vidas.render("Vidas extra: 1", True, pygame.Color("brown"))
    if vidas == 1:
        v_r = texto_vidas.render("Vidas extra: 0", True, pygame.Color("brown"))
    pantalla.blit(v_r, [25, 25])

    zangoose.rect.x = pos_x
    zangoose.rect.y = pos_y

    # Movimiento del personaje
    if salto is False and salto_largo is False:
        zangoose.corre()

    # Salto simple
    if salto is True:

        if caida is False:
            pos_y -= 3
            if pos_y > 140:
                zangoose.salta("arriba")

        if caida is True:
            pos_y += 3
            zangoose.salta("abajo")

        if pos_y == 137:
            salto_espera += 1
            pos_y = 140
            zangoose.salta()
            if salto_espera > SALTO_DIST:
                salto_espera = 0
                pos_y = 137
                caida = True

        if pos_y == 242:
            caida = False
            salto = False
            salto_largo = False

    # Salto largo
    if salto_largo is True:

        if caida is False:
            pos_y -= 3
            if pos_y > 140:
                zangoose.salta("arriba")

        if caida is True:
            pos_y += 3
            zangoose.salta("abajo")

        if pos_y == 137:
            salto_espera += 1
            pos_y = 140
            zangoose.salta()
            if salto_espera > SALTO_LARGO_DIST:
                salto_espera = 0
                pos_y = 137
                caida = True

        if pos_y == 242:
            caida = False
            salto = False
            salto_largo = False
    return


def mover_rattata1():
    """Funcion que hace el movimiento a traves de la pantalla del
    primer enemigo
    """
    global bloque_x1, vel_bloque1
    global pasa_rata, contador_nivel, nivel_1, nivel_2

    rattata1.camina1()

    rattata1.rect.x = bloque_x1
    rattata1.rect.y = 260

    if pasa_rata == 1:
        if bloque_x1 > -400:
            bloque_x1 -= vel_bloque1
        else:
            vel_bloque1 = random.randrange(4, 7)
            bloque_x1 = random.randrange(900, 1500)

            if nivel_1 is True:
                contador_nivel += 1

                if contador_nivel == 5:
                    nivel_1 = False
                    nivel()
                    contador_nivel = 0

            if nivel_2 is True:
                contador_nivel += 1

                pasa_rata = 2
                if contador_nivel == 4:
                    nivel_2 = False
                    final()


def mover_rattata2():
    """Funcion que hace el movimiento a traves de la pantalla del
    segundo enemigo
    """
    global bloque_x2, vel_bloque2, pasa_rata

    rattata2.camina2()

    rattata2.rect.x = bloque_x2
    rattata2.rect.y = 260

    if pasa_rata == 2:

        if bloque_x2 < 1000:
            bloque_x2 += vel_bloque2
        else:
            vel_bloque2 = random.randrange(4, 8)
            bloque_x2 = random.randrange(-1000, -500)
            pasa_rata = 1


def detectar_colision():
    """Detecta si ocurre una colision entre el protagonista y algun
    enemigo
    """
    global pause, pantalla

    colision = pygame.sprite.spritecollide(zangoose, bloque_lista, False)

    if colision:
        zangoose.golpe()
        sprite_lista.draw(pantalla)
        pygame.display.flip()
        pause = True
        morido()


def tecla():
    """Lee el estado del teclado y realiza las acciones acorde a la
    tecla presionada y al estado actual del personaje.

    X = Salto
    C = Salto largo
    P = Pausa
    """
    global salto, salto_largo, pause, tiempo_pausa

    teclado = pygame.key.get_pressed()

    if teclado[K_p] and pause is False and tiempo_pausa == 0:
        pause = True
        detener()

    if pause is False:
        if teclado[K_x] and salto is False and salto_largo is False:
            salto = True

        if teclado[K_c] and salto is False and salto_largo is False:
            salto_largo = True

    else:
        pause = True

    for eventos in pygame.event.get():
        if eventos.type == pygame.QUIT:
            sys.exit()

    return


def detener():
    """Funcion que pausa el juego y cuenta con un contador para que
    no se pueda hacer pausa hasta despues de algun tiempo
    """
    global pantalla, pause, tiempo_pausa

    texto_pausa = pygame.font.SysFont(None, 115)
    pantalla_pausa = texto_pausa.render("PAUSA", True, pygame.Color("white"))
    centro_pausa = pantalla_pausa.get_rect(center=pantalla.get_rect().center)
    pygame.mixer.music.pause()

    pantalla.blit(pantalla_pausa, centro_pausa)

    while pause:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    tiempo_pausa = 80
                    pause = False
                    pygame.mixer.music.unpause()

        pygame.display.update()
        fps.tick(15)


def morido():
    """Funcion que pausa el juego y que muestra lo que ocurre cuando
    sucede una colision.
    """

    global pause, pantalla, sprite_lista, bloque_x1, bloque_x2, pos_y, vidas
    global caida, salto, salto_largo, salto_espera, contador_nivel

    vidas -= 1

    texto_fin = pygame.font.SysFont(None, 90)
    pantalla_fin = texto_fin.render("GAME OVER", True, pygame.Color("white"))
    centro_fin = pantalla_fin.get_rect(center=pantalla.get_rect().center)

    if vidas > 0:
        tex_reint = pygame.font.SysFont(None, 40)
        de_nuevo = tex_reint.render("Aprete Z", True, pygame.Color("white"))
        pantalla.blit(de_nuevo, [355, 235])
    pantalla.blit(pantalla_fin, centro_fin)
    while pause:
        pygame.display.update()

        if vidas > 0:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_z:
                        pause = False
                        bloque_x1 = random.randrange(900, 1500)
                        bloque_x2 = random.randrange(-1100, -500)
                        salto = False
                        salto_largo = False
                        caida = False
                        salto_espera = 0
                        pos_y = 242
                        zangoose.i_sprite = 0
                        if nivel_1:
                            contador_nivel = 0
                        pygame.mixer.music.unpause()

        else:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()


def main():
    """Funcion que inicia el programa
    """
    global tiempo_pausa

    iniciar()
    intro()
    while True:
        fps.tick(120)
        actualizar()
        

if __name__ == '__main__':
    main()
