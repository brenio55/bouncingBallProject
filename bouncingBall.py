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
	tela = Tela()
	def __init__(self):
		self.ballFile = 0;
		self.default_image_size = (0,0);
		self.ballrect = self.ballLoad().get_rect();
		self.pos_x = 0
		self.pos_y = 0

	def move(self, velBola : int):
		if ((self.ballrect.left < 0) or (self.ballrect.right > tela.width)):
			self.pos_x += -velBola
		if ((self.ballrect.top < 0) or (self.ballrect.bottom > tela.height)):
			self.pos_y += -velBola

		self.pos_x += velBola
		self.pos_y += velBola

		return [self.pos_x, self.pos_y]

	def ballLoad(self):
		self.ballFile = pygame.image.load("intro_ball.gif")
		self.default_image_size = (45, 45)
		self.ballObj = pygame.transform.scale(self.ballFile, self.default_image_size)
		self.pos = (5,5)
		return self.ballObj

	# self.ballrect = arg.get_rect(top = topLeft[1], left = topLeft[0], width=45, height=45)

	def blitBall(self):
		ballMove = self.move(velocidadeBola)
		ballX = ballMove[0]
		ballY = ballMove[1]

		tela.blitt(self.ballLoad(), self.ballLoad().get_rect(top = ballY, left = ballX, width = 45, height=45))
		print('ballX = ', ballX)
		print('ballY = ', ballY)
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
		##DEFINIÇÃO DAS BORDAS para a TÁBUA
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
velocidadeBola = 0.3
################################ main #########################
tela.iniciarTela()
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