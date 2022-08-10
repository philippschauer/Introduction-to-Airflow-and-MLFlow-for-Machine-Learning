import numpy as np
import logging

logging.basicConfig(format='[%(levelname)s]: %(message)s - %(asctime)s', level=logging.DEBUG)

# Some very important function
def compute_squares(number_list = np.linspace(0, 10, 10)):
    squares = []
    try:
        for number in number_list:
            squares.append(number ** 2)
        logging.info('Succeeded! %(squares)s') 
        if max(squares) > 200:
            return 'too_large'
        return 'success'
    except:
        logging.info('Did not work.') 
        return 'fail'


# Put your really important function here instead :p
