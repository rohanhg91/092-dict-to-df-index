import pandas as pd
import numpy as np


def solution(data, index):
    datas = pd.DataFrame(data)
    datas['label'] = index
    indexed_data = datas.set_index('label')
    return indexed_data
