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

def julia(z, c, max_iter):
    n = 0
    while abs(z) <= 2 and n < max_iter:
        z = z**2 + c
        n += 1
    if n == max_iter:
        return max_iter
    return n + 1 - np.log(np.log2(abs(z)))

def fractal_image(width, height, x_min, x_max, y_min, y_max, max_iter, color_map, fractal_type='mandelbrot', animal_choice=None):
    image = np.zeros((height, width))

    for x in range(width):
        for y in range(height):
            real = x_min + (x / width) * (x_max - x_min)
            imag = y_min + (y / height) * (y_max - y_min)

            if animal_choice:
                if animal_choice == 'lion':
                    animal_real, animal_imag = -0.7, 0.27015
                elif animal_choice == 'papillon':
                    animal_real, animal_imag = 0.355, 0.355
                elif animal_choice == 'dauphin':
                    animal_real, animal_imag = -0.75, 0.1
                else:
                    raise ValueError("Animal non pris en charge.")
                c = complex(animal_real, animal_imag)
            else:
                # Si aucun animal choisi, utilise les coordonnées actuelles
                c = complex(real, imag)

            if fractal_type == 'mandelbrot':
                color = mandelbrot(c, max_iter)
            elif fractal_type == 'julia':
                z = complex(real, imag)
                color = julia(z, c, max_iter)
            else:
                raise ValueError("Type de fractal non pris en charge.")
                
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
    x_min, x_max = -2, 2
    y_min, y_max = -2, 2
    max_iter = 100

    # Couleur de fond
    background_color = 'black'

    # Palette de couleurs personnalisée
    custom_color_map = ['black', 'darkblue', 'blue', 'lightblue', 'white']

    # Interaction avec l'utilisateur pour choisir le type de fractal
    fractal_choice = input("Choisissez le type de fractal :\n1. Mandelbrot\n2. Julia\nRéponse (1 ou 2): ")

    if fractal_choice == '1':
        fractal_type = 'mandelbrot'
    elif fractal_choice == '2':
        fractal_type = 'julia'
    else:
        print("Choix non valide. Veuillez entrer 1 ou 2.")
        exit()

    # Interaction avec l'utilisateur pour choisir l'animal (si applicable)
    animal_choice = None
    if fractal_type == 'mandelbrot' or fractal_type == 'julia':
        animal_choice = input("Choisissez un animal :\n1. Lion\n2. Papillon\n3. Dauphin\nRéponse (lion, papillon, dauphin): ").lower()

    # Générer l'image du fractal en fonction des choix de l'utilisateur
    fractal_image, custom_cmap = fractal_image(width, height, x_min, x_max, y_min, y_max, max_iter, custom_color_map, fractal_type, animal_choice)

    # Afficher l'image du fractal
    plot_fractal(fractal_image, custom_cmap)
