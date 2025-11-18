import pygame
import random
import time
import json
import os
import sys
import math
from datetime import datetime

# --- Configuration ---
GRID_SIZE = 15
CELL_SIZE = 40
FONT_SIZE = 40
WORD_FONT_SIZE = 24
QUESTION_FONT_SIZE = 28
TEXT_COLOR = (0, 0, 0)
BG_COLOR = (255, 255, 255)
GRID_COLOR = (88, 101, 242)
BUTTON_COLOR = (114, 137, 218)
HIGHLIGHT_COLOR = (114, 137, 218)
FOUND_WORD_COLOR = (46, 204, 113)
RED_COLOR = (255, 60, 60)
GOLD_COLOR = (255, 215, 0)
CUSTOM_CURSOR_PATH = 'Midterm-Project/cursor_pen.png'
LIVES_ICON_PATH = 'Midterm-Project/lives.png'
LOGO_IMAGE_PATH = 'Midterm-Project/Game_Logo.png'
MENU_BACKGROUND_PATH = 'Midterm-Project/Game_grounds.png'
QUESTION_TIME_LIMIT = 60
BONUS_TIME_THRESHOLD = 10
PAUSE_DURATION = 5

TIMER_BG_COLOR = (85, 85, 85)
TIMER_FILL_COLOR = (46, 204, 113)

BACKGROUND_IMAGE_PATHS = [
    'Midterm-Project/Stage_1.jpg',
    'Midterm-Project/Stage_2.jpg',
    'Midterm-Project/Stage_3.jpg',
]

# --- Stage Logo Image Paths ---
STAGE_LOGO_PATHS = [
    'Midterm-Project/Stage1.png',
    'Midterm-Project/Stage2.png',
    'Midterm-Project/Stage3.png',
]

# --- Score Board Image Paths ---
SCORE_BOARD_PATHS = [
    'Midterm-Project/stage1_score_board.png',
    'Midterm-Project/stage2_score_board.png',
    'Midterm-Project/stage3_score_board.png',
]

STAGES_DATA = [
    # Stage 1: 20 Questions
    [
        {'question': "A popular library for creating games in Python.", 'answer': "PYGAME"},
        {'question': "The high-level language this game is written in.", 'answer': "PYTHON"},
        {'question': "A set of instructions executed by a computer.", 'answer': "SCRIPT"},
        {'question': "The fundamental building block of a program.", 'answer': "CODE"},
        {'question': "To find and fix errors in a program.", 'answer': "DEBUG"},
        {'question': "The brain of the computer.", 'answer': "CPU"},
        {'question': "The permanent memory of a computer.", 'answer': "ROM"},
        {'question': "The temporary memory of a computer.", 'answer': "RAM"},
        {'question': "The first page of a website.", 'answer': "HOMEPAGE"},
        {'question': "The markup language of the web.", 'answer': "HTML"},
        {'question': "The styling language of the web.", 'answer': "CSS"},
        {'question': "The scripting language of the web.", 'answer': "JAVASCRIPT"},
        {'question': "A device used to display output from a computer.", 'answer': "MONITOR"},
        {'question': "The inventor of the World Wide Web.", 'answer': "BERNERSLEE"},
        {'question': "The main circuit board of a computer.", 'answer': "MOTHERBOARD"},
        {'question': "A small portable computer.", 'answer': "LAPTOP"},
        {'question': "An input device used to type.", 'answer': "KEYBOARD"},
        {'question': "An input device used to point and click.", 'answer': "MOUSE"},
        {'question': "A search engine owned by Google.", 'answer': "CHROME"},
        {'question': "A search engine represented by a blue 'e'.", 'answer': "EDGE"},
    ],
    # Stage 2: 20 Questions
    [
        {'question': "A versatile language often used for web development.", 'answer': "JAVA"},
        {'question': "A named storage location in memory.", 'answer': "VARIABLE"},
        {'question': "A reusable block of code that performs a specific task.", 'answer': "FUNCTION"},
        {'question': "A control flow statement that repeats a block of code.", 'answer': "LOOP"},
        {'question': "A structure for holding the letters in a word search.", 'answer': "GRID"},
        {'question': "A self-contained file with Python code.", 'answer': "MODULE"},
        {'question': "A collection of data in rows and columns.", 'answer': "MATRIX"},
        {'question': "A programming concept for combining related data and functions.", 'answer': "CLASS"},
        {'question': "The blue bird social media platform (former name).", 'answer': "TWITTER"},
        {'question': "The company that makes iPhones.", 'answer': "APPLE"},
        {'question': "The company that makes Windows.", 'answer': "MICROSOFT"},
        {'question': "The company that makes Android.", 'answer': "GOOGLE"},
        {'question': "The first mechanical computer creator Charles _____.", 'answer': "BABBAGE"},
        {'question': "A collection of web pages.", 'answer': "WEBSITE"},
        {'question': "The physical parts of a computer.", 'answer': "HARDWARE"},
        {'question': "The non-physical programs of a computer.", 'answer': "SOFTWARE"},
        {'question': "The storage device using spinning disks.", 'answer': "HDD"},
        {'question': "The faster storage device using flash memory.", 'answer': "SSD"},
        {'question': "A place to store files on the internet.", 'answer': "CLOUD"},
        {'question': "The 'G' in GIF stands for.", 'answer': "GRAPHICS"},
    ],
    # Stage 3: 20 Questions
    [
        {'question': "What does 'GUI' stand for? (Graphical User...)", 'answer': "INTERFACE"},
        {'question': "A collection of pre-written code for common tasks.", 'answer': "LIBRARY"},
        {'question': "A step-by-step procedure for solving a problem.", 'answer': "ALGORITHM"},
        {'question': "A system for naming and locating resources on the internet (e.g., a web address).", 'answer': "URL"},
        {'question': "The physical components of a computer system.", 'answer': "HARDWARE"},
        {'question': "A collection of related data stored in a computer.", 'answer': "DATABASE"},
        {'question': "The programs and operating information used by a computer.", 'answer': "SOFTWARE"},
        {'question': "Protecting computer systems and networks from theft or damage.", 'answer': "SECURITY"},
        {'question': "A global computer network providing a variety of information.", 'answer': "INTERNET"},
        {'question': "The process of creating a computer program.", 'answer': "DEVELOP"},
        {'question': "A type of data structure that holds an ordered collection of items.", 'answer': "LIST"},
        {'question': "A conditional statement that executes a block of code if a condition is true.", 'answer': "IF"},
        {'question': "A special value in Python that represents nothing.", 'answer': "NONE"},
        {'question': "A container that stores data in key-value pairs.", 'answer': "DICTIONARY"},
        {'question': "A framework for organizing code into manageable units.", 'answer': "ARCHITECTURE"},
        {'question': "The 'P' in PNG stands for.", 'answer': "PORTABLE"},
        {'question': "The 'J' in JPEG stands for.", 'answer': "JOINT"},
        {'question': "A malicious software program.", 'answer': "VIRUS"},
        {'question': "A self-replicating program.", 'answer': "WORM"},
        {'question': "A program that disguises as useful software.", 'answer': "TROJAN"},
    ]
]
# New list to track completion requirements per stage
STAGES_COMPLETION_REQUIREMENTS = [5, 8, 12]

