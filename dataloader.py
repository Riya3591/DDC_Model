import os
import torch

from torchvision import datasets, transforms

def load_training(root_path, directory, batch_size):
    transform = transforms.Compose(
        [transforms.Resize([256, 256]),
         transforms.RandomCrop(227),
         transforms.ToTensor(),
         transforms.Normalize(mean=[0.485, 0.456, 0.406],
                              std=[0.229, 0.224, 0.225])
         ]
    )
    data = datasets.ImageFolder(root=os.path.join(root_path, directory), transform=transform)
    train_loader = torch.utils.data.DataLoader(data, batch_size=batch_size, shuffle=True, drop_last=True)
    return train_loader

def load_testing(root_path, directory, batch_size):
    transform = transforms.Compose(
        [transforms.Resize([227, 227]),
         transforms.ToTensor(),
         transforms.Normalize(mean=[0.485, 0.456, 0.406],
                              std=[0.229, 0.224, 0.225]),
         ]
    )
    data = datasets.ImageFolder(root=os.path.join(root_path, directory), transform=transform)
    test_loader = torch.utils.data.DataLoader(data, batch_size=batch_size, shuffle=True)
    return test_loader