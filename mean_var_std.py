import numpy as np

def calculate(lista):
    if len(lista) == 9:
        lista = np.array(lista)
        lista_matrix = lista.reshape((3, 3))
        calculations = {
            'mean': [np.mean(lista_matrix, axis=0).tolist(), np.mean(lista_matrix, axis=1).tolist(), np.mean(lista).tolist()],
            'variance': [np.var(lista_matrix, axis=0).tolist(), np.var(lista_matrix, axis=1).tolist(), np.var(lista).tolist()],
            'standard deviation': [np.std(lista_matrix, axis=0).tolist(), np.std(lista_matrix, axis=1).tolist(), np.std(lista).tolist()],
            'max': [np.max(lista_matrix, axis=0).tolist(), np.max(lista_matrix, axis=1).tolist(), np.max(lista).tolist()],
            'min': [np.min(lista_matrix, axis=0).tolist(), np.min(lista_matrix, axis=1).tolist(), np.min(lista).tolist()],
            'sum': [np.sum(lista_matrix, axis=0).tolist(), np.sum(lista_matrix, axis=1).tolist(), np.sum(lista).tolist()]
        }
    else:
        raise ValueError('List must contain nine numbers.')
    return calculations