DIRECTIONS = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
COLOR_ORDER = []

# --- Pygame Initialization ---
pygame.init()
pygame.font.init()
pygame.mixer.init()
screen_width = GRID_SIZE * CELL_SIZE
screen_height = screen_width + 200
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Word Search Trivia")
pygame.mouse.set_visible(False)

# --- Fonts ---
font = pygame.font.Font(None, FONT_SIZE)
word_font = pygame.font.Font(None, WORD_FONT_SIZE)
question_font = pygame.font.Font(None, QUESTION_FONT_SIZE)
title_font = pygame.font.Font(None, 80)
score_font = pygame.font.Font(None, 60) # <--- ADDED: New font for the score
all_colored_images = None
stage_backgrounds = []
stage_logos = []
score_board_images = []
menu_background_image = None
time_out_sound = None

# --- Load Assets ---
try:
    custom_cursor_image = pygame.image.load(CUSTOM_CURSOR_PATH).convert_alpha()
    custom_cursor_image = pygame.transform.scale(custom_cursor_image, (48, 48))
except Exception as e:
    print(f"Error loading custom cursor image: {e}")
    custom_cursor_image = None

try:
    correct_word_sound = pygame.mixer.Sound('Midterm-Project/sound_effect_correct_word.mp3')
except Exception as e:
    print(f"Error loading sound: {e}")
    correct_word_sound = None

try:
    lives_icon = pygame.image.load(LIVES_ICON_PATH).convert_alpha()
    lives_icon = pygame.transform.scale(lives_icon, (40, 40))
except Exception as e:
    print(f"Error loading lives icon: {e}")
    lives_icon = None

# Load the logo image
try:
    logo_image = pygame.image.load(LOGO_IMAGE_PATH).convert_alpha()
    logo_width = int(screen_width * 0.8)
    logo_height = int(logo_image.get_height() * (logo_width / logo_image.get_width()))
    logo_image = pygame.transform.scale(logo_image, (logo_width, logo_height))
except Exception as e:
    print(f"Error loading logo image: {e}")
    logo_image = None
    
