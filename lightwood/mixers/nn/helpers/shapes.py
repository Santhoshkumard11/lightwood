import logging
import math


def funnel(in_size, out_size, depth):
    if depth < 2:
        logging.warning('Depth must be at least 2 for the funnel function to work correctly, setting it to 2')
        depth = 2

    step_denominator = depth - 1
    layers = list( range(out_size, in_size, round((in_size - out_size)/step_denominator) ) )
    layers.reverse()
    layers = [in_size, *layers]
    return layers

def rectangle(in_size,out_size,depth):
    if depth < 2:
        logging.warning('Depth must be at least 2 for the rectangle function to work correctly, setting it to 2')
        depth = 2

    layers = [in_size for x in range(depth - 1)]
    layers = [*layers,out_size]
    return layers

def rombus(in_size,out_size,depth,max_size=None):
    if max_size is None:
        max_size = max(in_size,out_size)*2
    if depth < 3:
        logging.warning('Depth must be at least 3 for the rombus function to work correctly, setting it to 3')
        depth = 3

    funnel_size = math.ceil(depth/2)

    first_funnel = funnel(in_size, max_size,funnel_size)

    if depth % 2 == 1:
        first_funnel = first_funnel[:-1]

    second_funnel = funnel(max_size,out_size,funnel_size)

    layers = [*first_funnel,*second_funnel]

    return layers
