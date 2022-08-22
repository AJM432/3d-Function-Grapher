import pygame
import numpy as np

pygame.init()
clock = pygame.time.Clock()
WIDTH = HEIGHT = 400 # keep width and height the same
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3d Graphing")

FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
SCALE_FACTOR = 10
SCALE_FACTOR_CHANGE = 1
original_scale_factor = SCALE_FACTOR
ANGLE_CHANGE = 10*(np.pi/180)
NODE_SIZE = 1
BOUND = 20

def hsv_to_rgb(h, s, v):
    if s == 0.0: v*=255; return (v, v, v)
    i = int(h*6.)
    f = (h*6.)-i; p,q,t = int(255*(v*(1.-s))), int(255*(v*(1.-s*f))), int(255*(v*(1.-s*(1.-f)))); v*=255; i%=6
    if i == 0: return (v, t, p)
    if i == 1: return (q, v, p)
    if i == 2: return (p, v, t)
    if i == 3: return (p, q, v)
    if i == 4: return (t, p, v)
    if i == 5: return (v, p, q)

# this function determines the position of the z-axis point
def z_function(x, y):

    # if x*np.sin(y) + y*np.cos(x) <= 0: return 0
    # return np.log(x*np.sin(y) + y*np.cos(x))*2
# 
    # return np.sin(((x**2 + y**2)**(1/2)))*7

    # return (x**2 + y**2)/10
    # if x <= 0 or y <= 0:
        # return 0
    
    # return np.sin((x**(1/2)) + y**(1/2))*10

    # return sum(abs(1/n**(1j*x+1j*y)) for n in range(1, 100))

    # return 0

    return np.sin(5*x)*np.cos(5*y)*5


    # if x**2 + y**2 == 0: return 0
    # else: return (np.tan(np.log(x**2+ y**2)))
    # else: return np.log(x**2 + y**2)*10

    # if x**2 + y**2 == 0: return 0
    # else: return 100/(x**2+y**2)

def convert_ranges(value, value_min, value_max, new_min, new_max):
    return (((value - value_min) * (new_max - new_min)) / (value_max - value_min)) + new_min

# collection of functions that rotate a shape by a given angle
#________________________________________________________________
def rotate_x_axis(matrix, theta):
    rotation_matrix = np.array([[1, 0, 0],
                                [0, np.cos(theta), -np.sin(theta)],
                                [0, np.sin(theta), np.cos(theta)]])
    return np.dot(matrix, rotation_matrix)


def rotate_y_axis(matrix, theta):
    rotation_matrix = np.array([[np.cos(theta), 0, np.sin(theta)],
                                [0, 1, 0],
                                [-np.sin(theta), 0, np.cos(theta)]])
    return np.dot(matrix, rotation_matrix)


def rotate_z_axis(matrix, theta):
    rotation_matrix = np.array([[np.cos(theta), -np.sin(theta), 0],
                                [np.sin(theta), np.cos(theta), 0],
                                [0, 0, 1]])
    return np.dot(matrix, rotation_matrix)
#________________________________________________________________


def scale_array(x):
 return x*SCALE_FACTOR + WIDTH//2

# checks if the array index is at the edges of the array to avoid making long triangles
def in_bound(x):
    global BOUND
    for i in range(2*BOUND, (2*BOUND+1)**2+1, 2*BOUND+1):
        if i == x:
            return True
    return False

# find the min and max of a funnction
def find_min_max_val_function(f):
    global BOUND
    min_val = f(0, 0) # initial value
    max_val = f(0, 0) # initial value
    for x in range(-BOUND, BOUND+1):
        for y in range(-BOUND, BOUND+1):
            curr_val = f(x,y)
            if curr_val < min_val:
                min_val = curr_val
            elif curr_val > max_val:
                max_val = curr_val
    return [min_val, max_val]
    

