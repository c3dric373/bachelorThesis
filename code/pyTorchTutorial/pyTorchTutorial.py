from __future__ import print_function
import torch

x=torch.tensor([[1,1],[-1,-1]])
print(x)
y=torch.tensor([[0,0],[1,1]])
print(y)
print(torch.add(x,y))
print(y.add_(x))
x0 = x.view(4)
print(x0)
x=torch.empty(5,3)
z = torch.randn(4,4,4)
z0 = z.view(-1,8,2)
print(z0.size())
print(torch.cuda.is_available())
