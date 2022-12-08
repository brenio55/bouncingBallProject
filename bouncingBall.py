import pygame

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
class Tela:		
	width = 640
	height = 480	
	fundo = pygame.display.set_mode((width, height))

	def blitt(self, surface, location):
		self.fundo.blit(surface, location)

	def iniciarTela(self):		
		pygame.display.set_caption("Bouncing Ball")

	def pintarFundo(self):
		self.fundo.fill(blue)

	def atualizarTela(self):
		pygame.display.flip()

class Bola:
	def __init__(self):
		self.ball = 0;
		self.default_image_size = (0,0);
		self.ballrect = 0;

	def ballLoad(self):
		self.ball = pygame.image.load("intro_ball.gif")
		self.default_image_size = (45, 45)
		self.ball = pygame.transform.scale(self.ball, self.default_image_size)
		return self.ball

	def ballRect(self, arg='unset'):
		if (arg == 'unset'):
			self.ballrect = self.ballLoad().get_rect()
			print('ARG IS NOT SET')
			return self.ballrect
		else:
			self.ballrect = arg.get_rect()
			print('ARG IS SET')
			return self.ballrect

	def createBall(self): 
		self.ballLoad()
		self.ballRect(self.ball)

	def blitBall(self):
		# tela = Tela()
		# self.ballrect.move(velocidadeBola)
		# if (self.ballrect.left <0) or (self.ballrect.right > tela.width):
		#  	velocidadeBola = -velocidadeBola
    	# if (self.ballrect.top < 0) or (self.ballrect.bottom > tela.height):
        # 	velocidadeBola = -velocidadeBola
		tela.blitt(self.ballLoad(), self.ballRect(self.ball))

		# return 0



class Tabua:
	tela = Tela()
	tamanhoW = 70
	tamanhoH = 10

	pos_x = tela.width / 2 - (tamanhoW / 2)
	pos_y = tela.height / 2 + (tela.height / 4)

	def move(self, movement):
		if movement == 'L':
			pos_y = tela.height / 2 + (tela.height / 4)
			self.pos_x += -velocidadeX
			print('VelX L = ', velocidadeX)
			print('pos_x = ', self.pos_x)

		if movement == 'R':
			pos_y = tela.height / 2 + (tela.height / 4)
			self.pos_x += velocidadeX
			print('VelX R = ', velocidadeX)
			print('pos_x = ', self.pos_x)

		if movement == 0:
			pos_y = tela.height / 2 + (tela.height / 4)
			self.pos_x = 0

	def VerifyKey(self):
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				return 'L'
			if event.key == pygame.K_RIGHT:
				return 'R'

		return print('No move');

	def desenharTabua(self):
		pygame.draw.rect(tela.fundo, white, [self.pos_x, self.pos_y, self.tamanhoW, self.tamanhoH])
		#Superficie de desenho, cor do retangulo, posXY, tamanhoWH

class GameConfig:
	tabua = Tabua()
	tela = Tela()
	def VerifyQuit(self, event):
		if event.type == pygame.QUIT:
			print("Quitting...")
			execucao = False
			pygame.quit()

	def VerifyBorder(self):
		##DEFINIÇÃO DAS BORDAS
		if tabua.pos_x > tela.width - tabua.tamanhoW:
			print('verificado direito')
			tabua.pos_x = tela.width - tabua.tamanhoW
		if tabua.pos_x < 0:
			print('verificado esquerdo')
			tabua.pos_x = 0
## end classes

# definindo objetos
tabua = Tabua()
tela = Tela()
gameConfig = GameConfig()
bola = Bola()
#variaveis de execução
execucao = True
velocidadeX = 0.7
velocidadeBola = 0.75
#main
tela.iniciarTela()
bola.createBall()
moveAct = 0;

while execucao:
	for event in pygame.event.get():
		gameConfig.VerifyQuit(event)
		moveAct = tabua.VerifyKey()
		print(event)

	tela.pintarFundo()	
	tabua.desenharTabua()
	gameConfig.VerifyBorder()
	bola.blitBall()
	tabua.move(moveAct)
	tela.atualizarTela()