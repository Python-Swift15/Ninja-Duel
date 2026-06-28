import tkinter as tk
import random
import math

root = tk.Tk()
root.title("Ninja Duel - 360 Arena")

# --- 1. Fullscreen Setup ---
W = root.winfo_screenwidth()
H = root.winfo_screenheight()
root.attributes('-fullscreen', True) 
root.bind('<Escape>', lambda e: root.destroy()) 

canvas = tk.Canvas(root, width=W, height=H, highlightthickness=0)
canvas.pack(fill="both", expand=True)

NINJA_W = 128 
NINJA_H = 128
STAR_W = 64 
STAR_SPEED = 12 
NINJA_SPEED = 6

# --- 2. Load Images ---
bg_image = tk.PhotoImage(file='01_Tiles (Working folder)/tile_0004.png').zoom(2)

images = {
    'ninja1': tk.PhotoImage(file='01_Tiles (Working folder)/tile_0000.png').zoom(2),
    'ninja2': tk.PhotoImage(file='01_Tiles (Working folder)/tile_0001.png').zoom(2),
    'star': tk.PhotoImage(file='01_Tiles (Working folder)/tile_0002.png').zoom(2),
    'heart': tk.PhotoImage(file='01_Tiles (Working folder)/tile_0006.png').zoom(2) 
}

# --- 3. Game Variables ---
p1_lives = 3
p2_lives = 3
game_over = False
menu_active = True
game_mode = 'computer' 

ai_speed = 4
ai_shoot_chance = 60 

n1_x, n1_y = 150, H // 2
n2_x, n2_y = W - 150, H // 2

p1_stars = []
p2_stars = []
p1_reloading = False
p2_reloading = False

keys_pressed = {}
mouse_x, mouse_y = W // 2, H // 2

ninja1_img = None
ninja2_img = None
p1_turret = None
p2_turret = None
p1_heart_icons = []
p2_heart_icons = []

# --- 4. Drawing Functions ---
def update_hearts():
    for heart_id in p1_heart_icons + p2_heart_icons:
        canvas.delete(heart_id)
    p1_heart_icons.clear()
    p2_heart_icons.clear()
    
    for i in range(p1_lives):
        x_pos = 60 + (i * 60) 
        h = canvas.create_image(x_pos, 60, image=images['heart'], anchor='center')
        p1_heart_icons.append(h)
        
    for i in range(p2_lives):
        x_pos = (W - 60) - (i * 60)
        h = canvas.create_image(x_pos, 60, image=images['heart'], anchor='center')
        p2_heart_icons.append(h)

def draw_all():
    global ninja1_img, ninja2_img, p1_turret, p2_turret
    canvas.delete('all')
    
    bg_w = bg_image.width()
    bg_h = bg_image.height()
    for x in range(0, W, bg_w):
        for y in range(0, H, bg_h):
            canvas.create_image(x, y, image=bg_image, anchor='nw')
            
    # Draw turrets FIRST so they appear underneath the ninjas!
    # They are drawn as thick lines that act as rectangles.
    p1_turret = canvas.create_line(n1_x, n1_y, n1_x, n1_y, fill='#00ffcc', width=14)
    p2_turret = canvas.create_line(n2_x, n2_y, n2_x, n2_y, fill='#ff3333', width=14)
            
    ninja1_img = canvas.create_image(n1_x, n1_y, image=images['ninja1'], anchor='center')
    ninja2_img = canvas.create_image(n2_x, n2_y, image=images['ninja2'], anchor='center')
    update_hearts()

# --- 5. Controls ---
def key_down(e):
    keys_pressed[e.keysym.lower()] = True

def key_up(e):
    keys_pressed[e.keysym.lower()] = False

def update_mouse(e):
    global mouse_x, mouse_y
    mouse_x, mouse_y = e.x, e.y

root.bind('<KeyPress>', key_down)
root.bind('<KeyRelease>', key_up)
root.bind('<Motion>', update_mouse)

def p1_shoot(event=None):
    # The global declaration MUST be at the very top of the function!
    global p1_reloading 
    
    if menu_active or game_over or p1_reloading: return
    
    if len(p1_stars) < 3:
        angle = math.atan2(mouse_y - n1_y, mouse_x - n1_x)
        vx = STAR_SPEED * math.cos(angle)
        vy = STAR_SPEED * math.sin(angle)
        
        s_id = canvas.create_image(n1_x, n1_y, image=images['star'], anchor='center')
        p1_stars.append({'id': s_id, 'x': n1_x, 'y': n1_y, 'vx': vx, 'vy': vy})
        
        if len(p1_stars) == 3: p1_reloading = True

