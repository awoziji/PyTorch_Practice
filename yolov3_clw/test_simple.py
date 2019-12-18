import numpy as np
import torch

# anchors = [1,2,3,4,5]
#
# anchors = torch.FloatTensor(anchors)
# anchors = anchors.repeat(50 * 50, 2)
# anchors = anchors.unsqueeze(0)
#
# print('1111')

# grid1 = np.array([0,1])
# grid2 = np.array([2,3,4])
# a, b = np.meshgrid(grid1, grid2)
# print('a=',a)
# print('b=',b)

# Add the center offsets
grid_size=10
grid = np.arange(grid_size)
a, b = np.meshgrid(grid, grid)
print('a=',a)
print('b=',b)
x_offset = torch.FloatTensor(a).view(-1, 1)
y_offset = torch.FloatTensor(b).view(-1, 1)
print('x_offset=',x_offset)
print('y_offset=',y_offset)