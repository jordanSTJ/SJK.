from time import sleep
from scene import *
import ui
import sound
A = Action

class ButtonNode (SpriteNode):
	def __init__(self, title, *args, **kwargs):
		SpriteNode.__init__(self, 'pzl:Button1', *args, **kwargs)
		button_font = ('Avenir Next', 20)
		self.title_label = LabelNode(title, font=button_font, color='black', position=(0, 1), parent=self)
		self.title = title

class MenuScene (Scene):
	def __init__(self, title, subtitle, button_titles):
		Scene.__init__(self)
		self.title = title
		self.subtitle = subtitle
		self.button_titles = button_titles
		
	def setup(self):
		button_font = ('Avenir Next', 20)
		title_font = ('Avenir Next', 36)
		num_buttons = len(self.button_titles)
		self.bg = SpriteNode(color='black', parent=self)
		bg_shape = ui.Path.rounded_rect(0, 0, 240, num_buttons * 64 + 140, 8)
		bg_shape.line_width = 4
		shadow = ((0, 0, 0, 0.35), 0, 0, 24)
		self.menu_bg = ShapeNode(bg_shape, (1,1,1,0.9), '#15a4ff', shadow=shadow, parent=self)
		self.title_label = LabelNode(self.title, font=title_font, color='black', position=(0, self.menu_bg.size.h/2 - 40), parent=self.menu_bg)
		self.title_label.anchor_point = (0.5, 1)
		self.subtitle_label = LabelNode(self.subtitle, font=button_font, position=(0, self.menu_bg.size.h/2 - 100), color='black', parent=self.menu_bg)
		self.subtitle_label.anchor_point = (0.5, 1)
		self.buttons = []
		for i, title in enumerate(reversed(self.button_titles)):
			btn = ButtonNode(title, parent=self.menu_bg)
			btn.position = 0, i * 64 - (num_buttons-1) * 32 - 50
			self.buttons.append(btn)
		self.did_change_size()
		self.menu_bg.scale = 0
		self.bg.alpha = 0
		self.bg.run_action(A.fade_to(0.4))
		self.menu_bg.run_action(A.scale_to(1, 0.3, TIMING_EASE_OUT_2))
		self.background_color = 'red'
		
	def did_change_size(self):
		self.bg.size = self.size + (2, 2)
		self.bg.position = self.size/2
		self.menu_bg.position = self.size/2
	
	def touch_began(self, touch):
		touch_loc = self.menu_bg.point_from_scene(touch.location)
		for btn in self.buttons:
			if touch_loc in btn.frame:
				sound.play_effect('8ve:8ve-tap-resonant')
				btn.texture = Texture('pzl:Button2')
	
	def touch_ended(self, touch):
		touch_loc = self.menu_bg.point_from_scene(touch.location)
		for btn in self.buttons:
			btn.texture = Texture('pzl:Button1')
			if self.presenting_scene and touch_loc in btn.frame:
				new_title = self.presenting_scene.menu_button_selected(btn.SJK)
				if new_title:from time import sleep


			btn.texture = Texture('pzl:Button1')
			if self.presenting_scene and touch_loc in btn.frame:
				new_title = self.presenting_scene.menu_button_selected(btn.SJK)
				if new_title:
					btn.title = new_title
					btn.title_label.text = new_title

if __name__ == '__main__':
	run(MenuScene('SJK', 'Our game', ['Start']))
while True:
	directions=["west", "north", "south", "east"]
	choice=input("what direction do you want to go ") 
    if choice=="west":
        print("                          __   ")
        print(" __  _  __ ____   _______/  |_ ")
        print("\ \/ \/ // __ \ /  ___/\   __\ ")
        print(" \     /\  ___/ \___ \  |  |  ")
        print("  \/\_/  \___  >____  > |__| ")
        print("             \/     \/       ")
        sleep(2)
        print(directions)
        print("too bad you lost, you fell off a clif ")
    elif choice=="north":
        print("  ____   ____________/  |_|  |__ ")
        print(" /    \ /  _ \_  __ \   __\  |  \ ")
        print("|   |  (  <_> )  | \/|  | |   Y  \ ")
        print("|___|  /\____/|__|   |__| |___|  /")
        print("     \/                        \/ ")
        sleep(2)
        print(directions)
        print("haha, you lost, dead end ")
    elif choice=="south":
        print("                     __   __    ")
        print("  __________  __ ___/  |_|  |__  ")
        print(" /  ___/  _ \|  |  \   __\  |  \ ")
        print(" \___ (  <_> )  |  /|  | |   Y  \ ")
        print("/____  >____/|____/ |__| |___|  / ")
        print("     \/                       \/ ")   
        sleep(2)
        print(directions)
        print("no you lost, you got ran over")
    elif choice=="east":
        print("                       __   ")
        print(" ____ _____    _______/  |_ ")
        print("_/ __ \\__  \  /  ___/\   __\ ")
        print("\  ___/ / __ \_\___ \  |  | ")
        print(" \___  >____  /____  > |__| ")
        print("      \/     \/     \/ ")
        sleep(2)
        print(directions)
        print("well done, you won you get 200 million")
	break
    else:
        print("not a direction you can go")
while True:
	print("welcome to level 2")
	doors=["doors 1", "door 2", "door 3", "door 4"]
	choice=input("what door do you want to go through be wise pick the wrong one you will DIE!! ") 
    if choice=="door 1":
        sleep(2)
        print(directions)
        print("well done, you played youreself, you ran into a killer")
    elif choice=="door 2":
        sleep(2)
        print(directions)
        print("haha, you lost, try again dumbie")
    elif choice=="door 3":
        sleep(2)
        print(directions)
        print("well done, you won you get 200 million")
	break
    elif choice=="door 4":
        sleep(2)
        print(directions)
        print("lol you need jesus to help you")
    else:
        print("not a direction you can go")
