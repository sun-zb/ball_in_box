import math
import random
from .validate import validate

__all__ = ['ball_in_box']

def ball_in_box(m=5, blockers=[(0.5, 0.5), (0.5, -0.5), (0.5, 0.3)]):
    """
    m is the number circles.
    n is the list of coordinates of tiny blocks.
    
    This returns a list of tuple, composed of x,y of the circle and r of the circle.
    """

    circles = []

    for circle_index in range(m):
        tmp=0
        circles.append((0,0,0))
        for i in range(200):
            for j in range(200):
                x=-1+0.01*i
                y=-1+0.01*j
                for k in range(1000):
                    r=0.002*k
                    circles[circle_index]=(x,y,r)
                    if not validate(circles,blockers):
                        break
                if r-0.002>tmp :
                    tmp=r-0.002
                    tmp_circle=(x,y,tmp)
        circles[circle_index]=tmp_circle
        circle_index += 1
    
    return circles
