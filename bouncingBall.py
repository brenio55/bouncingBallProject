import pygame
clock = pygame.time.Clock()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

try:
	pygame.init()
except:
	print("O módulo pygame não foi inicializado com sucesso.")

#classes
width = 640
height = 480
screen = pygame.display.set_mode((width, height))

class Tela:	
	def blit(self, surface, location):
		screen.blit(surface, location)

	def iniciarTela(self):		
		pygame.display.set_caption("Bouncing Ball")

	def pintarFundo(self):
		screen.fill(blue)

	def atualizarTela(self):
		pygame.display.flip()

# class Bola:
# 	tela = Tela()

class Tabua:
	tela = Tela()
	tamanhoW = 70
	tamanhoH = 10

	pos_x = width / 2 - (tamanhoW / 2)
	pos_y = height / 2 + (height / 4)

	def move(self, movement):
		if movement == 'L':
			pos_y = height / 2 + (height / 4)
			self.pos_x += -velocidadeX
			# print('VelX L = ', velocidadeX)
			# print('pos_x = ', self.pos_x)

		if movement == 'R':
			pos_y = height / 2 + (height / 4)
			self.pos_x += velocidadeX
			# print('VelX R = ', velocidadeX)
			# print('pos_x = ', self.pos_x)

		if movement == 0:
			pos_y = height / 2 + (height / 4)
			self.pos_x = 0

	def VerifyKey(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				return 'L'
			if event.key == pygame.K_RIGHT:
				return 'R'

		# return print('No move');

	def desenharTabua(self):
		tabua = pygame.Rect([self.pos_x, self.pos_y, self.tamanhoW, self.tamanhoH])
		pygame.draw.rect(screen, white, tabua)
		#Superficie de desenho, cor do retangulo, posXY, tamanhoWH
		return tabua

class GameConfig:
	tabua = Tabua()
	tela = Tela()
	def VerifyQuit(self, event):
		if event.type == pygame.QUIT:
			print("Quitting...")
			execucao = False
			pygame.quit()

	def VerifyBorder(self):
		##DEFINIÇÃO DAS BORDAS para a TÁBUA
		if tabua.pos_x > width - tabua.tamanhoW:
			print('verificado direito')
			tabua.pos_x = width - tabua.tamanhoW
		if tabua.pos_x < 0:
			print('verificado esquerdo')
			tabua.pos_x = 0
## end classes

# definindo objetos

GetFontSystem = pygame.font.SysFont('Consolas', 18)

tabua = Tabua()
tela = Tela()
gameConfig = GameConfig()
#variaveis de execução

execucao = True
velocidadeX = 2
velocidadeBola = [0.5, 0.5]

################################ main #########################
# bola = Bola(velocidadeBola)
tela.iniciarTela()
moveAct = 0;
pontos = 0;

speed = [2, 2]
ball = pygame.image.load("intro_ball.gif")
default_image_size = (45, 45)
ball = pygame.transform.scale(ball, default_image_size)
ballrect = ball.get_rect()


pontosStrNivel = 'NÍVEL 1. --- VEL_TABUA = 2 --- VEL_BOLA = 200 --- PONTOS A PERDER: -5 '
pontosRenderObjNivel = pygame.font.Font.render(GetFontSystem, pontosStrNivel, False, white)

while execucao:
	for event in pygame.event.get():
		gameConfig.VerifyQuit(event)
		moveAct = tabua.VerifyKey(event)
		# print(event)

	#### VERIFICAÇÃO DE BORDAS ####
	ballrect = ballrect.move(speed)
	if ballrect.left < 0 or ballrect.right > width:
		speed[0] = -speed[0]
	if ballrect.top < 0 or ballrect.bottom > height:
		speed[1] = -speed[1]

	#### ANOTAÇÃO DOS PONTOS NEGATIVOS ######
	if ballrect.bottom > height:
		if pontos < 20: ##NIVEL 1
			pontos = pontos - 5
			print(pontos)

		if pontos > 20 and pontos < 100: ##NIVEL 2
			pontos = pontos - 30
			print(pontos)

		if pontos > 100 and pontos < 200: ##NIVEL 3
			pontos = pontos - 70
			print(pontos)

		if pontos > 200 and pontos < 400: ##NIVEL 4
			pontos = pontos - 150
			print(pontos)

		if pontos > 400 and pontos < 800: ##NIVEL 5
			pontos = pontos - 350
			print(pontos)

		if pontos > 800 and pontos < 1000: ##NIVEL 6
			pontos = pontos - 500
			print(pontos)

		if pontos > 1000 and pontos < 2000: ##NIVEL 7
			pontos = pontos - 700
			print(pontos)
	#### -- #######################
	######### ANOTAÇÃO DE NIVEL ##########
	if pontos < 20: 
		pontosStrNivel = 'NÍVEL 1. --- VEL_TABUA = 2 --- VEL_BOLA = 200 --- PONTOS A PERDER: -5 '
		pontosRenderObjNivel = pygame.font.Font.render(GetFontSystem, pontosStrNivel, False, white)			
		velocidadeX = 2
		velocidadeBola = clock.tick(velocidadeX * 100)
	if pontos > 20 and pontos < 100:
		pontosStrNivel = 'NÍVEL 2. --- VEL_TABUA = 3 --- VEL_BOLA = 300 --- PONTOS A PERDER: -30 '
		pontosRenderObjNivel = pygame.font.Font.render(GetFontSystem, pontosStrNivel, False, white)
		velocidadeX = 3
		velocidadeBola = clock.tick(velocidadeX * 100)
	if pontos > 100 and pontos < 200:
		pontosStrNivel = 'NÍVEL 3. --- VEL_TABUA = 4 --- VEL_BOLA = 400 --- PONTOS A PERDER: -70 '
		pontosRenderObjNivel = pygame.font.Font.render(GetFontSystem, pontosStrNivel, False, white)
		velocidadeX = 4
		velocidadeBola = clock.tick(velocidadeX * 100)
	if pontos > 200 and pontos < 400:
		pontosStrNivel = 'NÍVEL 4. --- VEL_TABUA = 5 --- VEL_BOLA = 500 --- PONTOS A PERDER: -150 '
		pontosRenderObjNivel = pygame.font.Font.render(GetFontSystem, pontosStrNivel, False, white)
		velocidadeX = 5
		velocidadeBola = clock.tick(velocidadeX * 100)
	if pontos > 400 and pontos < 800:
		pontosStrNivel = 'NÍVEL 5. --- VEL_TABUA = 6 --- VEL_BOLA = 600 --- PONTOS A PERDER: -350'
		pontosRenderObjNivel = pygame.font.Font.render(GetFontSystem, pontosStrNivel, False, white)
		velocidadeX = 6
		velocidadeBola = clock.tick(velocidadeX * 100)
	if pontos > 800 and pontos < 1000:
		pontosStrNivel = 'NÍVEL 6. --- VEL_TABUA = 7 --- VEL_BOLA = 700 --- PONTOS A PERDER: -500'
		pontosRenderObjNivel = pygame.font.Font.render(GetFontSystem, pontosStrNivel, False, white)
		velocidadeX = 7
		velocidadeBola = clock.tick(velocidadeX * 100)
	if pontos > 1000 and pontos < 2000:
		pontosStrNivel = 'NÍVEL 7. --- VEL_TABUA = 7 --- VEL_BOLA = 800 --- PONTOS A PERDER: -700'
		pontosRenderObjNivel = pygame.font.Font.render(GetFontSystem, pontosStrNivel, False, white)
		velocidadeX = 8
		velocidadeBola = clock.tick(velocidadeX * 100)

	tabuaRect = tabua.desenharTabua()
	if tabuaRect.colliderect(ballrect):
		speed[1] = -speed[1]
		pontos = pontos + 1 #anotação dos pontos positivos
		print(pontos)
	

	tela.pintarFundo()	
	## escreve pontos na tela:
	pontosStr = 'Pontos = ' + str(pontos)
	pontosRenderObj = pygame.font.Font.render(GetFontSystem, pontosStr, False, white)

	tabua.desenharTabua()
	gameConfig.VerifyBorder()

	tabua.move(moveAct)
	screen.blit(pontosRenderObj, [0,0])
	screen.blit(ball, ballrect)
	screen.blit(pontosRenderObjNivel, [160, 0])
	tela.atualizarTela()