import pygame
import random
import os
import neat
import matplotlib as plt
pygame.font.init()  # init font
width = 600
height = 800
FLOOR = 730
STAT_FONT = pygame.font.SysFont("arial", 40)
END_FONT = pygame.font.SysFont("arial", 40)
DRAW_LINES = True

WIN = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flappy Bird")

pipe_img = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "pipe.png")).convert_alpha())
bg_img = pygame.transform.scale(pygame.image.load(os.path.join("imgs", "bg.png")).convert_alpha(), (600, 900))
bird_images = [pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "bird" + str(x) + ".png"))) for x in range(1,4)]
base_img = pygame.transform.scale2x(pygame.image.load(os.path.join("imgs", "base.png")).convert_alpha())

gen = 0


class Bird:

    #Bird class 

    MAX_ROTATION = 25
    IMGS = bird_images
    ROT_VEL = 20
    ANIMATION_TIME = 5

    def __init__(self, x, y):
     
       
        #param x: starting x pos (int)
        #param y: starting y pos (int)
        
        self.x = x
        self.y = y
        self.tilt = 0  # degrees to tilt
        self.tick_count = 0
        self.vel = 0
        self.height = self.y
        self.img_count = 0
        self.img = self.IMGS[0]

    def jump(self):
        """
        make the bird jump
        :return: None
        """
        self.vel = -9.5
        self.tick_count = 0
        self.height = self.y

    def move(self):
        """
        make the bird move
        """
        self.tick_count += 1

        # for downward acceleration
        down_acceleration = self.vel*(self.tick_count) + 0.5*(3)*(self.tick_count)**2  # calculate displacement

        # terminal velocity
        if down_acceleration >= 16:
            down_acceleration = (down_acceleration/abs(down_acceleration)) * 16

        if down_acceleration < 0:
            down_acceleration -= 2

        self.y = self.y + down_acceleration

        if down_acceleration < 0 or self.y < self.height + 50:  # tilt up
            if self.tilt < self.MAX_ROTATION:
                self.tilt = self.MAX_ROTATION
        else:  # tilt down
            if self.tilt > -90:
                self.tilt -= self.ROT_VEL

    def draw(self, win):
       
        self.img_count += 1
        
        # so when bird is nose diving it isn't flapping
        if self.tilt <= -80:
            self.img = self.IMGS[1]
            self.img_count = self.ANIMATION_TIME*2


        # tilt the bird
        blitRotateCenter(win, self.img, (self.x, self.y), self.tilt)

    def get_mask(self):
        return pygame.mask.from_surface(self.img)


class Pipe():
    

    
    pipe_size = 160
    pipe_speed = 6

    def __init__(self, x):
        
        self.x = x
        self.height = 0

        # where the top and bottom of the pipe is
        self.top = 0
        self.bottom = 0

        self.PIPE_TOP = pygame.transform.flip(pipe_img, False, True)
        self.PIPE_BOTTOM = pipe_img

        self.passed = False

        self.set_height()

    def set_height(self):
        
        self.height = random.randrange(50, 450)
        self.top = self.height - self.PIPE_TOP.get_height()
        self.bottom = self.height + self.pipe_size

    def move(self):
        
        self.x -= self.pipe_speed

    def draw(self, win):
        
        # draw top
        win.blit(self.PIPE_TOP, (self.x, self.top))
        # draw bottom
        win.blit(self.PIPE_BOTTOM, (self.x, self.bottom))


    def collide(self, bird, win):
       
        bird_mask = bird.get_mask()
        top_mask = pygame.mask.from_surface(self.PIPE_TOP)
        bottom_mask = pygame.mask.from_surface(self.PIPE_BOTTOM)
        top_offset = (self.x - bird.x, self.top - round(bird.y))
        bottom_offset = (self.x - bird.x, self.bottom - round(bird.y))

        b_point = bird_mask.overlap(bottom_mask, bottom_offset)
        t_point = bird_mask.overlap(top_mask,top_offset)

        if b_point or t_point:
            return True

        return False

class Base:
    
    pipe_speed = 5
    WIDTH = base_img.get_width()
    IMG = base_img

    def __init__(self, y):
        
        self.y = y
        self.x1 = 0
        self.x2 = self.WIDTH

    def move(self):
       
        self.x1 -= self.pipe_speed
        self.x2 -= self.pipe_speed
        if self.x1 + self.WIDTH < 0:
            self.x1 = self.x2 + self.WIDTH

        if self.x2 + self.WIDTH < 0:
            self.x2 = self.x1 + self.WIDTH

    def draw(self, win):
        
        win.blit(self.IMG, (self.x1, self.y))
        win.blit(self.IMG, (self.x2, self.y))


def blitRotateCenter(surf, image, topleft, angle):
    
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect.topleft)



