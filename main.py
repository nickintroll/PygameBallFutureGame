import pygame
import sys

from objects import Object


_display_size = width, heigth = 1300, 800
_background_color = 12, 0, 12


def main():
	__display = pygame.display.set_mode(_display_size)


	objects = [
		Object('ball.png'),
		]
	gg = objects[0]
# 	objects.append(pygame.Surface((gg.rect.w, gg.rect.h)))
	while True:
		events = pygame.event.get()

		for event in events:
			if event.type == pygame.QUIT: sys.exit()

			# GG CONTROLL
			if event.type == pygame.KEYDOWN:
				# sides wolking
				if event.key == pygame.K_RIGHT:
					gg.vector_horisontal += 1
				if event.key == pygame.K_LEFT:
					gg.vector_horisontal -= 1
				if event.key == pygame.K_UP:
					gg.vector_vertical += 1
				if event.key == pygame.K_DOWN:
					gg.vector_vertical -= 1
				# speed up
				if event.key == pygame.K_LSHIFT:
					gg.max_speed = 5

				# rotate
				if event.key == pygame.K_SPACE:
					gg.rotate()
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_RIGHT:
					gg.vector_horisontal -= 1
				if event.key == pygame.K_LEFT:
					gg.vector_horisontal += 1
				if event.key == pygame.K_UP:
					gg.vector_vertical -= 1
				if event.key == pygame.K_DOWN:
					gg.vector_vertical += 1

				if event.key == pygame.K_LSHIFT:
					gg.max_speed = 3


		__display.fill(_background_color)
		for i in objects:

			if isinstance(i, Object):
				i.update(_display_size)
				__display.blit(i.image, i.rect)
			else:
				__display.blit(i, (0,0))
		# print(gg.rect.center)

		# destanation
		pygame.draw.line(__display, (255, 100, 100), 
			gg.rect.center, [
				gg.speed[0]*14+gg.rect.center[0],
				gg.speed[1]*14+gg.rect.center[1]]
				)

		# line to the mouse
		pygame.draw.line(__display, (100, 255, 100, 0.4),
			gg.rect.center, 
			pygame.mouse.get_pos())

		# rotate


		pygame.display.flip()



if __name__ == '__main__':
	main()