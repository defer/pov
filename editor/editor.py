import pygame
from pygame.color import THECOLORS

#constants
BLOCK_SIZE=32
LEDS=8
WINDOW_WIDTH=1024
WIN_SIZE = (WINDOW_WIDTH+1, BLOCK_SIZE*LEDS+1)



class Editor:
	def __init__(self):
		self.status = [ [ False for i in xrange(0,WINDOW_WIDTH/BLOCK_SIZE)] for j in xrange(0,LEDS)]

	def arduinoArrayOutput(self):
		last = len(self.status[0])

		for i in xrange(last-1, -1, -1):
			empty = True
			for j in xrange(0,LEDS):
				if self.status[j][i] == True:
					empty = False
			if not empty:
				last = i
				break
		print last

		header = 'int A[] = {'
		content = ''
		for j in xrange(0,last+1):
			value = 0
			cnt = 0
			for i in xrange(0,LEDS):
				if self.status[i][j]:
					value = value | (1<<cnt)
				cnt+=1
			content += str(value) + ','
		footer = '};'

		print header+content+footer

	def drawSquares (self, screen):
		for i in xrange(0, LEDS):
			for j in xrange(0, WINDOW_WIDTH/BLOCK_SIZE):
				Y0 = i*BLOCK_SIZE
				X0 = j*BLOCK_SIZE
				Y1 = BLOCK_SIZE
				X1 = BLOCK_SIZE
				pygame.draw.rect(screen, (0,0,0), (X0,Y0,Y1,X1))
				if self.status[i][j]:
					pygame.draw.rect(screen, (255,0,0), (X0+1,Y0+1,Y1-1,X1-1))
				else:
					pygame.draw.rect(screen, (255,255,255), (X0+1,Y0+1,Y1-1,X1-1))

	def toggleLed (self,pos):
		x = int(pos[0]/BLOCK_SIZE)
		y = int(pos[1]/BLOCK_SIZE)

		self.status[y][x] = not self.status[y][x]

	def mainLoop (self):
		pygame.init()

		screen = pygame.display.set_mode (WIN_SIZE)
		clock = pygame.time.Clock()
		
		done = False
		while not done:
			events = pygame.event.get()
			clock.tick(25)
			for event in events:
				if event.type == 'QUIT':
					done = True
					break
				if event.type == pygame.MOUSEBUTTONDOWN:
					buttons = pygame.mouse.get_pressed()
#					print buttons
					if buttons[0] == 1: #left click
						self.toggleLed(pygame.mouse.get_pos())
					elif buttons[2] == 1: #right click
						self.arduinoArrayOutput()

			screen.fill((255,255,255))
			self.drawSquares(screen)
			
			pygame.display.flip()
			#TODO: mouse events

if __name__ == "__main__":
	editor = Editor()
	editor.mainLoop()
