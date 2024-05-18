import pandas as pd
import numpy as np
import scipy.stats as stats

chat_id = 1028099632 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
    alpha = 0.03
    z_a = stats.norm.ppf(1 - alpha)
    
    p1 = x_success / x_cnt # cont
    p2 = y_success / y_cnt # test
    p = (x_success + y_success) / (x_cnt + y_cnt) # all
    
    z = (p1 - p2) / np.sqrt(p * (1 - p) * (1 / x_cnt + 1 / y_cnt))
