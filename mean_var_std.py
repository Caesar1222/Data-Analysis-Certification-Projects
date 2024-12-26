### Mean-Variance-Standard Deviation Calculator ###
import numpy as np
def calculate(list):
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')
    
    array1 = np.array(list)
    array1 = array1.reshape((3, 3))

    return {
        "mean": [np.mean(array1, axis = 0, ).tolist(), np.mean(array1, axis = 1).tolist(), np.mean(array1).tolist()],
        "variance": [np.var(array1, axis = 0).tolist(), np.var(array1, axis = 1).tolist(), np.var(array1).tolist()],
        "standard deviation": [np.std(array1, axis = 0).tolist(), np.std(array1, axis = 1).tolist(), np.std(array1).tolist()],
        "max": [np.max(array1, axis = 0).tolist(), np.max(array1, axis = 1).tolist(), np.max(array1).tolist()],
        "min": [np.min(array1, axis = 0).tolist(), np.min(array1, axis = 1).tolist(), np.min(array1).tolist()],
        "sum": [np.sum(array1, axis = 0).tolist(), np.sum(array1, axis = 1).tolist(), np.sum(array1).tolist()]
    }
