import pygame
from pygame import mixer
from sys import exit
from pygame.locals import MOUSEBUTTONDOWN

class HarmonyKitchen:
    """A class including everything that is needed to play HARMONY KITCHEN"""
    def __init__(self):
        pygame.init()
        mixer.init()
        
        # Basics
        self.screen = pygame.display.set_mode((1500,900), pygame.RESIZABLE)
        pygame.display.set_caption("HARMONY KITCHEN")
        self.clock = pygame.time.Clock() 

        # Music & sounds                                                                                        
        mixer.music.load("music/music.mp3")
        pygame.mixer.music.set_volume(0.25)
        mixer.music.play(-1)       # Music plays until the game closes
        self.cutting_sound = pygame.mixer.Sound("music/cutting.mp3")
        self.frying_sound = pygame.mixer.Sound("music/frying.mp3")
        self.mixing_sound = pygame.mixer.Sound("music/mixing.mp3")
        
        # Fonts
        self.font = pygame.font.Font("font/VCR_OSD_Mono.ttf", 100)
        self.font_small = pygame.font.Font("font/VCR_OSD_Mono.ttf", 40)
        self.font_smaller = pygame.font.Font("font/VCR_OSD_Mono.ttf", 25)
        self.font_smallest = pygame.font.Font("font/VCR_OSD_Mono.ttf", 20)

        # Title screen 
        self.title_screen = pygame.Surface((1500,900))
        self.title_screen.fill((255, 234, 222))
        self.game_title = self.font.render("HARMONY KITCHEN", True, (83,15,57)) 
        self.start_text = self.font_small.render("Press SPACE to start", True, (83,15,57))
        self.space_pressed = False

        self.screen.blit(self.title_screen,(0,0))
        self.screen.blit(self.game_title,(300,300))
        self.screen.blit(self.start_text,(480,420))
        pygame.display.flip()
        
        # Kitchen
        self.kitchen_background = pygame.image.load("images/kitchen.jpg")
        self.kitchen_background = pygame.transform.scale(self.kitchen_background, (1500, 900))
        self.obstacle_top_left_rect = pygame.Rect(0, 0, 700, 180)
        self.obstacle_left_rect = pygame.Rect(-100, 0, 10, 900)
        self.obstacle_top_right_rect = pygame.Rect(1300, 0, 300, 300)
        self.obstacle_right_rect = pygame.Rect(1450, 0, 200, 900)
        self.obstacle_bottom = pygame.Rect(0, 900, 1000, 1)
        
        # Character 
        self.portrait = pygame.image.load("images/portrait.png")
        self.portrait = pygame.transform.scale_by(self.portrait, 2)
        self.character_front = pygame.image.load("images/front.png")
        self.character_front = pygame.transform.scale_by(self.character_front, 2)
        self.character_back = pygame.image.load("images/back.png")
        self.character_back = pygame.transform.scale_by(self.character_back, 2)
        self.character_right = pygame.image.load("images/right.png")
        self.character_right = pygame.transform.scale_by(self.character_right, 2)
        self.character_left = pygame.image.load("images/left.png")
        self.character_left = pygame.transform.scale_by(self.character_left, 2)
        self.character_position = [100, 300]
        self.prev_character_position = self.character_position.copy()
        self.character_speed = 5
        self.character_rect = pygame.Rect(
            self.character_position[0],
            self.character_position[1],
            self.character_front.get_width(),
            self.character_front.get_height())
        
        # Beginning instructions
        self.speech_bubble = pygame.image.load("images/speech.png")
        self.speech_bubble = pygame.transform.flip(self.speech_bubble, True, False)
        self.start_text1 = self.font_small.render("Welcome to HARMONY KITCHEN!", True, (83,15,57))
        self.instruction = self.font_smallest.render("Click on the arrow to continue", True, (83,15,57))
        self.text = ['"Cooking is love made visible"',
                'This mini-game embraces exactly that.',
                'The goal is to promote cultural exchange,...',
                'overcoming barriers,...',
                'further understanding...',
                'and ultimately peace through the shared love of food.',
                'You can move around in the cozy environment,...',
                'look at the recipe book...',
                'and also interactively cook dishes.',
                'Just use the arrow keys to move around.',
                'And click on the recipe book to look at recipes...',
                'and start the mini games!',
                'Enjoy your stay at HARMONY KITCHEN!']
        self.text_index = 0

        # Basic interactive buttons
        self.arrow = pygame.image.load("images/arrow.png")
        self.arrow = pygame.transform.scale_by(self.arrow, 1.5)
        self.arrow_info_rect = self.arrow.get_rect(topleft=(1180,320))
        self.arrow_rect = self.arrow.get_rect(topleft=(1085,550))
        self.arrow_rect2 = self.arrow.get_rect(topleft=(1300,600))
        self.arrow_rect3 = self.arrow.get_rect(topleft=(1320,630))
        self.arrow2 = pygame.transform.flip(self.arrow, True, False)
        self.arrow2_rect = self.arrow2.get_rect(topleft=(170,550))
        self.x = pygame.image.load("images/x.png")
        self.x = pygame.transform.scale_by(self.x, 0.5)
        self.x_rect = pygame.Rect(0, 0, 100, 100)
        
        # Recipe book
        self.book = pygame.image.load("images/book.png")
        self.book = pygame.transform.scale_by(self.book, 0.25)
        self.book_rect = self.book.get_rect(topleft=(30, 400))
        self.book_open = pygame.image.load("images/book_open.png")
        self.book_open = pygame.transform.scale_by(self.book_open, 2.25)
        self.recipe1 = pygame.image.load("images/recipe1.png")
        self.recipe1 = pygame.transform.scale_by(self.recipe1, 0.35)
        self.recipe2 = pygame.image.load("images/recipe2.png")
        self.recipe2 = pygame.transform.scale_by(self.recipe2, 0.35)
        self.recipe3 = pygame.image.load("images/recipe3.png")
        self.recipe3 = pygame.transform.scale_by(self.recipe3, 0.5)
        self.soon = pygame.image.load("images/soon.png")
        self.soon = pygame.transform.scale_by(self.soon, 0.5) 
        self.cooking_button1 = pygame.image.load("images/cooking_button.png")
        self.cooking_button1 = pygame.transform.scale_by(self.cooking_button1, 0.35)
        self.cooking_button1_rect = self.cooking_button1.get_rect(topleft=(350,500))
        self.cooking_button2 = pygame.image.load("images/cooking_button.png")
        self.cooking_button2 = pygame.transform.scale_by(self.cooking_button2, 0.35)
        self.cooking_button2_rect = self.cooking_button2.get_rect(topleft=(850,500))
        self.cooking_button3 = pygame.image.load("images/cooking_button.png")
        self.cooking_button3 = pygame.transform.scale_by(self.cooking_button3, 0.35)
        self.cooking_button3_rect = self.cooking_button3.get_rect(topleft=(350,500))
        self.covering_rect = pygame.Rect(750, 200, 400, 400)
        self.covering_rect2 = pygame.Rect(1120, 644, 50, 30)
        self.covering_rect3 = pygame.Rect(100, 100, 200, 200)
        
        self.book_opened = False
        self.display_first_recipes = True
        self.display_recipe3 = False
        
        # Cooking game basics
        self.kitchen_surface = pygame.Surface((1500,900)) 
        self.kitchen_surface.fill((236, 234, 230))
        self.recipe_display_surface = pygame.Surface((1500, 900))
        self.recipe_display_surface.fill((255, 235, 247))
        self.finished_cooking = self.font_small.render("GOOD JOB! ENJOY YOUR FOOD!", True, (83,15,57))
        self.cutting_board = pygame.image.load("images/cutting_board.png")
        self.cutting_speed = 10
        self.bowl = pygame.image.load("images/bowl.png")
        self.bowl = pygame.transform.scale_by(self.bowl, 1.25)
        self.bowl_rect = self.bowl.get_rect(topleft=(400,150))
        self.bowl_rect2 = self.bowl.get_rect(topleft=(700,150))
        self.bowl_rect3 = self.bowl.get_rect(topleft=(50,150))
        self.bowl_original = pygame.image.load("images/bowl.png")
        self.bowl_original = pygame.transform.scale_by(self.bowl_original, 1.25)
        self.pan = pygame.image.load("images/pan.png")
        self.pan = pygame.transform.scale_by(self.pan, 3)
        self.pan_rect = self.pan.get_rect(topleft=(400,100))
        
        # Recipe 1
        self.tomato = pygame.image.load("images/tomato.png")
        self.tomato = pygame.transform.scale_by(self.tomato, 0.6)
        self.tomato_original = pygame.image.load("images/tomato.png")
        self.tomato_original = pygame.transform.scale_by(self.tomato_original, 0.6)
        self.tomato_rect = pygame.Rect(0, 80, 350, 300)
        self.chopped_tomato_rect = pygame.Rect(50, 70, 150, 150)
        self.tomato_position = [100, -80]
        self.garlic = pygame.image.load("images/garlic.png")
        self.garlic = pygame.transform.scale_by(self.garlic, 0.25)
        self.garlic_original = pygame.image.load("images/garlic.png")
        self.garlic_original = pygame.transform.scale_by(self.garlic_original, 0.25)
        self.garlic_rect = pygame.Rect(10, 400, 300, 300)
        self.chopped_garlic_rect = pygame.Rect(50, 200, 150, 150)
        self.garlic_position = [300, 250]
        self.basil = pygame.image.load("images/basil.png")
        self.basil = pygame.transform.scale_by(self.basil, 0.25)
        self.basil_rect = pygame.Rect(50, 300, 150, 150)
        self.seasonings = pygame.image.load("images/seasonings.png")
        self.seasonings = pygame.transform.scale_by(self.seasonings, 0.25)
        self.seasonings_rect = pygame.Rect(50, 440, 150, 150)
        self.olive_oil = pygame.image.load("images/olive_oil.png")
        self.olive_oil = pygame.transform.scale_by(self.olive_oil, 0.25)
        self.olive_oil_rect = pygame.Rect(50, 610, 150, 150)
        self.bruschetta_mixed = pygame.image.load("images/bruschetta_mixed.png")
        self.bruschetta_mixed = pygame.transform.scale_by(self.bruschetta_mixed, 0.6)
        self.bruschetta_served = pygame.image.load("images/bruschetta_served.png")
        self.bruschetta_served = pygame.transform.scale_by(self.bruschetta_served, 0.85)
        
        self.making_recipe1 = False
        self.recipe1_step1 = False
        self.recipe1_step2 = False
        self.tomato_selected = False
        self.tomato_done = False
        self.garlic_selected = False
        self.chopped_tomato_added = False
        self.chopped_garlic_added = False
        self.basil_added = False
        self.seasonings_added = False
        self.olive_oil_added = False
        self.ingredients_mixed = False
        
        # Recipe 2
        self.cauliflower = pygame.image.load("images/cauliflower.png")
        self.cauliflower = pygame.transform.scale_by(self.cauliflower, 0.6)
        self.cauliflower_original = pygame.image.load("images/cauliflower.png")
        self.cauliflower_original = pygame.transform.scale_by(self.cauliflower_original, 0.6)
        self.cauliflower_rect = self.cauliflower.get_rect(topleft=(10,150))
        self.chopped_cauliflower_rect = pygame.Rect(20, 70, 170, 160)
        self.cauliflower_position = [350, 280]
        self.tofu = pygame.image.load("images/tofu.png")
        self.tofu = pygame.transform.scale_by(self.tofu, 0.6)
        self.tofu_original = pygame.image.load("images/tofu.png")
        self.tofu_original = pygame.transform.scale_by(self.tofu_original, 0.6)
        self.tofu_rect = self.tofu.get_rect(topleft=(10,400))
        self.chopped_tofu_rect = pygame.Rect(20, 230, 170, 150)
        self.tofu_position = [350, 280]
        self.cauliflower_tofu = pygame.image.load("images/cauliflower_tofu.png")
        self.cauliflower_tofu = pygame.transform.scale_by(self.cauliflower_tofu, 1.25)
        self.coconut_milk = pygame.image.load("images/coconut_milk.png")
        self.coconut_milk = pygame.transform.scale_by(self.coconut_milk, 0.75)
        self.coconut_milk_rect = self.coconut_milk.get_rect(topleft=(30,580))
        self.coconut_milk_liquid = pygame.image.load("images/coconut_milk_liquid.png")
        self.coconut_milk_liquid = pygame.transform.scale_by(self.coconut_milk_liquid, 3)
        self.spices = pygame.image.load("images/spices.png")
        self.spices = pygame.transform.scale_by(self.spices, 0.4)
        self.spices_rect = self.spices.get_rect(topleft=(30,400))
        self.spices_loose = pygame.image.load("images/spices_loose.png")
        self.spices_mixed = pygame.image.load("images/spices_mixed.png")
        self.spices_mixed = pygame.transform.scale_by(self.spices_mixed, 3)
        self.curry_served = pygame.image.load("images/curry_served.png")
        
        self.making_recipe2 = False
        self.recipe2_step1 = False
        self.cauliflower_selected = False
        self.cauliflower_done = False
        self.tofu_selected = False
        self.chopped_cauliflower_added = False
        self.chopped_tofu_added = False
        self.coconut_milk_added = False
        self.spices_added = False
        
        # Recipe 3
        self.flour = pygame.image.load("images/flour.png")
        self.flour_rect = pygame.Rect(50,100, 150, 190)
        self.sugar = pygame.image.load("images/sugar.png")
        self.sugar_rect = pygame.Rect(50,280, 150, 190)
        self.baking_powder = pygame.image.load("images/baking_powder.png")
        self.baking_powder = pygame.transform.scale_by(self.baking_powder, 0.5)
        self.baking_powder_rect = pygame.Rect(50,450, 150, 150)
        self.salt_rect = pygame.Rect(50, 600, 150, 150)
        self.dry_ingredients = pygame.image.load("images/dry_ingredients.png")
        self.dry_ingredients = pygame.transform.scale_by(self.dry_ingredients, 1.25)
        self.milk = pygame.image.load("images/milk.png")
        self.milk = pygame.transform.scale_by(self.milk, 0.75)
        self.milk_rect = pygame.Rect(30, 100, 200, 250)
        self.milk_liquid = pygame.image.load("images/milk_liquid.png")
        self.milk_liquid = pygame.transform.scale_by(self.milk_liquid, 1.25)
        self.vinegar = pygame.image.load("images/vinegar.png")
        self.vinegar = pygame.transform.scale_by(self.vinegar, 0.5)
        self.vinegar_rect = pygame.Rect(50, 350, 150, 250)
        self.vinegar_liquid = pygame.image.load("images/vinegar_liquid.png")
        self.vinegar_liquid = pygame.transform.scale_by(self.vinegar_liquid, 1.25)
        self.vanilla = pygame.image.load("images/vanilla.png")
        self.vanilla = pygame.transform.scale_by(self.vanilla, 0.75)
        self.vanilla_rect = pygame.Rect(40, 560, 150, 200)
        self.vanilla_liquid = pygame.image.load("images/vanilla_liquid.png")
        self.vanilla_liquid = pygame.transform.scale_by(self.vanilla_liquid, 1.25)
        self.liquid_ingredients = pygame.image.load("images/liquid_ingredients.png")
        self.liquid_ingredients = pygame.transform.scale_by(self.liquid_ingredients, 1.25)
        self.pancake_raw = pygame.image.load("images/pancake_raw.png")
        self.pancake_raw = pygame.transform.scale_by(self.pancake_raw, 1.5)
        self.pancake_raw_rect = self.pancake_raw.get_rect(topleft=(600,300))
        self.pancake = pygame.image.load("images/pancake.png")
        self.pancake = pygame.transform.scale_by(self.pancake, 1.5)
        self.pancake_rect = self.pancake.get_rect(topleft=(600,300))
        self.pancakes_served = pygame.image.load("images/pancakes_served.png")

        self.making_recipe3 = False
        self.recipe3_step1 = False
        self.recipe3_step2 = False
        self.recipe3_step3 = False
        self.recipe3_step4 = False
        self.recipe3_step5 = False
        self.flour_added = False
        self.sugar_added = False
        self.baking_powder_added = False
        self.milk_added = False
        self.vinegar_added = False
        self.vanilla_added = False
        self.display_bowls = False
        self.liquid_ingredients_done = False
        self.bowls_prepared = False
        self.bowls_combind = False
        self.pan_prepared = False
        self.pancake_frying = False
        self.pancake_ready = False
        self.pancake_done = False
        
        # Minigame instructions
        self.instruction_cutting = self.font_smallest.render(
            "Click on the ingredient to select it. Then press the SPACE key to cut it.",
            True, (83,15,57))
        self.instruction_adding_mixing = self.font_smallest.render(
            "Click on the ingredient to add it to the bowl. Then click on the bowl to mix everything.",
            True, (83,15,57))
        self.instruction_adding = self.font_smallest.render(
            "Click on the ingredient to add it to the bowl.",
            True, (83,15,57))
        self.instruction_frying = self.font_smallest.render(
            "Click on the ingredient to add it to the pan. Then click on the pan to stir.",
            True, (83,15,57))
        self.instruction_bowl = self.font_smallest.render(
            "Click on the right bowl to add it's mixture into the other.",
            True, (83,15,57))
        self.instruction_frying_flipping = self.font_smallest.render(
            "Click on the bowl to add the batter into the pan. Then click on the pancake to flip it and remove it.",
            True, (83,15,57))
 
        # Future ideas
        self.future_features = pygame.image.load("images/future_features.png")
        self.future_features = pygame.transform.scale_by(self.future_features, 0.5)
        self.background_rect = pygame.Rect(250,50,950,680)
        self.display_future_features = False

        # Cat
        self.cat_rect = pygame.Rect(-100,600,10,90)
        self.meow = self.font_small.render("Meow!", True, (83,15,57))
        self.cat_speech_bubble = pygame.image.load("images/speech.png")
        self.cat_speech_bubble = pygame.transform.flip(self.cat_speech_bubble, True, False)
        self.cat_speech_bubble = pygame.transform.scale_by(self.cat_speech_bubble, 0.3)

        
    def start_game(self):
        """Starts the game loop, initializes functions and handels events in the main kitchen environment"""
        
        self.playing = True

        while self.playing:
            self.kitchen()
            self.recipe_book()
            self.future_ideas()
            self.reset_images()
            self.cat()

            self.clock.tick(60) 
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:        # Close the pygame window
                    pygame.quit()
                    mixer.quit()
                    exit()
                    
                elif (event.type == pygame.KEYDOWN
                      and event.key == pygame.K_SPACE
                      and not self.space_pressed): 
                    self.space_pressed = True        # This boolean is needed so pressing the space key again wont do anything 
                    self.screen.blit(self.kitchen_background, (0,0))
                    self.screen.blit(self.book, (30, 400))
                    self.screen.blit(self.portrait, (-50,300))
                    self.screen.blit(self.speech_bubble, (350, 250))
                    self.screen.blit(self.arrow, (1180, 320))
                    self.screen.blit(self.start_text1, (450, 350))
                    self.screen.blit(self.instruction, (450, 420))
                    pygame.display.flip()
                        
                # Display the info text
                elif event.type == MOUSEBUTTONDOWN: 
                    if self.arrow_info_rect.collidepoint(event.pos):        # Click on the arrow to continue
                        if self.text_index < len(self.text):
                            pygame.draw.rect(self.screen, (255, 255, 255), (450, 350, 850, 40))
                            rendered_line = self.font_smaller.render(self.text[self.text_index], True, (83, 15, 57))
                            self.screen.blit(rendered_line, (450, 350))
                            pygame.display.flip()
                            self.text_index = self.text_index+1
                                
                        # Finish reading the info text and display the main kitchen environment      
                        else:
                            self.screen.blit(self.kitchen_background, (0,0))
                            self.screen.blit(self.book, (30, 400))
                            self.screen.blit(self.arrow, (1320, 630))
                            self.screen.blit(self.character_front, (100,300))
                            pygame.display.flip()
                            self.kitchen()
                        
                        
                    # Click on the recipe book to display it 
                    elif self.book_rect.collidepoint(event.pos):
                        if not self.book_opened:
                            self.book_opened = True
                            self.recipe_book()
                            
                    # Click on the arrow to diplay future ideas 
                    elif self.arrow_rect3.collidepoint(event.pos):
                        if not self.display_future_features:
                            self.display_future_features = True
                            self.future_ideas()

                            
    def kitchen(self):
        """A function enabling the character to move around in the kitchen and stopping it from leaving the screen"""

        key = pygame.key.get_pressed()
        self.prev_character_position = self.character_position.copy()
        
        if key[pygame.K_RIGHT]:
            self.character_position[0] = self.character_position[0] + self.character_speed
            self.screen.blit(self.kitchen_background, (0,0))
            self.screen.blit(self.book, (30, 400))
            self.screen.blit(self.arrow, (1320, 630))
            self.screen.blit(self.character_right, self.character_position)
            pygame.display.flip()
            
        elif key[pygame.K_LEFT]:
            self.character_position[0] = self.character_position[0] - self.character_speed
            self.screen.blit(self.kitchen_background, (0,0))
            self.screen.blit(self.arrow, (1320, 630))
            self.screen.blit(self.book, (30, 400))
            self.screen.blit(self.character_left, self.character_position)
            pygame.display.flip()


        elif key[pygame.K_UP]:
            self.character_position[1] = self.character_position[1] - self.character_speed
            self.screen.blit(self.kitchen_background, (0,0))
            self.screen.blit(self.book, (30, 400))
            self.screen.blit(self.arrow, (1320, 630))
            self.screen.blit(self.character_back, self.character_position)
            pygame.display.flip()


        elif key[pygame.K_DOWN]:
            self.character_position[1] = self.character_position[1] + self.character_speed
            self.screen.blit(self.kitchen_background, (0,0))
            self.screen.blit(self.book, (30, 400))
            self.screen.blit(self.arrow, (1320, 630))
            self.screen.blit(self.character_front, self.character_position)
            pygame.display.flip()


        # Stop the character from moving when it is colliding with obstacles
        self.character_rect.topleft = self.character_position 
        if self.character_rect.colliderect(self.obstacle_top_right_rect):
            self.character_position = self.prev_character_position.copy()
            self.screen.blit(self.kitchen_background, (0, 0))
            self.screen.blit(self.book, (30, 400))
            self.screen.blit(self.arrow, (1320, 630))
            self.screen.blit(self.character_right, self.character_position)
            pygame.display.flip()


        elif self.character_rect.colliderect(self.obstacle_right_rect):
            self.character_position = self.prev_character_position.copy()
            self.screen.blit(self.kitchen_background, (0, 0))
            self.screen.blit(self.book, (30, 400))
            self.screen.blit(self.arrow, (1320, 630))
            self.screen.blit(self.character_right, self.character_position)
            pygame.display.flip()

        elif self.character_rect.colliderect(self.obstacle_left_rect):
            self.character_position = self.prev_character_position.copy()
            self.screen.blit(self.kitchen_background, (0, 0))
            self.screen.blit(self.book, (30, 400))
            self.screen.blit(self.arrow, (1320, 630))
            self.screen.blit(self.character_left, self.character_position)
            pygame.display.flip()

        elif self.character_rect.colliderect(self.obstacle_top_left_rect):
            self.character_position = self.prev_character_position.copy()
            self.screen.blit(self.kitchen_background, (0, 0))
            self.screen.blit(self.book, (30, 400))
            self.screen.blit(self.arrow, (1320, 630))
            self.screen.blit(self.character_back, self.character_position)
            pygame.display.flip()

        elif self.character_rect.colliderect(self.obstacle_bottom):
            self.character_position = self.prev_character_position.copy()
            self.screen.blit(self.kitchen_background, (0, 0))
            self.screen.blit(self.book, (30, 400))
            self.screen.blit(self.arrow, (1320, 630))
            self.screen.blit(self.character_front, self.character_position)
            pygame.display.flip()


    def recipe_book(self):
        """A function handling the viewing of the recipe book and cooking of recipes"""
        
        if self.book_opened:
            self.screen.blit(self.title_screen,(0,0))
            self.screen.blit(self.book_open, (-400,-1260))
            self.screen.blit(self.cooking_button1, (350, 500))
            self.screen.blit(self.cooking_button2, (850, 500))
            self.screen.blit(self.arrow, (1085, 550))
            self.screen.blit(self.x, (-70,-50))

            if self.display_first_recipes: 
                self.screen.blit(self.recipe1, (250,100))
                self.screen.blit(self.cooking_button1, (350, 500))
                self.screen.blit(self.recipe2, (750,100))
                self.screen.blit(self.cooking_button2, (850, 500))
                self.display_recipe3 = False
                pygame.display.flip()

            
        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN: 
                if self.x_rect.collidepoint(event.pos):        # Click on x to close the recipe book
                    self.screen.blit(self.kitchen_background, (0,0))
                    self.screen.blit(self.book, (30, 400))
                    self.screen.blit(self.arrow, (1320, 630))
                    self.screen.blit(self.character_front, (100,300))
                    pygame.display.flip()
                    self.kitchen()
                    self.book_opened = False
                    self.display_first_recipes = True
                    
                elif (self.arrow_rect.collidepoint(event.pos)
                      and self.display_first_recipes):        # Flip the page around
                    self.screen.blit(self.recipe3, (250,100))
                    self.screen.blit(self.cooking_button3, (350, 500))
                    pygame.draw.rect(self.screen, (255, 255, 255), self.covering_rect)
                    self.screen.blit(self.soon, (750,100))
                    self.screen.blit(self.arrow2, (170, 550))
                    pygame.draw.rect(self.screen, (255, 255, 255), self.covering_rect2) 
                    self.display_first_recipes = False
                    pygame.display.flip()
                    self.display_recipe3 = True

                elif (self.arrow2_rect.collidepoint(event.pos)
                      and self.display_recipe3):        # Flip back to the first pages 
                    self.screen.blit(self.recipe1, (250,100))
                    self.screen.blit(self.recipe2, (750,100))
                    pygame.display.flip()
                    self.display_recipe3 = False
                    self.display_first_recipes = True
                    
                elif (self.cooking_button1_rect.collidepoint(event.pos)
                      and self.display_first_recipes):        # Display the start for recipe 1
                    self.screen.blit(self.kitchen_surface, (0,0))
                    self.screen.blit(self.x, (-70,-50))
                    self.screen.blit(self.cutting_board, (-250, -280))
                    self.screen.blit(self.tomato, (-310, -200))
                    self.screen.blit(self.garlic, (-100, 400))
                    self.screen.blit(self.instruction_cutting, (100, 20))
                    pygame.display.flip()
                    self.display_first_recipes = False
                    self.making_recipe1 = True
                    self.recipe1_step1 = True
                    
                elif self.cooking_button2_rect.collidepoint(event.pos):        # Display the start for recipe 2 
                    self.screen.blit(self.kitchen_surface, (0,0))
                    self.screen.blit(self.x, (-70,-50))
                    self.screen.blit(self.cutting_board, (-250, -280))
                    self.screen.blit(self.cauliflower, (10, 150))
                    self.screen.blit(self.tofu, (10, 400))
                    self.screen.blit(self.instruction_cutting, (100, 20))
                    pygame.display.flip()
                    self.display_first_recipes = False
                    self.making_recipe2 = True
                    self.recipe2_step1 = True

                elif (self.cooking_button3_rect.collidepoint(event.pos)
                      and self.display_recipe3):        # Display the start for recipe 3 
                    self.screen.blit(self.kitchen_surface, (0,0))
                    self.screen.blit(self.x, (-70,-50))
                    self.screen.blit(self.instruction_adding, (100, 20))
                    self.screen.blit(self.bowl, (400, 150))
                    self.screen.blit(self.flour, (30, 100))
                    self.screen.blit(self.sugar, (30, 280))
                    self.screen.blit(self.baking_powder, (50, 450))
                    self.screen.blit(self.seasonings, (-110, 480))
                    pygame.display.flip()
                    self.display_recipe3 = False
                    self.making_recipe3 = True
                    self.recipe3_step1 = True

                
        # Making recipe1
        # I wanted to put this in a function but there were so many problems
        #(including a really long delay in clicking or not detecting the mouseclick at all)
        # I didnt manage to solve in time so I had to choose this uglier but working way 
        tomato_chop_position = 200
        garlic_chop_position = 550
        while self.making_recipe1:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if self.x_rect.collidepoint(event.pos):        # Click on x to leave the cooking process of recipe 1
                        self.screen.blit(self.kitchen_background, (0,0))
                        self.screen.blit(self.book, (30, 400))
                        self.screen.blit(self.character_front, (100,300))
                        pygame.display.flip()
                        self.kitchen()
                        self.making_recipe1 = False
                        self.display_first_recipes = True
                        self.book_opened = False
                         
                    elif (self.tomato_rect.collidepoint(event.pos)
                          and self.recipe1_step1):        # Click on the tomato to put it on the cutting board
                        pygame.draw.rect(self.screen, (236, 234, 230), self.tomato_rect)
                        self.screen.blit(self.tomato, (100, -80))
                        pygame.display.flip()
                        self.tomato_selected = True

                    elif (self.garlic_rect.collidepoint(event.pos)
                          and self.recipe1_step1
                          and self.tomato_done):        # Click on the garlic to put it on the cutting board
                        pygame.draw.rect(self.screen, (236, 234, 230), self.garlic_rect)
                        self.screen.blit(self.garlic, (300, 250))
                        pygame.display.flip()
                        self.garlic_selected = True

                    elif (self.arrow_rect2.collidepoint(event.pos)
                          and self.recipe1_step2):        # Click on the arrow to get to the next step in the cooking process
                        self.screen.blit(self.kitchen_surface, (0,0))
                        self.screen.blit(self.x, (-70,-50))
                        self.screen.blit(self.instruction_adding_mixing, (100, 20))
                        self.screen.blit(self.bowl, (400, 150))
                        self.tomato = pygame.transform.scale_by(self.tomato, 0.6)
                        self.screen.blit(self.tomato, (-20, 30))
                        self.garlic = pygame.transform.scale_by(self.garlic, 0.6)
                        self.screen.blit(self.garlic, (10, 160))
                        self.screen.blit(self.basil, (-130, 210))
                        self.screen.blit(self.seasonings, (-110, 330))
                        self.screen.blit(self.olive_oil, (-20, 510))
                        pygame.display.flip()
                        

                    elif (self.chopped_tomato_rect.collidepoint(event.pos)
                          and self.recipe1_step2):        # Click on the tomato to add it to the bowl
                        pygame.draw.rect(self.screen, (236, 234, 230), self.chopped_tomato_rect)
                        self.tomato = pygame.transform.scale_by(self.tomato, 2)
                        self.screen.blit(self.tomato, (350, 200))
                        pygame.display.flip()
                        self.chopped_tomato_added = True
                        
                    elif (self.chopped_garlic_rect.collidepoint(event.pos)
                          and self.recipe1_step2
                          and self.chopped_tomato_added):        # Click on the garlic to add it to the bowl 
                        pygame.draw.rect(self.screen, (236, 234, 230), self.chopped_garlic_rect)
                        self.screen.blit(self.garlic, (550, 300))
                        pygame.display.flip()
                        self.chopped_garlic_added = True

                    elif (self.basil_rect.collidepoint(event.pos)
                          and self.recipe1_step2
                          and self.chopped_garlic_added):        # Click on the basil to add it to the bowl 
                        pygame.draw.rect(self.screen, (236, 234, 230), self.basil_rect)
                        self.screen.blit(self.basil, (400, 150))
                        pygame.display.flip()
                        self.basil_added = True

                    elif (self.seasonings_rect.collidepoint(event.pos)
                          and self.recipe1_step2
                          and self.basil_added):        # Click on the seasonings to add them to the bowl 
                        pygame.draw.rect(self.screen, (236, 234, 230), self.seasonings_rect)
                        pygame.display.flip()
                        self.seasonings_added = True

                    elif (self.olive_oil_rect.collidepoint(event.pos)
                          and self.recipe1_step2
                          and self.seasonings_added):        # Click on olive oil to add it to the bowl 
                        pygame.draw.rect(self.screen, (236, 234, 230), self.olive_oil_rect)
                        pygame.display.flip()
                        self.olive_oil_added = True

                    elif (self.bowl_rect.collidepoint(event.pos)
                          and self.recipe1_step2
                          and self.olive_oil_added):        # Click on the bowl to mix it 
                        self.screen.blit(self.bowl, (400, 150))
                        self.screen.blit(self.bruschetta_mixed, (190,100))
                        self.screen.blit(self.arrow, (1300, 600))
                        self.mixing_sound.play()
                        pygame.display.flip()
                        self.ingredients_mixed = True
                        self.recipe1_step2 = False

                    elif (self.arrow_rect2.collidepoint(event.pos)
                          and self.ingredients_mixed):        # Click on the arrow to finish the cooking process  
                        self.screen.blit(self.recipe_display_surface, (0,0))
                        self.screen.blit(self.x, (-70,-50))
                        self.screen.blit(self.finished_cooking, (400, 100))
                        self.screen.blit(self.bruschetta_served, (300,200))
                        self.mixing_sound.stop()
                        pygame.display.flip()
                        self.reset_images()
                    
                        
            keys = pygame.key.get_pressed()
            if (keys[pygame.K_SPACE]
                and self.tomato_selected):        # Press the space key to chop the tomato
                if self.tomato_position[0] >= tomato_chop_position:        # The tomato stops moving and turns into a chopped tomato once a position is reached 
                    self.tomato_position[0] = 200
                    self.tomato = pygame.image.load("images/chopped_tomato.png")
                    self.tomato = pygame.transform.scale_by(self.tomato, 0.5)
                    self.screen.blit(self.kitchen_surface, (0,0))
                    self.screen.blit(self.x, (-70,-50))
                    self.screen.blit(self.cutting_board, (-250, -280))
                    self.screen.blit(self.garlic, (-100, 400))
                    self.screen.blit(self.instruction_cutting, (100, 20))
                    self.screen.blit(self.tomato, (600, 200))
                    pygame.display.flip()
                    self.tomato_done = True
                    self.tomato_selected = False

                # If the tomato is not at the right position yet, it moves to the right when the space key is pressed   
                else: 
                    self.tomato_position[0] = self.tomato_position[0] + self.cutting_speed
                    self.screen.blit(self.kitchen_surface, (0, 0))
                    self.screen.blit(self.x, (-70, -50))
                    self.screen.blit(self.cutting_board, (-250, -280))
                    self.screen.blit(self.garlic, (-100, 400))
                    self.screen.blit(self.instruction_cutting, (100, 20))
                    self.screen.blit(self.tomato, self.tomato_position)
                    self.cutting_sound.play()
                    pygame.display.flip()


            elif (keys[pygame.K_SPACE]
                  and self.garlic_selected):        # Press the space key to chop garlic
                if self.garlic_position[0] >= garlic_chop_position:        # Garlic stops moving and turns into chopped garlic once position is reached   
                    self.garlic_position[0] = 550
                    self.garlic = pygame.image.load("images/chopped_garlic.png")
                    self.garlic = pygame.transform.scale_by(self.garlic, 0.5)
                    self.screen.blit(self.kitchen_surface, (0,0))
                    self.screen.blit(self.x, (-70,-50))
                    self.screen.blit(self.cutting_board, (-250, -280))
                    self.screen.blit(self.instruction_cutting, (100, 20))
                    self.screen.blit(self.garlic, (600, 150))
                    self.screen.blit(self.arrow, (1300, 600))
                    pygame.display.flip()
                    self.garlic_selected = False
                    self.recipe1_step1 = False
                    self.recipe1_step2 = True

                # If the garlic is not at the right position yet, it moves to the right when the space key is pressed
                else: 
                    self.garlic_position[0] = self.garlic_position[0] + self.cutting_speed - 3
                    self.screen.blit(self.kitchen_surface, (0, 0))
                    self.screen.blit(self.x, (-70, -50))
                    self.screen.blit(self.cutting_board, (-250, -280))
                    self.screen.blit(self.instruction_cutting, (100, 20))
                    self.screen.blit(self.garlic, self.garlic_position)
                    self.cutting_sound.play()
                    pygame.display.flip()

                    
        # Making recipe 2
        cauliflower_chop_position = 600
        tofu_chop_position = 600
        while self.making_recipe2:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if self.x_rect.collidepoint(event.pos):        # Click on x to leave the cooking process of recipe 2
                        self.screen.blit(self.kitchen_background, (0,0))
                        self.screen.blit(self.book, (30, 400))
                        self.screen.blit(self.arrow, (1320, 630))
                        self.screen.blit(self.character_front, (100,300))
                        pygame.display.flip()
                        self.kitchen()
                        self.making_recipe2 = False
                        self.display_first_recipes = True
                        self.book_opened = False
        
                    elif (self.cauliflower_rect.collidepoint(event.pos)
                          and self.recipe2_step1):        # Click on the cauliflower to put it on the cutting board 
                        pygame.draw.rect(self.screen, (236, 234, 230), self.cauliflower_rect)
                        self.screen.blit(self.cauliflower, (350, 280))
                        pygame.display.flip()
                        self.cauliflower_selected = True

                    elif (self.tofu_rect.collidepoint(event.pos)
                          and self.recipe2_step1
                          and self.cauliflower_done):        # Click on the tofu to put it on the cutting board 
                        pygame.draw.rect(self.screen, (236, 234, 230), self.tofu_rect)
                        self.screen.blit(self.tofu, (200, 250))
                        pygame.display.flip()
                        self.tofu_selected = True

                    elif (self.arrow_rect2.collidepoint(event.pos)
                          and self.recipe2_step2):        # Click on the arrow to get to next step in the cooking process
                        self.screen.blit(self.kitchen_surface, (0,0))
                        self.screen.blit(self.x, (-70,-50))
                        self.screen.blit(self.instruction_frying, (100, 20))
                        self.screen.blit(self.pan, (400, 100))
                        self.cauliflower = pygame.transform.scale_by(self.cauliflower, 0.6)
                        self.screen.blit(self.cauliflower, (20, 50))
                        self.tofu = pygame.transform.scale_by(self.tofu, 0.6)
                        self.screen.blit(self.tofu, (20, 210))
                        self.screen.blit(self.spices, (30, 400))
                        self.screen.blit(self.coconut_milk, (30, 580))
                        pygame.display.flip()

                    elif (self.chopped_cauliflower_rect.collidepoint(event.pos)
                          and self.recipe2_step2):        # Click on the cauliflower to add it to the bowl   
                        pygame.draw.rect(self.screen, (236, 234, 230), self.chopped_cauliflower_rect)
                        self.cauliflower = pygame.transform.scale_by(self.cauliflower, 2)
                        self.screen.blit(self.cauliflower, (500, 230))
                        self.frying_sound.play()
                        pygame.display.flip()
                        self.chopped_cauliflower_added = True

                    elif (self.chopped_tofu_rect.collidepoint(event.pos)
                          and self.recipe2_step2
                          and self.chopped_cauliflower_added):        # Click on the tofu to add it to the bowl   
                        pygame.draw.rect(self.screen, (236, 234, 230), self.chopped_tofu_rect)
                        self.tofu = pygame.transform.scale_by(self.tofu, 2)
                        self.screen.blit(self.tofu, (500, 250))
                        pygame.display.flip()
                        self.chopped_tofu_added = True

                    elif (self.spices_rect.collidepoint(event.pos)
                          and self.recipe2_step2
                          and self.chopped_tofu_added):        # Click on spices to add them to the bowl   
                        pygame.draw.rect(self.screen, (236, 234, 230), self.spices_rect)
                        self.screen.blit(self.spices_loose, (500, 300))
                        pygame.display.flip()
                        self.spices_added = True

                    elif (self.coconut_milk_rect.collidepoint(event.pos)
                          and self.recipe2_step2
                          and self.spices_added):        # Click on the coconut milk to add it to the bowl   
                        pygame.draw.rect(self.screen, (236, 234, 230), self.coconut_milk_rect)
                        self.screen.blit(self.coconut_milk_liquid, (400, 100))
                        self.screen.blit(self.cauliflower, (500, 230))
                        self.screen.blit(self.tofu, (500, 250))
                        self.screen.blit(self.spices_loose, (500, 300))
                        pygame.display.flip()
                        self.coconut_milk_added = True

                    elif (self.pan_rect.collidepoint(event.pos)
                          and self.recipe2_step2
                          and self.coconut_milk_added):        # Click on the pan to mix everything  
                        self.screen.blit(self.pan, (400, 100))
                        self.screen.blit(self.spices_mixed, (400,160))
                        self.screen.blit(self.cauliflower_tofu, (500, 250))
                        self.screen.blit(self.arrow, (1300, 600))
                        self.mixing_sound.play()
                        pygame.display.flip()
                        self.ingredients_mixed = True
                        self.recipe2_step2 = False

                    elif (self.arrow_rect2.collidepoint(event.pos)
                          and self.making_recipe2
                          and self.ingredients_mixed):        # Click on the arrow to finish the cooking process 
                        self.frying_sound.stop()
                        self.mixing_sound.stop()
                        self.screen.blit(self.recipe_display_surface, (0,0))
                        self.screen.blit(self.x, (-70,-50))
                        self.screen.blit(self.curry_served, (380,280))
                        self.screen.blit(self.finished_cooking, (400, 100))
                        pygame.display.flip()
                        self.reset_images()
            
                        
            keys = pygame.key.get_pressed()
            if (keys[pygame.K_SPACE]
                and self.cauliflower_selected):        # Press the space key to chop the cauliflower
                if self.cauliflower_position[0] >= cauliflower_chop_position:        # The cauliflower stops moving and turns into chopped cauliflower once a position is reached 
                    self.cauliflower_position[0] = 600
                    self.cauliflower = pygame.image.load("images/chopped_cauliflower.png")
                    self.cauliflower = pygame.transform.scale_by(self.cauliflower, 0.6)
                    self.screen.blit(self.kitchen_surface, (0,0))
                    self.screen.blit(self.x, (-70,-50))
                    self.screen.blit(self.cutting_board, (-250, -280))
                    self.screen.blit(self.tofu, (10, 400))
                    self.screen.blit(self.instruction_cutting, (100, 20))
                    self.screen.blit(self.cauliflower, (700, 250))
                    pygame.display.flip()
                    self.cauliflower_done = True
                    self.cauliflower_selected = False

                # If the cauliflower is not at the right position yet, it moves to the right when the space key is pressed
                else:
                    self.cauliflower_position[0] = self.cauliflower_position[0] + self.cutting_speed
                    self.screen.blit(self.kitchen_surface, (0, 0))
                    self.screen.blit(self.x, (-70, -50))
                    self.screen.blit(self.cutting_board, (-250, -280))
                    self.screen.blit(self.tofu, (10, 400))
                    self.screen.blit(self.instruction_cutting, (100, 20))
                    self.screen.blit(self.cauliflower, self.cauliflower_position)
                    self.cutting_sound.play()
                    pygame.display.flip()

            elif (keys[pygame.K_SPACE]
                  and self.tofu_selected):        # Preaa the space key to chop tofu
                if self.tofu_position[0] >= tofu_chop_position:        # The tofu stops moving and turns into chopped tofu once a position is reached 
                    self.tofu_position[0] = 600
                    self.tofu = pygame.image.load("images/chopped_tofu.png")
                    self.tofu = pygame.transform.scale_by(self.tofu, 0.6)
                    self.screen.blit(self.kitchen_surface, (0,0))
                    self.screen.blit(self.x, (-70,-50))
                    self.screen.blit(self.cutting_board, (-250, -280))
                    self.screen.blit(self.instruction_cutting, (100, 20))
                    self.screen.blit(self.tofu, (700, 250))
                    self.screen.blit(self.arrow, (1300, 600))
                    pygame.display.flip()
                    self.tofu_selected = False
                    self.recipe2_step1 = False
                    self.recipe2_step2 = True

                # If the tofu is not at the right position yet, it moves to the right when the space key is pressed
                else:
                    self.tofu_position[0] = self.tofu_position[0] + self.cutting_speed
                    self.screen.blit(self.kitchen_surface, (0, 0))
                    self.screen.blit(self.x, (-70, -50))
                    self.screen.blit(self.cutting_board, (-250, -280))
                    self.screen.blit(self.instruction_cutting, (100, 20))
                    self.screen.blit(self.tofu, self.tofu_position)
                    self.cutting_sound.play()
                    pygame.display.flip()


        # Making recipe 3
        while self.making_recipe3:
            for event in pygame.event.get():
                if event.type == MOUSEBUTTONDOWN:
                    if self.x_rect.collidepoint(event.pos):        # Click on x to leave the cooking process of recipe 3
                        self.screen.blit(self.kitchen_background, (0,0))
                        self.screen.blit(self.book, (30, 400))
                        self.screen.blit(self.arrow, (1320, 630))
                        self.screen.blit(self.character_front, (100,300))
                        pygame.display.flip()
                        self.kitchen()
                        self.making_recipe3 = False
                        self.display_first_recipes = True
                        self.book_opened = False

                    elif (self.flour_rect.collidepoint(event.pos)
                          and self.recipe3_step1):        # Click on the flour to add it to the bowl
                        pygame.draw.rect(self.screen, (236, 234, 230), self.flour_rect)
                        self.screen.blit(self.dry_ingredients, (400, 190))
                        pygame.display.flip()
                        self.flour_added = True

                    elif (self.sugar_rect.collidepoint(event.pos)
                          and self.recipe3_step1
                          and self.flour_added):        # Click on the sugar to add it to the bowl
                        pygame.draw.rect(self.screen, (236, 234, 230), self.sugar_rect)
                        pygame.display.flip()
                        self.sugar_added = True
                        
                    elif (self.baking_powder_rect.collidepoint(event.pos)
                          and self.recipe3_step1
                          and self.sugar_added):        # Click on the baking powder to add it to the bowl
                        pygame.draw.rect(self.screen, (236, 234, 230), self.baking_powder_rect)
                        pygame.display.flip()
                        self.baking_powder_added = True

                    elif (self.salt_rect.collidepoint(event.pos)
                          and self.recipe3_step1
                          and self.baking_powder_added):        # Click on the salt to add it to the bowl
                        pygame.draw.rect(self.screen, (236, 234, 230), self.salt_rect)
                        self.screen.blit(self.arrow, (1300, 600))
                        pygame.display.flip()
                        self.recipe3_step1 = False
                        self.recipe3_step2 = True 
                        
                    elif (self.arrow_rect2.collidepoint(event.pos)
                          and self.recipe3_step2):        # Click on the arrow to get to the next step in the cooking process
                        self.screen.blit(self.kitchen_surface, (0,0))
                        self.screen.blit(self.x, (-70,-50))
                        self.screen.blit(self.instruction_adding_mixing, (100, 20))
                        self.screen.blit(self.bowl, (400, 150))
                        self.screen.blit(self.milk, (30, 100))
                        self.screen.blit(self.vinegar, (50, 350))
                        self.screen.blit(self.vanilla, (40, 580))
                        pygame.display.flip()

                    elif (self.milk_rect.collidepoint(event.pos)
                          and self.recipe3_step2):        # Click on the milk to add it to the bowl 
                        pygame.draw.rect(self.screen, (236, 234, 230), self.milk_rect)
                        self.screen.blit(self.milk_liquid, (410, 180))
                        pygame.display.flip()
                        self.milk_added = True

                    elif (self.vinegar_rect.collidepoint(event.pos)
                          and self.milk_added):        # Click on the vinegar to add it to the bowl 
                        self.screen.blit(self.bowl, (400, 150))
                        pygame.draw.rect(self.screen, (236, 234, 230), self.vinegar_rect)
                        self.screen.blit(self.vinegar_liquid, (380, 187))
                        pygame.display.flip()
                        self.vinegar_added = True

                    elif (self.vanilla_rect.collidepoint(event.pos)
                          and self.vinegar_added):        # Click on the vanilla to add it to the bowl 
                        self.screen.blit(self.bowl, (400, 150))
                        pygame.draw.rect(self.screen, (236, 234, 230), self.vanilla_rect)
                        self.screen.blit(self.vanilla_liquid, (390, 173))
                        pygame.display.flip()
                        self.milk_added = True
                        
                    elif (self.bowl_rect.collidepoint(event.pos)
                          and self.milk_added):        # Click on the bowl to mix it
                        self.screen.blit(self.bowl, (400, 150))
                        self.screen.blit(self.liquid_ingredients, (434, 215))
                        self.screen.blit(self.arrow, (1300, 600))
                        pygame.display.flip()
                        self.liquid_ingredients_done = True
                        self.recipe3_step2 = False
                        
                    elif (self.arrow_rect2.collidepoint(event.pos)
                          and self.liquid_ingredients_done):        # Click on the arrow to get to next step in the cooking process
                        self.screen.blit(self.kitchen_surface, (0,0))
                        self.screen.blit(self.x, (-70,-50))
                        self.screen.blit(self.instruction_bowl, (100, 20))
                        self.screen.blit(self.bowl, (700, 150))
                        self.screen.blit(self.liquid_ingredients, (734, 215))
                        self.screen.blit(self.bowl, (100, 150))
                        self.screen.blit(self.dry_ingredients, (100, 190))
                        pygame.display.flip()
                        self.bowls_prepared = True
                        self.milk_added = False

                    elif (self.bowl_rect2.collidepoint(event.pos)
                          and self.bowls_prepared):        # Click on the bowl to add ingredients to the other bowl
                        self.screen.blit(self.kitchen_surface, (0,0))
                        self.screen.blit(self.x, (-70,-50))
                        self.screen.blit(self.instruction_bowl, (100, 20))
                        self.screen.blit(self.bowl, (100, 150))
                        self.screen.blit(self.liquid_ingredients, (134,215))
                        self.screen.blit(self.bowl, (700, 150))
                        self.screen.blit(self.arrow, (1300, 600))
                        pygame.display.flip()
                        self.bowls_combined = True
                        self.liquid_ingredients_done = False
                        
                    elif (self.arrow_rect2.collidepoint(event.pos)
                          and self.bowls_combined):        # Click on the arrow to get to next step in the cooking process
                        self.screen.blit(self.kitchen_surface, (0,0))
                        self.screen.blit(self.x, (-70,-50))
                        self.screen.blit(self.instruction_frying_flipping, (100, 20))
                        self.bowl = pygame.transform.scale_by(self.bowl, 0.75)
                        self.screen.blit(self.bowl, (50, 150))
                        self.liquid_ingredients = pygame.transform.scale_by(self.liquid_ingredients, (0.75))
                        self.screen.blit(self.liquid_ingredients, (75, 200))
                        self.screen.blit(self.pan, (450, 150))
                        pygame.display.flip()
                        self.pan_prepared = True
                        self.bowls_prepared = False

                    elif (self.bowl_rect3.collidepoint(event.pos)
                          and self.pan_prepared):        # Click on the bowl to add the batter to pan
                        self.screen.blit(self.pancake_raw, (600, 300))
                        self.screen.blit(self.bowl, (50, 150))
                        self.frying_sound.play()
                        pygame.display.flip()
                        self.pancake_frying = True
                        self.bowls_combined = False

                    elif (self.pancake_raw_rect.collidepoint(event.pos)
                          and self.pancake_frying):        # Click on the pancake to flip it
                        self.screen.blit(self.pancake, (600, 300))
                        pygame.display.flip()
                        self.pancake_ready = True
                        self.pancake_frying = False

                    elif (self.pancake_rect.collidepoint(event.pos)
                          and self.pancake_ready):        # Click on tthe pancake to remove it from the pan
                        self.screen.blit(self.pan, (450, 150))
                        self.screen.blit(self.arrow, (1300, 600))
                        self.frying_sound.stop()
                        pygame.display.flip()
                        self.pancake_done = True
                        
                    elif (self.arrow_rect2.collidepoint(event.pos)
                          and self.pancake_done):        # Click on the arrow to finish the cooking process 
                        self.screen.blit(self.recipe_display_surface, (0,0))
                        self.screen.blit(self.x, (-70,-50))
                        self.screen.blit(self.finished_cooking, (400, 100))
                        self.screen.blit(self.pancakes_served, (450, 250))
                        pygame.display.flip()
                        self.reset_images()

                        
    def reset_images(self):
        """A function resetting all images altered in the cooking process"""
        
        self.tomato = self.tomato_original.copy()
        self.garlic = self.garlic_original.copy()
        self.cauliflower = self.cauliflower_original.copy()
        self.tofu = self.tofu_original.copy()
        self.bowl = self.bowl_original.copy()

        
    def future_ideas(self):
        """A function displaying future ideas and possible additions to the game"""
        
        if self.display_future_features:
            self.screen.blit(self.recipe_display_surface, (0,0))
            pygame.draw.rect(self.screen, (255, 200, 233), self.background_rect)
            self.screen.blit(self.future_features, (300,100))
            self.screen.blit(self.x, (-70,-50))
            pygame.display.flip()

        for event in pygame.event.get():
            if event.type == MOUSEBUTTONDOWN:
                if self.x_rect.collidepoint(event.pos):        # Click on x to close the window                                                                                          
                    self.screen.blit(self.kitchen_background, (0,0))
                    self.screen.blit(self.book, (30, 400))
                    self.screen.blit(self.arrow, (1320, 630))
                    self.screen.blit(self.character_front, self.character_position)
                    pygame.display.flip()
                    self.kitchen()
                    self.display_future_features = False

                
    def cat(self):
        """A function displaying the meow of a cat when the character is close to it"""

        if self.character_rect.colliderect(self.cat_rect):
            self.screen.blit(self.cat_speech_bubble, (60, 530))
            self.screen.blit(self.meow, (155,545))
            pygame.display.flip()

             
if __name__ == "__main__":
    harmony_kitchen = HarmonyKitchen()
    harmony_kitchen.start_game()