root.bind('<Button-1>', p1_shoot) 

def p2_shoot(event=None):
    # Fix Player 2's global declaration as well!
    global p2_reloading 
    
    if menu_active or game_over or p2_reloading: return
    
    if len(p2_stars) < 3:
        angle = math.atan2(n1_y - n2_y, n1_x - n2_x)
            
        vx = STAR_SPEED * math.cos(angle)
        vy = STAR_SPEED * math.sin(angle)
        
        s_id = canvas.create_image(n2_x, n2_y, image=images['star'], anchor='center')
        p2_stars.append({'id': s_id, 'x': n2_x, 'y': n2_y, 'vx': vx, 'vy': vy})
        
        if len(p2_stars) == 3: p2_reloading = True

root.bind('<Return>', p2_shoot)

# --- 6. Menus and Game Logic ---
def show_menu():
    global menu_active
    menu_active = True
    canvas.delete('all')
    
    bg_w = bg_image.width()
    bg_h = bg_image.height()
    for x in range(0, W, bg_w):
        for y in range(0, H, bg_h):
            canvas.create_image(x, y, image=bg_image, anchor='nw')
            
    canvas.create_rectangle(W//4, H//5, 3*W//4, 4*H//5, fill='#1a1a2e', outline='white', width=4)
    canvas.create_text(W//2, H//4, text="360 NINJA ARENA", font=('Arial', 48, 'bold'), fill='white')
    
    canvas.create_text(W//2, H//2 - 40, text="Press 1: VS Friend (WASD vs Arrows)", font=('Arial', 24), fill='yellow')
    canvas.create_text(W//2, H//2 + 10, text="Press 2: VS Computer (EASY)", font=('Arial', 20), fill='#00ff00')
    canvas.create_text(W//2, H//2 + 50, text="Press 3: VS Computer (MEDIUM)", font=('Arial', 20), fill='#ffaa00')
    canvas.create_text(W//2, H//2 + 90, text="Press 4: VS Computer (HARD)", font=('Arial', 20), fill='#ff0000')
    canvas.create_text(W//2, 4*H//5 - 40, text="Press ESC to Quit", font=('Arial', 14), fill='gray')

def start_match(mode, diff='medium'):
    global game_mode, menu_active, n1_x, n1_y, n2_x, n2_y, game_over
    global p1_stars, p2_stars, p1_reloading, p2_reloading, p1_lives, p2_lives
    global ai_speed, ai_shoot_chance
    
    game_mode = mode
    menu_active = False
    game_over = False
    
    if mode == 'computer':
        if diff == 'easy': ai_speed, ai_shoot_chance = 3, 100
        elif diff == 'medium': ai_speed, ai_shoot_chance = 5, 60
        elif diff == 'hard': ai_speed, ai_shoot_chance = 7, 30
            
    n1_x, n1_y = 150, H // 2
    n2_x, n2_y = W - 150, H // 2
    p1_stars.clear()
    p2_stars.clear()
    p1_reloading = False
    p2_reloading = False
    p1_lives = 3
    p2_lives = 3
    
    keys_pressed.clear()
    draw_all()
    game_loop()

root.bind('1', lambda e: start_match('friend') if menu_active else None)
root.bind('2', lambda e: start_match('computer', 'easy') if menu_active else None)
root.bind('3', lambda e: start_match('computer', 'medium') if menu_active else None)
root.bind('4', lambda e: start_match('computer', 'hard') if menu_active else None)

def hits(star_x, star_y, ninja_x, ninja_y):
    return (abs(ninja_x - star_x) < (NINJA_W // 2 + STAR_W // 2) and
            abs(ninja_y - star_y) < (NINJA_H // 2 + STAR_W // 2))

def clamp(val, min_val, max_val):
    return max(min_val, min(val, max_val))

def game_loop():
    global p1_lives, p2_lives, n1_x, n1_y, n2_x, n2_y, p1_reloading, p2_reloading
    
    if game_over or menu_active: return
        
    # --- Player 1 Logic ---
    if keys_pressed.get('w'): n1_y -= NINJA_SPEED
    if keys_pressed.get('s'): n1_y += NINJA_SPEED
    if keys_pressed.get('a'): n1_x -= NINJA_SPEED
    if keys_pressed.get('d'): n1_x += NINJA_SPEED
    
    n1_x = clamp(n1_x, NINJA_W//2, W - NINJA_W//2)
    n1_y = clamp(n1_y, NINJA_H//2, H - NINJA_H//2)
    canvas.coords(ninja1_img, n1_x, n1_y)
    
    # Update Player 1 Turret (Aiming at Mouse)
    p1_angle = math.atan2(mouse_y - n1_y, mouse_x - n1_x)
    p1_tx = n1_x + 85 * math.cos(p1_angle)
    p1_ty = n1_y + 85 * math.sin(p1_angle)
    canvas.coords(p1_turret, n1_x, n1_y, p1_tx, p1_ty)
    
    # --- Player 2 / AI Logic ---
    p2_angle = math.atan2(n1_y - n2_y, n1_x - n2_x) # Always aiming at Player 1
    
    if game_mode == 'computer':
        dist = math.hypot(n1_x - n2_x, n1_y - n2_y)
        
        if dist > 250:
            n2_x += ai_speed * math.cos(p2_angle)
            n2_y += ai_speed * math.sin(p2_angle)
        elif dist < 150:
            n2_x -= ai_speed * math.cos(p2_angle)
            n2_y -= ai_speed * math.sin(p2_angle)
            
        if not p2_reloading and random.randint(1, ai_shoot_chance) == 1:
            p2_shoot()
    else:
        if keys_pressed.get('up'): n2_y -= NINJA_SPEED
        if keys_pressed.get('down'): n2_y += NINJA_SPEED
        if keys_pressed.get('left'): n2_x -= NINJA_SPEED
        if keys_pressed.get('right'): n2_x += NINJA_SPEED

    n2_x = clamp(n2_x, NINJA_W//2, W - NINJA_W//2)
    n2_y = clamp(n2_y, NINJA_H//2, H - NINJA_H//2)
    canvas.coords(ninja2_img, n2_x, n2_y)
    
    # Update Player 2 Turret (Aiming at Player 1)
    p2_tx = n2_x + 85 * math.cos(p2_angle)
    p2_ty = n2_y + 85 * math.sin(p2_angle)
    canvas.coords(p2_turret, n2_x, n2_y, p2_tx, p2_ty)
            
    # --- P1 Stars ---
    for star in p1_stars[:]:
        star['x'] += star['vx']
        star['y'] += star['vy']
        canvas.coords(star['id'], star['x'], star['y'])
        
        if hits(star['x'], star['y'], n2_x, n2_y):
            canvas.delete(star['id'])
            p1_stars.remove(star)
            p2_lives -= 1                        
            update_hearts() 
            if p2_lives <= 0: return end_game('Player 1 Wins!')
                
        elif not (0 <= star['x'] <= W and 0 <= star['y'] <= H):
            canvas.delete(star['id'])
            p1_stars.remove(star)
            
    if p1_reloading and len(p1_stars) == 0: p1_reloading = False
            
    # --- P2 Stars ---
    for star in p2_stars[:]:
        star['x'] += star['vx']
        star['y'] += star['vy']
        canvas.coords(star['id'], star['x'], star['y'])
            
        if hits(star['x'], star['y'], n1_x, n1_y):
            canvas.delete(star['id'])
            p2_stars.remove(star)
            p1_lives -= 1                           
            update_hearts() 
            if p1_lives <= 0: return end_game('Player 2 Wins!')
                
        elif not (0 <= star['x'] <= W and 0 <= star['y'] <= H):
            canvas.delete(star['id'])
            p2_stars.remove(star)
            
    if p2_reloading and len(p2_stars) == 0: p2_reloading = False
            
    root.after(16, game_loop)

def end_game(winner):
    global game_over
    game_over = True
    
    canvas.create_rectangle(W//4, H//3, 3*W//4, 2*H//3, fill='black', outline='white', width=4)
    canvas.create_text(W//2, H//2 - 20, text=winner, font=('Arial', 48, 'bold'), fill='yellow')
    canvas.create_text(W//2, H//2 + 40, text='Press M for Main Menu', font=('Arial', 18), fill='white')
        
def go_to_menu(event):
    if game_over: show_menu()
        
root.bind('<m>', go_to_menu)

# --- 7. Start the Game at the Menu ---
show_menu()
root.mainloop()