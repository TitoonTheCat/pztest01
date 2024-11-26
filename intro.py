alien = Actor('alien_green_walk2right')
alien.topright = 0,10
sens = 2

WIDTH = 500
HEIGHT = alien.height + 20

def draw():
	screen.clear()
	alien.draw()

def update():
	alien.left += sens
	if alien.left > WIDTH and sens > 0:
		alien.right = 0
	if alien.right <= 0 and sens < 0:
		alien.left = WIDTH

def on_mouse_down(pos):
	global sens
	if alien.collidepoint(pos):
		# set_alien_hurt()
		if sens == 2:
			sens = -2
		else:
			sens = 2
		set_alien_hurt()

def on_key_down(key):
	if key == LEFT:
		sens = -2
	if key == RIGHT:
		sens = +2

def set_alien_hurt():
	alien.image = 'alien_green_hurt'
	sounds.eep.play()
	clock.schedule_unique(set_alien_normal, 0.5)

def set_alien_normal():
	if sens == 2:
		alien.image = 'alien_green_walk2right'
	if sens == -2:
		alien.image = 'alien_green_walk2left'
