#!/usr/bin/env python
# coding=utf-8

# Manages Reproducibility

import numpy as np
import random
import torch

def set_seed(seed=None, seed_torch=True, seed_cudnn=False):
    """Set seed of random number generators to limit the number of sources of
    nondeterministic behavior for a specific platform, device, and PyTorch
    release. For more information, see
    https://pytorch.org/docs/stable/notes/randomness.html.

    Parameters
    ----------
    seed: int
        Seed for random number generators.
        Default: 2**32
    seed_torch: bool
        If we will set the seed for torch random number generators.
        Default: True

    Returns
    -------
    seed : int
        Seed used for random number generators
    """
    if seed is None:
        seed_str = "{{ cookiecutter.repo_name }}"
        seed = [str(ord(letter) - 96) for letter in seed_str]
        seed = abs(int(''.join(seed))) % 2 ** 32
        #seed = np.random.choice(2 ** 32)

    # Set python seed for custom operators
    random.seed(seed)

    # Set seed for the global NumPy RNG if any of the libraries rely on NumPy
    np.random.seed(seed)

    if seed_torch:
        # Seed the RNG for all devices (both CPU and CUDA)
        torch.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)
        torch.cuda.manual_seed(seed)
        if seed_cudnn:
            # Set cuDNN to deterministically select a convolution algorithm
            torch.backends.cudnn.benchmark = False
            # Ensure that the cuDNN convolution algorithm is deterministic
            torch.backends.cudnn.deterministic = True

    print(f'Random seed {seed} has been set.')

    return seed


def seed_worker(worker_id):
    """Set seed for Dataloader. DataLoader will reseed workers the "Randomness
    in multi-process data loading" algorithm. Use `worker_init_fn()` to
    preserve reproducibility. For more information, see
    https://pytorch.org/docs/stable/notes/randomness.html.
    """
    worker_seed = torch.initial_seed() % 2**32
    np.random.seed(worker_seed)
    random.seed(worker_seed)


def set_generator(seed=0):
    """Set seed for Dataloader generators. DataLoader will reseed workers the
    "Randomness in multi-process data loading" algorithm. Use `generator` to
    preserve reproducibility. For more information, see
    https://pytorch.org/docs/stable/notes/randomness.html.

    Parameters
    ----------
    seed: int
        Seed for random number generators.
        Default: 0

    Returns
    -------
    generator: torch.Generator
        Seeded torch generator
    """
    generator = torch.Generator()
    generator.manual_seed(seed)

    return generator


def set_device():
    """
    Setup device (GPU or CPU).

    Returns
    -------
    device: str
        The device to be used, either `cpu` or `gpu`

    """
    device = "cuda" if torch.cuda.is_available() else "cpu"
    # Inform the user if torch  uses GPU or CPU.
    if device != "cuda":
        print("GPU is not enabled.")
    else:
        print("GPU is enabled.")

    return device
