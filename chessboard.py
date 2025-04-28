#tabuleiro de xadrez - chess board 

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

# Criação do tabuleiro
board = np.tile([1, 0], (8, 4))

# Ajuste das linhas do tabuleiro
for i in range(board.shape[0]):
    board[i] = np.roll(board[i], i % 2)

# Definição do colormap
cmap = ListedColormap(['#779556', '#ebec00'])

# Plotagem do tabuleiro
plt.matshow(board, cmap=cmap)
plt.xticks([])
plt.yticks([])
plt.show()