def draw_matrix(matrix, node_size=NODE_SIZE, line_width=1):
    matrix = scale_array(matrix)
    min_matrix_x = min(matrix[0:,0])
    max_matrix_x = max(matrix[0:,0])
    min_matrix_y = min(matrix[0:,1])
    max_matrix_y = max(matrix[0:,1])
    # min_height, max_height = find_min_max_val_function(z_coordinate_height)

    for elem in range(len(matrix)):
        pygame.draw.circle(WIN, BLACK, (matrix[elem][0], matrix[elem][1]), node_size)


        if elem < len(matrix) - BOUND*2-2 and not in_bound(elem):

            hue_1 = convert_ranges(matrix[elem][0], min_matrix_x, max_matrix_x, 0.5, 1)
            brightness_1 = convert_ranges(matrix[elem][1], min_matrix_y, max_matrix_y, 0.6, 1)

            hue_2 = convert_ranges(matrix[elem+BOUND*2+1][0], min_matrix_x, max_matrix_x, 0.5, 1)
            brightness_2 = convert_ranges(matrix[elem+BOUND*2+1][1], min_matrix_y, max_matrix_y, 0.6, 1)

            color_1 = hsv_to_rgb(hue_1, 1, brightness_1)
            color_2 = hsv_to_rgb(hue_2, 1, brightness_2)

            pygame.draw.polygon(WIN, color_1, ((matrix[elem][0], matrix[elem][1]), (matrix[elem+BOUND*2+1][0], matrix[elem+BOUND*2+1][1]), (matrix[elem+BOUND*2+2][0], matrix[elem+BOUND*2+2][1])))
            pygame.draw.polygon(WIN, color_2, ((matrix[elem][0], matrix[elem][1]), (matrix[elem+1][0], matrix[elem+1][1]), (matrix[elem + BOUND*2+2][0], matrix[elem+BOUND*2+2][1])))
            # pygame.draw.polygon(WIN, color, ((matrix[elem][0], matrix[elem][1]), (matrix[elem+1][0], matrix[elem+1][1]), (matrix[elem + BOUND*2+2][0], matrix[elem+BOUND*2+2][1]), (matrix[elem+BOUND*2+1][0], matrix[elem+BOUND*2+1][1])))


points = [[x, y, z_function(x, y)] for x in range(-BOUND, BOUND+1) for y in range(-BOUND, BOUND+1)]

points = np.array(points)

projection_matrix = np.array([[1, 0, 0],
                              [0, 1, 0],
                              [0, 0, 0]])


two_dim_projection = points
three_dim_points_copy = points
running = True
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                three_dim_points_copy = points
                SCALE_FACTOR = original_scale_factor # update to constant variable

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        three_dim_points_copy = rotate_y_axis(
            three_dim_points_copy, -ANGLE_CHANGE)
    if keys[pygame.K_RIGHT]:
        three_dim_points_copy = rotate_y_axis(
            three_dim_points_copy, ANGLE_CHANGE)

    if keys[pygame.K_UP]:
        three_dim_points_copy = rotate_x_axis(
            three_dim_points_copy, ANGLE_CHANGE)

    if keys[pygame.K_DOWN]:
        three_dim_points_copy = rotate_x_axis(
            three_dim_points_copy, -ANGLE_CHANGE)

    if keys[pygame.K_q]:
        three_dim_points_copy = rotate_z_axis(
            three_dim_points_copy, ANGLE_CHANGE)

    if keys[pygame.K_w]:
        three_dim_points_copy = rotate_z_axis(
            three_dim_points_copy, -ANGLE_CHANGE)

    if keys[pygame.K_EQUALS]:
        SCALE_FACTOR += SCALE_FACTOR_CHANGE

    if keys[pygame.K_MINUS]:
        if SCALE_FACTOR - SCALE_FACTOR_CHANGE > 1:
            SCALE_FACTOR -= SCALE_FACTOR_CHANGE
        else:
            SCALE_FACTOR = 1

    WIN.fill(WHITE)

    two_dim_projection = np.dot(three_dim_points_copy, projection_matrix)
    draw_matrix(two_dim_projection)
    pygame.display.update()
    clock.tick(FPS)