"""
exit_button_image = pygame.image.load('/Users/LuisV./machinelearningpractice/NEAT-FlappyBird/exit_btn.png').convert_alpha()

class button():
    def __init__(self, x, y, img, scale):
        width = img.get_width()
        height = img.get_height()
        self.image = pygame.transform.scale(img, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        #get mouse pos
        pos = pygame.mouse.get_pos()

        #check mouse over and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[1] == 1 and self.clicked == False:
                self.clicked = True
            elif pygame.mouse.get_pressed()[1] == 1 and self.clicked == True:
                self.clicked = False
        
        if self.clicked == True:
            DRAW_LINES == True
        if self.clicked == False:
            DRAW_LINES == False
            
        

        WIN.blit(self.image, (self.rect.x, self.rect.y))

linesbtn = button(4, 100, exit_button_image, 0.5)
"""
        

def draw_window(win, birds, pipes, base, score, gen, pipe_ind):

    if gen == 0:
        gen = 1
    win.blit(bg_img, (0,0))

    for pipe in pipes:
        pipe.draw(win)

    base.draw(win)
    for bird in birds:
        # draw lines from bird to pipe
        if DRAW_LINES:
            try:
                pygame.draw.line(win, (255,0,0), (bird.x+bird.img.get_width()/2, bird.y + bird.img.get_height()/2), (pipes[pipe_ind].x + pipes[pipe_ind].PIPE_TOP.get_width()/2, pipes[pipe_ind].height), 5)
                pygame.draw.line(win, (255,0,0), (bird.x+bird.img.get_width()/2, bird.y + bird.img.get_height()/2), (pipes[pipe_ind].x + pipes[pipe_ind].PIPE_BOTTOM.get_width()/2, pipes[pipe_ind].bottom), 5)
            except:
                pass
        # draw bird
        bird.draw(win)

    score_label = STAT_FONT.render("Score: " + str(score),1,(255,255,255))
    win.blit(score_label, (width - score_label.get_width() - 15, 10))

    # generations
    score_label = STAT_FONT.render("Gens: " + str(gen-1),1,(255,255,255))
    win.blit(score_label, (10, 10))
    print(neat.__annotations__)
    
    #draw lines
    #linesbtn.draw()


    # alive
    score_label = STAT_FONT.render("Alive: " + str(len(birds)),1,(255,255,255))
    win.blit(score_label, (10, 50))

    pygame.display.update()



def eval_genomes(genomes, config):

    global WIN, gen
    win = WIN
    gen += 1

    # start by creating lists holding the genome itself, the
    # neural network associated with the genome and the
    # bird object that uses that network to play
    nets = []
    birds = []
    ge = []
    for genome_id, genome in genomes:
        genome.fitness = 0  # start with fitness level of 0
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        nets.append(net)
        birds.append(Bird(230,350))
        ge.append(genome)

    base = Base(FLOOR)
    pipes = [Pipe(1000)]
    score = 0

    clock = pygame.time.Clock()

    run = True
    while run and len(birds) > 0:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        pipe_ind = 0
        if len(birds) > 0:
            if len(pipes) > 1 and birds[0].x > pipes[0].x + pipes[0].PIPE_TOP.get_width():  # determine whether to use the first or second
                pipe_ind = 1                                                                 # pipe on the screen for neural network input

        for x, bird in enumerate(birds):  # give each bird a fitness of 0.1 for each frame it stays alive
            ge[x].fitness += 0.1
            bird.move()

            # send bird location, top pipe location and bottom pipe location and determine from network whether to jump or not
            output = nets[birds.index(bird)].activate((bird.y, abs(bird.y - pipes[pipe_ind].height), abs(bird.y - pipes[pipe_ind].bottom)))
            if output[0] > 0.5:  # tanh
                bird.jump()
        base.move()
        removed_pipes = []
        add_pipe = False
        for pipe in pipes:
            pipe.move()
            # check for collision
            for bird in birds:
                if pipe.collide(bird, win):
                    ge[birds.index(bird)].fitness -= 1
                    nets.pop(birds.index(bird))
                    ge.pop(birds.index(bird))
                    birds.pop(birds.index(bird))
            if pipe.x + pipe.PIPE_TOP.get_width() < 0:
                removed_pipes.append(pipe)
            if not pipe.passed and pipe.x < bird.x:
                pipe.passed = True
                add_pipe = True
        if add_pipe:
            score += 1
            for genome in ge:
                genome.fitness += 10
            pipes.append(Pipe(width))

        for r in removed_pipes:
            pipes.remove(r)

        for bird in birds:
            if bird.y + bird.img.get_height() - 10 >= FLOOR or bird.y < -50:
                nets.pop(birds.index(bird))
                ge.pop(birds.index(bird))
                birds.pop(birds.index(bird))

        draw_window(WIN, birds, pipes, base, score, gen, pipe_ind)

        


def run(config_file):
 
    #runs the NEAT algorithm to train a neural network to play flappy bird.
    config_file = "NEAT-FlappyBird/config.txt"
    #:return: None

    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    # Create the population, which is the top-level object for a NEAT run.
    p = neat.Population(config)

    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    #p.add_reporter(neat.Checkpointer(5))

    # Run for up to 50 generations.
    p.run(eval_genomes, 5000)

    # show final stats
    #print('\nBest genome:\n{!s}'.format(winner))



if __name__ == '__main__':
    # Determine path to configuration file. This path manipulation is
    # here so that the script will run successfully regardless of the
    # current working directory.
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward.txt')
    run(config_path)

