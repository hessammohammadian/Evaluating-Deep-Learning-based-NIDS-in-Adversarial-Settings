import torch
import torch.nn as nn
import numpy as np


class MultilayerPerceptron(nn.Module):
    def __init__(self, in_sz=76, out_sz=15, layers=[256, 256], p=0.2):
        super().__init__()

        layerlist = []

        for i in layers:
            layerlist.append(nn.Linear(in_sz, i))
            layerlist.append(nn.ReLU(inplace=True))
            layerlist.append(nn.Dropout(p))
            in_sz = i
        layerlist.append(nn.Linear(layers[-1], out_sz))

        self.layers = nn.Sequential(*layerlist)

    def forward(self, X):
        X = self.layers(X)
        return X


def FGSM(model, loss, epsilon, x, y, clip_min=0, clip_max=1, mask=None):

    adv_x = np.copy(x.detach().numpy())

    if mask is None:
        mask = np.ones_like(adv_x)

    output = model(x)
    loss = loss(output, y)
    model.zero_grad()
    loss.backward()

    with torch.no_grad():
        grad_sign = x.grad.data.sign()
        adv_x += epsilon * grad_sign.numpy() * mask

    adv_x = torch.FloatTensor(adv_x)
    adv_x = torch.clamp(adv_x, min=clip_min, max=clip_max)
    return adv_x