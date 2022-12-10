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
			print('VelX L = ', velocidadeX)
			print('pos_x = ', self.pos_x)

		if movement == 'R':
			pos_y = height / 2 + (height / 4)
			self.pos_x += velocidadeX
			print('VelX R = ', velocidadeX)
			print('pos_x = ', self.pos_x)

		if movement == 0:
			pos_y = height / 2 + (height / 4)
			self.pos_x = 0

	def VerifyKey(self, event):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				return 'L'
			if event.key == pygame.K_RIGHT:
				return 'R'

		return print('No move');

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


while execucao:
	for event in pygame.event.get():
		gameConfig.VerifyQuit(event)
		moveAct = tabua.VerifyKey(event)
		print(event)

	#### VERIFICAÇÃO DE BORDAS ####
	ballrect = ballrect.move(speed)
	if ballrect.left < 0 or ballrect.right > width:
		speed[0] = -speed[0]
	if ballrect.top < 0 or ballrect.bottom > height:
		speed[1] = -speed[1]

	###############################
	if ballrect.bottom > height:
		pontos = pontos - 1
		print(pontos)
	#### -- #######################
	tabuaRect = tabua.desenharTabua()
	if tabuaRect.colliderect(ballrect):
		speed[1] = -speed[1]
	

	tela.pintarFundo()	
	tabua.desenharTabua()
	gameConfig.VerifyBorder()

	tabua.move(moveAct)
	screen.blit(ball, ballrect)
	tela.atualizarTela()
	clock.tick(200)