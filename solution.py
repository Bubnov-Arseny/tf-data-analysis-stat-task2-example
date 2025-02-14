import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 700385968 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    alpha = 1 - p
    loc = 2*x.mean() - 0.05
    scale = np.sqrt(np.var(x)) / np.sqrt(len(x))
    return loc - scale * norm.ppf(1 - alpha / 1024), \
           loc - scale * norm.ppf(alpha / 1024)