# --- Game State ---
grid = [['' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
found_words_data = []
mouse_start_pos, mouse_end_pos = None, None
is_drawing, champion = False, False
current_stage_index, current_question_index = 0, 0
question_start_time = 0
is_paused, pause_end_time = False, 0
player_lives = 3
selected_word_state = {'word': '', 'color': TEXT_COLOR}
flash_end_time = 0
correct_guess_time = 0
logo_float_time = 0
is_time_out_triggered = False
# New state variables
correct_answers_this_stage = 0
questions_used_this_stage = []
total_questions_taken = 0

# --- Time Tracking Globals ---
FASTEST_TIME_FILE = 'Midterm-Project/fastest_time.json'
fastest_times_data = None


# --- Helper Functions ---
def load_or_create_fastest_times():
    """Loads fastest times from JSON, creating/validating a structure if needed."""
    try:
        with open(FASTEST_TIME_FILE, 'r') as f:
            data = json.load(f)
        if 'stages' not in data or len(data['stages']) != len(STAGES_DATA):
            raise ValueError("Mismatched stage count in JSON.")
        for i, stage in enumerate(STAGES_DATA):
            if 'questions' not in data['stages'][i] or len(data['stages'][i]['questions']) != len(stage):
                raise ValueError(f"Mismatched question count in Stage {i+1}.")
        print("Fastest times loaded and validated successfully.")
        return data
    except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
        print(f"Fastest time file issue: {e}. Creating a new one.")
        default_data = {"stages": []}
        for stage_questions in STAGES_DATA:
            stage_data = {"questions": []}
            for _ in stage_questions:
                stage_data["questions"].append({
                    "fastest_time_seconds": None,
                    "completion_date": None
                })
            default_data["stages"].append(stage_data)
        save_fastest_times(default_data)
        return default_data

def save_fastest_times(data):
    """Saves the fastest times data to the JSON file."""
    try:
        with open(FASTEST_TIME_FILE, 'w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"Error saving fastest times: {e}")

def load_background_images():
    global stage_backgrounds
    stage_backgrounds = []
    dim_surface = pygame.Surface((screen_width, screen_height)); dim_surface.fill((0, 0, 0)); dim_surface.set_alpha(150)
    for i, path in enumerate(BACKGROUND_IMAGE_PATHS):
        try:
            image = pygame.image.load(path).convert()
            scaled_image = pygame.transform.scale(image, (screen_width, screen_height))
            scaled_image.blit(dim_surface, (0, 0))
            stage_backgrounds.append(scaled_image)
            print(f"Successfully loaded background for Stage {i+1}")
        except Exception as e:
            print(f"Error loading background {path}: {e}.")
            stage_backgrounds.append(None)

def load_stage_logos():
    global stage_logos
    for path in STAGE_LOGO_PATHS:
        try:
            image = pygame.image.load(path).convert_alpha()
            logo_width = int(screen_width * 0.9)
            logo_height = int(image.get_height() * (logo_width / image.get_width()))
            scaled_image = pygame.transform.scale(image, (logo_width, logo_height))
            stage_logos.append(scaled_image)
            print(f"Successfully loaded stage logo: {path}")
        except Exception as e:
            print(f"Error loading stage logo {path}: {e}")
            stage_logos.append(None)
            
def load_score_board_images():
    global score_board_images
    for path in SCORE_BOARD_PATHS:
        try:
            image = pygame.image.load(path).convert_alpha()
            scaled_image = pygame.transform.scale(image, (screen_width, screen_height))
            score_board_images.append(scaled_image)
            print(f"Successfully loaded score board image: {path}")
        except Exception as e:
            print(f"Error loading score board image {path}: {e}")
            score_board_images.append(None)

def load_letter_images():
    global COLOR_ORDER, all_colored_images
    all_colored_images = {}
    base_path = r"C:\Users\mark paolo\Documents\Vs Code File\Laboratories in Python\Midterm-Project\assets_letterTiles\PNG"
    color_folders = ["Blue", "Box", "Brown", "Marble", "Metal", "Solid", "Wood", "Yellow"]
    COLOR_ORDER = []
    for color in color_folders:
        color_path = os.path.join(base_path, color)
        if not os.path.exists(color_path):
            continue
        letter_images = {}
        for char in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            image_path = os.path.join(color_path, f"Letter_{char}.png")
            if os.path.exists(image_path):
                try:
                    image = pygame.image.load(image_path).convert_alpha()
                    letter_images[char] = pygame.transform.scale(image, (CELL_SIZE, CELL_SIZE))
                except Exception as e:
                    print(f"Error loading image {image_path}: {e}")
        if letter_images:
            all_colored_images[color] = letter_images
            COLOR_ORDER.append(color)

def is_valid_placement(word, row, col, direction):
    dr, dc = direction
    for i, char in enumerate(word):
        r, c = row + i * dr, col + i * dc
        if not (0 <= r < GRID_SIZE and 0 <= c < GRID_SIZE):
            return False
        if grid[r][c] not in ('', char):
            return False
    return True

def place_word(word, row, col, direction):
    dr, dc = direction
    for i, char in enumerate(word):
        r, c = row + i * dr, col + i * dc
        grid[r][c] = char

def generate_grid(words_to_place):
    global grid
    grid = [['' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]
    for word in sorted(words_to_place, key=len, reverse=True):
        placed, attempts = False, 0
        while not placed and attempts < 1000:
            row, col, direction = random.randint(0, GRID_SIZE - 1), random.randint(0, GRID_SIZE - 1), random.choice(DIRECTIONS)
            if is_valid_placement(word, row, col, direction):
                place_word(word, row, col, direction)
                placed = True
            attempts += 1
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            if grid[r][c] == '':
                grid[r][c] = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

def draw_grid():
    grid_bg = pygame.Surface((GRID_SIZE * CELL_SIZE, GRID_SIZE * CELL_SIZE)); grid_bg.set_alpha(100); grid_bg.fill(BG_COLOR); screen.blit(grid_bg, (0, 0))
    grid_font = pygame.font.Font(None, FONT_SIZE - 4)
    for r in range(GRID_SIZE):
        for c in range(GRID_SIZE):
            rect = pygame.Rect(c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, GRID_COLOR, rect, 1)
            letter_surface = grid_font.render(grid[r][c], True, TEXT_COLOR)
            screen.blit(letter_surface, letter_surface.get_rect(center=rect.center))

def draw_text_wrapped(surface, text, pos, font, color, max_width):
    words, lines, current_line = text.split(' '), [], ""
    for word in words:
        test_line = f"{current_line}{word} "
        if font.size(test_line)[0] < max_width:
            current_line = test_line
        else:
            lines.append(current_line)
            current_line = f"{word} "
    lines.append(current_line)
    x, y = pos
    for line in lines:
        line_surface = font.render(line, True, color)
        surface.blit(line_surface, (x, y))
        y += font.get_height()

def draw_circular_timer(surface, pos, radius, width, time_left, max_time):
    if time_left < 0:
        time_left = 0
    progress = time_left / max_time
    start_angle, end_angle = math.pi / 2, (math.pi / 2) + (progress * 2 * math.pi)
    rect = pygame.Rect(pos[0] - radius, pos[1] - radius, radius * 2, radius * 2)
    color = RED_COLOR if time_left < 10 else TIMER_FILL_COLOR
    pygame.draw.circle(surface, TIMER_BG_COLOR, pos, radius)
    if progress > 0:
        pygame.draw.arc(surface, color, rect, start_angle, end_angle, width)
    time_text = font.render(str(int(time_left)), True, TEXT_COLOR)
    surface.blit(time_text, time_text.get_rect(center=pos))

def draw_ui(stage_idx, time_left, lives, correct_answers_count):
    if lives_icon:
        screen.blit(lives_icon, (10, screen_width + 2))
        info_text = f"x {lives}   Stage: {stage_idx + 1}   Correct: {correct_answers_count}/{STAGES_COMPLETION_REQUIREMENTS[stage_idx]}"
        # Used a larger font for this text
        info_font = pygame.font.Font(None, WORD_FONT_SIZE + 4)
        screen.blit(info_font.render(info_text, True, TEXT_COLOR), (45, screen_width + 10))
    else:
        info_text = f"Lives: {lives} | Stage: {stage_idx + 1} | Correct: {correct_answers_count}/{STAGES_COMPLETION_REQUIREMENTS[stage_idx]}"
        screen.blit(word_font.render(info_text, True, TEXT_COLOR), (10, screen_width + 5))

    current_question = STAGES_DATA[stage_idx][current_question_index]['question']
    draw_text_wrapped(screen, f"Q: {current_question}", (10, screen_width + 40), question_font, TEXT_COLOR, screen_width - 20)
    draw_circular_timer(screen, (screen_width - 50, screen_height - 50), 40, 8, time_left, QUESTION_TIME_LIMIT)

def draw_selection_line(start_pos, end_pos):
    if start_pos and end_pos:
        start_center = (start_pos[0] * CELL_SIZE + CELL_SIZE // 2, start_pos[1] * CELL_SIZE + CELL_SIZE // 2)
        end_center = (end_pos[0] * CELL_SIZE + CELL_SIZE // 2, end_pos[1] * CELL_SIZE + CELL_SIZE // 2)
        pygame.draw.line(screen, HIGHLIGHT_COLOR, start_center, end_center, 5)

def draw_found_images():
    # This function remains unchanged...
    if not all_colored_images or not found_words_data:
        # fallback: draw colored rectangles for found words
        for found_word in found_words_data:
            word, start_pos, end_pos = found_word['word'], found_word['start_pos'], found_word['end_pos']
            start_row, start_col, end_row, end_col = start_pos[0], start_pos[1], end_pos[0], end_pos[1]
            dr, dc = 0, 0
            if start_row == end_row:
                dc = 1 if end_col > start_col else -1
            elif start_col == end_col:
                dr = 1 if end_row > start_row else -1
            else:
                dr, dc = (1 if end_row > start_row else -1), (1 if end_col > start_col else -1)
            current_row, current_col = start_row, start_col
            for i, letter in enumerate(word):
                rect = pygame.Rect(current_col * CELL_SIZE, current_row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                pygame.draw.rect(screen, FOUND_WORD_COLOR, rect)
                letter_surface = font.render(letter, True, TEXT_COLOR)
                screen.blit(letter_surface, letter_surface.get_rect(center=rect.center))
                current_row += dr; current_col += dc
        return

    for found_word in found_words_data:
        word, start_pos, end_pos = found_word['word'], found_word['start_pos'], found_word['end_pos']
        start_row, start_col, end_row, end_col = start_pos[0], start_pos[1], end_pos[0], end_pos[1]
        dr, dc = 0, 0
        if start_row == end_row:
            dc = 1 if end_col > start_col else -1
        elif start_col == end_col:
            dr = 1 if end_row > start_row else -1
        else:
            dr, dc = (1 if end_row > start_row else -1), (1 if end_col > start_col else -1)
        current_row, current_col = start_row, start_col
        for i, letter in enumerate(word):
            rect = pygame.Rect(current_col * CELL_SIZE, current_row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            # pick a color folder cyclically for variety
            color_idx = (i + len(found_words_data)) % max(1, len(COLOR_ORDER))
            color_name = COLOR_ORDER[color_idx] if COLOR_ORDER else None
            image = all_colored_images.get(color_name, {}).get(letter) if color_name else None
            if image:
                # scale image into tile area
                img = pygame.transform.smoothscale(image, (CELL_SIZE, CELL_SIZE))
                screen.blit(img, rect)
            else:
                pygame.draw.rect(screen, FOUND_WORD_COLOR, rect)
                letter_surface = font.render(letter, True, TEXT_COLOR)
                screen.blit(letter_surface, letter_surface.get_rect(center=tile_rect.center))
            current_row += dr; current_col += dc


def get_word_from_selection(start_pos, end_pos):
    # This function remains unchanged...
    start_row, start_col, end_row, end_col = start_pos[0], start_pos[1], end_pos[0], end_pos[1]
    # Handle single-cell selection
    if start_pos == end_pos:
        return grid[start_row][start_col]

    if start_row == end_row:
        dr, dc = 0, 1 if end_col > start_col else -1
    elif start_col == end_col:
        dr, dc = (1 if end_row > start_row else -1), 0
    elif abs(start_row - end_row) == abs(start_col - end_col):
        dr, dc = (1 if end_row > start_row else -1), (1 if end_col > start_col else -1)
    else:
        return ""
    current_row, current_col, selected_word = start_row, start_col, ""
    while True:
        if not (0 <= current_row < GRID_SIZE and 0 <= current_col < GRID_SIZE):
            break
        selected_word += grid[current_row][current_col]
        if (current_row, current_col) == (end_row, end_col):
            break
        current_row += dr; current_col += dc
    return selected_word


def draw_selected_word_box(word, color):
    # This function remains unchanged...
    box_width = 360
    box_height = 60
    box_y = screen_height - 110
    box_x = (screen_width - box_width) / 2
    box_rect = pygame.Rect(box_x, box_y, box_width, box_height)

    # Draw translucent background surface
    box_surface = pygame.Surface((box_width, box_height), pygame.SRCALPHA)

    # NEW: Solid white background by default for the word selection box
    if color == FOUND_WORD_COLOR:
        border_color = FOUND_WORD_COLOR
        bg_color = (46, 204, 113, 100)
    elif color == RED_COLOR:
        border_color = RED_COLOR
        bg_color = (255, 60, 60, 100)
    else:
        border_color = (100, 100, 100)
        bg_color = (255, 255, 255) # Solid white color

    # Apply transparency to background if not solid white
    if bg_color != (255, 255, 255):
        box_surface.fill(bg_color)
    else:
        box_surface.fill((255, 255, 255, 100)) # Use a semi-transparent white for visual effect
    
    screen.blit(box_surface, (box_x, box_y))
    pygame.draw.rect(screen, border_color, box_rect, 3, 10)

    if not word:
        placeholder = word_font.render("", True, TEXT_COLOR)
        screen.blit(placeholder, placeholder.get_rect(center=box_rect.center))
        return

    # Dynamic font size calculation to fit the word
    if all_colored_images and COLOR_ORDER:
        letters = list(word)
        tile_spacing = 4
        # Calculate maximum possible tile size based on the longest word
        max_letters = len(max([q['answer'] for stage in STAGES_DATA for q in stage], key=len))
        if len(letters) > 0:
            tile_size = min(box_height - 16, int((box_width - (len(letters) - 1) * tile_spacing) / len(letters)))
        else:
            tile_size = box_height - 16
        
        total_tiles_width = len(letters) * tile_size + (len(letters) - 1) * tile_spacing
        start_x = box_x + (box_width - total_tiles_width) / 2
        y = box_y + (box_height - tile_size) / 2
        
        for i, letter in enumerate(letters):
            color_idx = (i + len(found_words_data)) % max(1, len(COLOR_ORDER))
            color_name = COLOR_ORDER[color_idx] if COLOR_ORDER else None
            image = all_colored_images.get(color_name, {}).get(letter) if color_name else None
            tile_rect = pygame.Rect(int(start_x + i * (tile_size + tile_spacing)), int(y), tile_size, tile_size)
            if image:
                img = pygame.transform.smoothscale(image, (tile_size, tile_size))
                screen.blit(img, tile_rect)
            else:
                pygame.draw.rect(screen, (60, 60, 60), tile_rect, border_radius=6)
                letter_surf = font.render(letter, True, TEXT_COLOR)
                screen.blit(letter_surf, letter_surf.get_rect(center=tile_rect.center))
    else:
        # Dynamic font size adjustment for plain text
        word_len = len(word)
        base_font_size = WORD_FONT_SIZE
        max_font_size = WORD_FONT_SIZE
        min_font_size = 12

        # Start with max font size and reduce if the word is too long
        dynamic_font_size = base_font_size
        temp_font = pygame.font.Font(None, dynamic_font_size)
        text_width = temp_font.size(word)[0]
        max_text_width = box_width - 20 # Add some padding

        if text_width > max_text_width:
            dynamic_font_size = int(base_font_size * (max_text_width / text_width))
            if dynamic_font_size < min_font_size:
                dynamic_font_size = min_font_size
        
        scaled_font = pygame.font.Font(None, dynamic_font_size)
        text_surface = scaled_font.render(word, True, color)
        text_rect = text_surface.get_rect(center=box_rect.center)
        screen.blit(text_surface, text_rect)


def show_transition_screen(message):
    overlay = pygame.Surface((screen_width, screen_height)); overlay.fill((0, 0, 0)); overlay.set_alpha(180)
    text_surface = title_font.render(message, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=(screen_width // 2, screen_height // 2))
    screen.blit(overlay, (0, 0)); screen.blit(text_surface, text_rect)
    pygame.display.flip(); pygame.time.wait(2500)

def show_stage_logo(stage_index):
    if stage_index < len(stage_logos) and stage_logos[stage_index]:
        logo_surface = stage_logos[stage_index]
        
        # --- Updated Background for Stage Logo Screen ---
        if menu_background_image:
            screen.blit(menu_background_image, (0, 0))
        else:
            screen.fill(BG_COLOR) # Fallback to original color
            
        screen.blit(logo_surface, logo_surface.get_rect(center=(screen_width // 2, screen_height // 2)))
        pygame.display.flip()
        pygame.time.wait(3000)
    else:
        # Fallback if the stage logo image itself failed to load
        show_transition_screen(f"Stage {stage_index + 1}")

def show_score_board(stage_idx, score):
    global total_questions_taken

    if menu_background_image:
        screen.blit(menu_background_image, (0, 0))
    else:
        screen.fill(BG_COLOR)
        
    score_board_y = screen_height * 0.1
    
    if stage_idx < len(score_board_images) and score_board_images[stage_idx]:
        score_board_image_original = pygame.image.load(SCORE_BOARD_PATHS[stage_idx]).convert_alpha()
        score_board_width = int(screen_width * 0.9)
        score_board_height = int(score_board_image_original.get_height() * (score_board_width / score_board_image_original.get_width()))
        
        score_board_surface = pygame.transform.scale(score_board_image_original, (score_board_width, score_board_height))
        score_board_rect = score_board_surface.get_rect(center=(screen_width // 2, score_board_y + score_board_surface.get_height() // 2))
        screen.blit(score_board_surface, score_board_rect)
        score_board_height = score_board_rect.height
    else:
        overlay = pygame.Surface((int(screen_width * 0.9), int(screen_height * 0.5)))
        overlay.fill((0, 0, 0))
        overlay.set_alpha(180)
        overlay_rect = overlay.get_rect(center=(screen_width // 2, score_board_y + overlay.get_height() // 2))
        screen.blit(overlay, overlay_rect)
        score_board_height = overlay_rect.height
        
        title_surface = title_font.render(f"Stage {stage_idx + 1}", True, (255, 255, 255))
        title_rect = title_surface.get_rect(center=(screen_width // 2, score_board_y + 50))
        screen.blit(title_surface, title_rect)
        
    # --- MODIFIED SECTION ---
    # ✅ Show correct answers out of total questions taken
    # 1. Render the score text to get its size and position
    score_text = score_font.render(f"Score: {score}/{total_questions_taken}", True, TEXT_COLOR)
    score_rect = score_text.get_rect(center=(screen_width // 2, score_board_y + score_board_height + 50))

    # 2. Create a larger rectangle for the box behind the text
    # The inflate method adds padding to all sides.
    score_box_rect = score_rect.inflate(40, 20)

    # 3. Draw the white box with rounded corners first
    pygame.draw.rect(screen, BG_COLOR, score_box_rect, border_radius=10)

    # 4. Draw the score text on top of the box
    screen.blit(score_text, score_rect)
    # --- END MODIFIED SECTION ---
    
    pygame.display.flip()
    pygame.time.wait(3000)

def main_menu():
    global logo_float_time
    try:
        pygame.mixer.music.load('Midterm-Project/Opening_Music.mp3')
        pygame.mixer.music.play(-1)
    except Exception as e:
        print(f"Error loading main menu music: {e}")
    
    logo_float_time = pygame.time.get_ticks()
    button_width, button_height, button_spacing = 200, 50, 20
    buttons_y_start = screen_height * 0.65
    start_button_rect = pygame.Rect((screen_width / 2) - (button_width / 2), buttons_y_start, button_width, button_height)
    quit_button_rect = pygame.Rect((screen_width / 2) - (button_width / 2), buttons_y_start + button_height + button_spacing, button_width, button_height)

    while True:
        logo_y_offset = math.sin(pygame.time.get_ticks() / 500.0) * 10
        
        # --- Updated Menu Background Drawing ---
        if menu_background_image:
            screen.blit(menu_background_image, (0, 0))
        else:
            screen.fill(BG_COLOR) # Fallback to original color
        
        logo_center_y = screen_height * 0.35 + logo_y_offset
        if logo_image:
            screen.blit(logo_image, logo_image.get_rect(center=(screen_width / 2, logo_center_y)))
        else:
            title_surface = title_font.render("Word Search Trivia", True, TEXT_COLOR)
            screen.blit(title_surface, title_surface.get_rect(center=(screen_width / 2, logo_center_y)))
        
        pygame.draw.rect(screen, BUTTON_COLOR, start_button_rect, border_radius=10)
        pygame.draw.rect(screen, BUTTON_COLOR, quit_button_rect, border_radius=10)
        start_text, quit_text = font.render("Start", True, TEXT_COLOR), font.render("Quit", True, TEXT_COLOR)
        screen.blit(start_text, start_text.get_rect(center=start_button_rect.center))
        screen.blit(quit_text, quit_text.get_rect(center=quit_button_rect.center))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.mixer.music.stop(); pygame.quit(); sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mx, my = event.pos
                if start_button_rect.collidepoint((mx, my)):
                    pygame.mixer.music.stop(); show_stage_logo(0); game_loop()
                if quit_button_rect.collidepoint((mx, my)):
                    pygame.mixer.music.stop(); pygame.quit(); sys.exit()
        
        if custom_cursor_image:
            screen.blit(custom_cursor_image, (pygame.mouse.get_pos()[0] - 5, pygame.mouse.get_pos()[1] - 35))
        pygame.display.flip()

def show_game_over_screen(stage_idx, score):
    """Displays the 'Game Over!' message and the final score before returning to the main menu."""
    pygame.mixer.music.stop()
    show_transition_screen("Game Over!")
    show_score_board(stage_idx, score)
    
    # Wait for user input to return to the main menu
    waiting_for_input = True
    while waiting_for_input:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                waiting_for_input = False
            if event.type == pygame.KEYDOWN:
                waiting_for_input = False
        
        # Keep the screen updated during the wait
        pygame.display.flip()
    
    # After input, return to main menu
    main_menu()

def game_loop():
    global is_drawing, mouse_start_pos, mouse_end_pos, champion, current_stage_index, current_question_index, found_words_data, question_start_time, is_paused, pause_end_time, player_lives, selected_word_state, flash_end_time, correct_guess_time, fastest_times_data, is_time_out_triggered, correct_answers_this_stage, questions_used_this_stage

    def start_new_stage(stage_idx):
        global current_question_index, found_words_data, question_start_time, is_time_out_triggered, correct_answers_this_stage, questions_used_this_stage, total_questions_taken
        current_question_index, found_words_data = 0, []
        correct_answers_this_stage = 0
        questions_used_this_stage = []
        total_questions_taken = 0 # BUG FIX: Reset counter for new stage
        
        answers = [item['answer'] for item in STAGES_DATA[stage_idx]]
        generate_grid(answers)
        question_start_time = time.time()
        is_time_out_triggered = False
        
        # Pick a random starting question that has not been used yet
        available_questions = [i for i in range(len(STAGES_DATA[stage_idx])) if i not in questions_used_this_stage]
        if not available_questions:
            # This should not happen if stage completion is less than total questions
            advance_stage()
            return
        current_question_index = random.choice(available_questions)

    def advance_question(bonus_pause=False, failed=False):
        global current_question_index, question_start_time, is_paused, pause_end_time, is_time_out_triggered, selected_word_state, total_questions_taken
        
        total_questions_taken += 1 # BUG FIX: Increment for each question attempted

        # Reset the selected word state
        selected_word_state = {'word': '', 'color': TEXT_COLOR}

        if not failed:
            questions_used_this_stage.append(current_question_index)
        
        available_questions = [i for i in range(len(STAGES_DATA[current_stage_index])) if i not in questions_used_this_stage]
        if not available_questions:
            # If all questions have been used, restart the pool
            questions_used_this_stage.clear()
            available_questions = list(range(len(STAGES_DATA[current_stage_index])))

        current_question_index = random.choice(available_questions)

        if bonus_pause: is_paused, pause_end_time = True, time.time() + PAUSE_DURATION
        question_start_time = time.time()
        is_time_out_triggered = False

    def advance_stage():
        global current_stage_index, champion
        show_score_board(current_stage_index, correct_answers_this_stage)
        show_transition_screen("Stage Complete!")
        current_stage_index += 1
        if current_stage_index >= len(STAGES_DATA):
            champion = True
        else:
            show_stage_logo(current_stage_index)
            start_new_stage(current_stage_index)

    champion, is_paused = False, False
    player_lives = 3
    current_stage_index = 0
    start_new_stage(current_stage_index)
    try:
        pygame.mixer.music.load('Midterm-Project/while_playing.mp3'); pygame.mixer.music.play(-1)
    except Exception as e:
        print(f"Error loading background music: {e}")

    running = True
    while running:
        game_over = player_lives <= 0

        if game_over:
            show_game_over_screen(current_stage_index, correct_answers_this_stage)
            running = False  # End the game loop after showing the game over screen
            continue

        if correct_guess_time and time.time() - correct_guess_time >= 1:
            time_elapsed = correct_guess_time - question_start_time
            if correct_answers_this_stage >= STAGES_COMPLETION_REQUIREMENTS[current_stage_index]:
                advance_stage()
            else:
                advance_question(bonus_pause=(time_elapsed <= BONUS_TIME_THRESHOLD))
            correct_guess_time = 0

        time_left = QUESTION_TIME_LIMIT
        if is_paused:
            if time.time() >= pause_end_time: 
                is_paused = False
                question_start_time = time.time()
                is_time_out_triggered = False
        elif not champion and not game_over:
            time_left = QUESTION_TIME_LIMIT - (time.time() - question_start_time)
            if time_left <= 0:
                if not is_time_out_triggered:
                    if time_out_sound:
                        time_out_sound.play()
                    is_time_out_triggered = True
                
                player_lives -= 1
                advance_question(failed=True) # This is the corrected line to advance the question automatically.

        if time.time() > flash_end_time and selected_word_state['color'] == RED_COLOR:
            selected_word_state['color'] = TEXT_COLOR; selected_word_state['word'] = ''

        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False
            if not champion and not game_over and not is_paused and not correct_guess_time:
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    is_drawing = True; x, y = event.pos
                    if y <= GRID_SIZE * CELL_SIZE:
                        mouse_start_pos, mouse_end_pos = (x // CELL_SIZE, y // CELL_SIZE), (x // CELL_SIZE, y // CELL_SIZE)
                if event.type == pygame.MOUSEMOTION and is_drawing:
                    x, y = event.pos
                    if y <= GRID_SIZE * CELL_SIZE and mouse_start_pos is not None:
                        mouse_end_pos = (x // CELL_SIZE, y // CELL_SIZE)
                        selected_word = get_word_from_selection((mouse_start_pos[1], mouse_start_pos[0]), (mouse_end_pos[1], mouse_end_pos[0]))
                        selected_word_state['word'] = selected_word; selected_word_state['color'] = TEXT_COLOR
                if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    is_drawing = False
                    if mouse_start_pos and mouse_end_pos:
                        start_pos_rev, end_pos_rev = (mouse_start_pos[1], mouse_start_pos[0]), (mouse_end_pos[1], mouse_end_pos[0])
                        selected_word = get_word_from_selection(start_pos_rev, end_pos_rev)
                        if mouse_start_pos == mouse_end_pos or selected_word == "":
                            # Removed player_lives -= 1
                            selected_word_state.update({'word': selected_word, 'color': RED_COLOR})
                            flash_end_time = time.time() + 1
                            # Deduct 5 seconds for wrong guess
                            question_start_time -= 5
                        else:
                            correct_answer = STAGES_DATA[current_stage_index][current_question_index]['answer']
                            selected_word_state['word'] = selected_word
                            already_found = any(data['word'] == correct_answer for data in found_words_data)
                            if not already_found and (selected_word == correct_answer or selected_word[::-1] == correct_answer):
                                # ✅ Correct answer
                                selected_word_state.update({'word': correct_answer, 'color': FOUND_WORD_COLOR})
                                correct_guess_time = time.time()
                                correct_answers_this_stage += 1
                                
                                # --- Record Fastest Time ---
                                time_elapsed = correct_guess_time - question_start_time
                                current_fastest = fastest_times_data['stages'][current_stage_index]['questions'][current_question_index]['fastest_time_seconds']
                                
                                if current_fastest is None or time_elapsed < current_fastest:
                                    record = fastest_times_data['stages'][current_stage_index]['questions'][current_question_index]
                                    record['fastest_time_seconds'] = time_elapsed
                                    record['completion_date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                                    save_fastest_times(fastest_times_data)
                                    print(f"New fastest time for Q{current_question_index+1} in Stage {current_stage_index+1}: {time_elapsed:.2f}s")

                                if correct_word_sound: correct_word_sound.play()
                                start_pos = start_pos_rev if selected_word == correct_answer else end_pos_rev
                                end_pos = end_pos_rev if selected_word == correct_answer else start_pos_rev
                                found_words_data.append({'word': correct_answer, 'start_pos': start_pos, 'end_pos': end_pos})
                            else:
                                # Removed player_lives -= 1
                                selected_word_state['color'] = RED_COLOR
                                flash_end_time = time.time() + 1
                                # Deduct 5 seconds for wrong guess
                                question_start_time -= 5
                    mouse_start_pos, mouse_end_pos = None, None

        bg_index = current_stage_index % len(stage_backgrounds)
        if stage_backgrounds and bg_index < len(stage_backgrounds) and stage_backgrounds[bg_index]:
            screen.blit(stage_backgrounds[bg_index], (0, 0))
        else:
            screen.fill(BG_COLOR)
        draw_grid(); draw_found_images()

        if champion:
            win_text = title_font.render("CHAMPION!", True, FOUND_WORD_COLOR)
            screen.blit(win_text, win_text.get_rect(center=(screen_width / 2, screen_height / 2)))
        else:
            draw_ui(current_stage_index, time_left, player_lives, correct_answers_this_stage)
            if is_drawing and mouse_start_pos and mouse_end_pos: draw_selection_line(mouse_start_pos, mouse_end_pos)
            if is_paused:
                bonus_text = title_font.render("TIME FREEZE!", True, GOLD_COLOR)
                screen.blit(bonus_text, bonus_text.get_rect(center=(screen_width / 2, screen_height / 2)))
            draw_selected_word_box(selected_word_state['word'], selected_word_state['color'])

        if custom_cursor_image:
            screen.blit(custom_cursor_image, (pygame.mouse.get_pos()[0] - 5, pygame.mouse.get_pos()[1] - 35))
        pygame.display.flip()

    pygame.mixer.music.stop()
    main_menu()

if __name__ == "__main__":
    load_background_images()
    load_letter_images()
    load_stage_logos()
    load_score_board_images()
    fastest_times_data = load_or_create_fastest_times()
    
    # --- Load Main Menu Background ---
    try:
        menu_background_image_original = pygame.image.load(MENU_BACKGROUND_PATH).convert()
        menu_background_image = pygame.transform.scale(menu_background_image_original, (screen_width, screen_height))
        print(f"Successfully loaded menu background: {MENU_BACKGROUND_PATH}")
    except Exception as e:
        print(f"Error loading menu background image: {e}")
        menu_background_image = None
    
    # --- New: Load Time Out Sound ---
    try:
        time_out_sound = pygame.mixer.Sound('Midterm-Project/break_glass.mp3')
        print("Successfully loaded time out sound effect.")
    except Exception as e:
        print(f"Error loading time out sound: {e}")
        time_out_sound = None

    main_menu()