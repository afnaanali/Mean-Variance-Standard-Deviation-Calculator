import numpy as np

def calculate(lst):
    if len(lst) != 9:
        raise ValueError("List must contain nine numbers.")
    
    # Convert the list to a 3x3 numpy array
    arr = np.array(lst).reshape(3, 3)
    
    # Calculate statistics along axis 0 (columns), axis 1 (rows), and flattened
    calculations = {
        'mean': [
            arr.mean(axis=0).tolist(),
            arr.mean(axis=1).tolist(),
            arr.mean().item()
        ],
        'variance': [
            arr.var(axis=0).tolist(),
            arr.var(axis=1).tolist(),
            arr.var().item()
        ],
        'standard deviation': [
            arr.std(axis=0).tolist(),
            arr.std(axis=1).tolist(),
            arr.std().item()
        ],
        'max': [
            arr.max(axis=0).tolist(),
            arr.max(axis=1).tolist(),
            arr.max().item()
        ],
        'min': [
            arr.min(axis=0).tolist(),
            arr.min(axis=1).tolist(),
            arr.min().item()
        ],
        'sum': [
            arr.sum(axis=0).tolist(),
            arr.sum(axis=1).tolist(),
            arr.sum().item()
        ]
    }
    
    return calculations
    print(calculate([0,1,2,3,4,5,6,7,8]))