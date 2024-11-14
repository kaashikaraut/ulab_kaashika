# imageplotting.py
import numpy as np
import matplotlib.pyplot as plt

def display_basic_image(data=None, cmap='viridis', interpolation='nearest'):
    """
    Displays a basic image with specified colormap and interpolation.
    
    Parameters:
        data (2D array, optional): The data to plot as an image. If None, a random 10x10 matrix is generated.
        cmap (str, optional): The colormap to use. Default is 'viridis'.
        interpolation (str, optional): The interpolation method to use. Default is 'nearest'.
    """
    # Generate random data if none is provided
    if data is None:
        data = np.random.rand(10, 10)
    
    plt.imshow(data, cmap=cmap, interpolation=interpolation)
    plt.colorbar(label="Color Scale")
    plt.title(f"Colormap: {cmap} | Interpolation: {interpolation}")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.show()


def plot_interpolations(data=None, cmap='viridis'):
    """
    Displays an image with multiple interpolation options in a 3x3 grid with a colorbar below the grid.
    
    Parameters:
        data (2D array, optional): The data to plot as an image. If None, a 5x5 random matrix is generated.
        cmap (str, optional): The colormap to use. Default is 'viridis'.
    """
    # Generate random data if none is provided
    if data is None:
        data = np.random.rand(5, 5)

    interpolations = [
        'nearest', 'bilinear', 'bicubic', 'spline16', 'spline36',
        'hanning', 'hamming', 'hermite', 'kaiser'
    ]
    
    fig, axes = plt.subplots(3, 3, figsize=(12, 12))
    fig.suptitle("Different Interpolation Methods", fontsize=16)

    # Plot each subplot with its own interpolation
    for ax, interp in zip(axes.flat, interpolations):
        im = ax.imshow(data, cmap=cmap, interpolation=interp)
        ax.set_title(f"Interpolation: {interp}")
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")

    # Add a colorbar below all the subplots
    cbar = fig.colorbar(im, ax=axes.ravel().tolist(), orientation='horizontal', fraction=0.05, pad=0.1, label="Color Scale")
    
    # Adjust layout manually instead of using tight_layout
    fig.subplots_adjust(top=0.92, wspace=0.3, hspace=0.3)
    plt.show()


def plot_various_colormaps(data=None):
    """
    Displays the data with different colormaps in a 3x3 grid with a single colorbar below the grid.
    
    Parameters:
        data (2D array, optional): The data to plot as an image. If None, a 10x10 random matrix is generated.
    """
    # Generate random data if none is provided
    if data is None:
        data = np.random.rand(10, 10)

    colormaps = [
        'viridis', 'plasma', 'inferno', 'magma', 'cividis',
        'Greys', 'Purples', 'Blues', 'Oranges'
    ]
    
    fig, axes = plt.subplots(3, 3, figsize=(12, 12))
    fig.suptitle("Different Colormaps", fontsize=16)

    # Plot each subplot with a different colormap
    for ax, cmap in zip(axes.flat, colormaps):
        im = ax.imshow(data, cmap=cmap)
        ax.set_title(f"Colormap: {cmap}")
        ax.set_xlabel("X-axis")
        ax.set_ylabel("Y-axis")

    # Add a single colorbar below all the subplots
    cbar = fig.colorbar(im, ax=axes.ravel().tolist(), orientation='horizontal', fraction=0.05, pad=0.1, label="Color Scale")
    
    # Adjust layout manually instead of using tight_layout to avoid layout warnings
    fig.subplots_adjust(top=0.92, wspace=0.3, hspace=0.3)
    plt.show()