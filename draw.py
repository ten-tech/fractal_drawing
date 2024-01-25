import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

def mandelbrot(c, max_iter):
    z = 0
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z**2 + c
        n += 1
    if n == max_iter:
        return max_iter
    return n + 1 - np.log(np.log2(abs(z)))

def mandelbrot_fractal(width, height, x_min, x_max, y_min, y_max, max_iter, color_map):
    image = np.zeros((height, width))

    for x in range(width):
        for y in range(height):
            real = x_min + (x / width) * (x_max - x_min)
            imag = y_min + (y / height) * (y_max - y_min)
            c = complex(real, imag)
            color = mandelbrot(c, max_iter)
            image[y, x] = color

    # Normalisation des valeurs pour les couleurs
    norm_image = image / np.max(image)

    # Création de la colormap personnalisée
    custom_cmap = LinearSegmentedColormap.from_list('custom', color_map, N=max_iter)

    return norm_image, custom_cmap

def plot_fractal(image, color_map):
    plt.imshow(image, cmap=color_map)
    plt.colorbar()
    plt.show()

if __name__ == "__main__":
    width, height = 800, 800
    x_min, x_max = -2, 1
    y_min, y_max = -1, 1
    max_iter = 100

    # Couleur de fond
    background_color = 'black'

    # Palette de couleurs personnalisée
    custom_color_map = ['black', 'darkblue', 'blue', 'lightblue', 'white']

    fractal_image, custom_cmap = mandelbrot_fractal(width, height, x_min, x_max, y_min, y_max, max_iter, custom_color_map)

    # Afficher l'image du fractal avec la colormap personnalisée
    plot_fractal(fractal_image, custom_cmap)
