from tkinter import *
from random import randint
from Logger import Logger
from time import strftime

SHAPE_SCALE = 30
logName = "Logs\\" + strftime("%d%m%Y%H%M%S") + ".log"
log = Logger(logName)


def check_collision(canvas, shape1, shape2):
    # Returns True if shape2 is touching shape1
    # Returns False otherwise.
    s1 = canvas.coords(shape1)
    s2 = canvas.coords(shape2)
    log.debug(s1, s2)
    return (s1[0] <= s2[0] <= s1[2] or s1[0] <= s2[2] <= s1[2])\
           and (s1[1] <= s2[1] <= s1[3] or s1[1] <= s2[3] <= s1[3])


def add_state(canvas, state, states):
    log.debug(states)
    width = canvas.width
    height = canvas.height
    # TODO: temporary Condition; find a better one.
    tests_pass = False
    new_shape = None
    while not tests_pass:
        chosen_width = randint(0, width-30)
        chosen_height = randint(0, height-30)
        new_shape = canvas.create_oval(chosen_width,
                                       chosen_height,
                                       chosen_width+30,
                                       chosen_height+30,
                                       fill="white")
        log.debug("Shape = ", canvas.coords(new_shape))
        for s in states:
            log.debug("s = ", s)
            if s == state:
                continue
            collision = check_collision(canvas, s.shape, new_shape)
            if collision:
                log.debug("Collision")
                canvas.delete(new_shape)
                break
        else:
            tests_pass = True
            state.shape = new_shape
            pass