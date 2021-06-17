import pygame

class Platform:

	def __init__(self, Arena_Game):
		#Init Screen For Platform
		self.screen = Arena_Game.screen
		self.screen_rect = self.screen.get_rect()

		#Init Platform Image
		self.game_settings = Arena_Game.game_settings
		self.image = self.game_settings.platform_image
		self.image_rect = self.image.get_rect()
		self.scaleWidth()

		#Init Platform Position
		self.image_rect.midbottom = self.screen_rect.midbottom

		#tambahan posisi khusus x
		self.x = self.image_rect.x

	def scaleWidth(self):
		height = self.image_rect.height
		width2x = self.image_rect.width * 2
		self.image = pygame.transform.scale(self.image, (width2x, height))

	def move(self):
		if self.image_rect.centerx <= self.screen_rect.left:
			self.x = 0
		self.x -= self.game_settings.platform_speed
		self.image_rect.x = self.x

	def show_platform(self):
		self.screen.blit(self.image, self.image_rect)