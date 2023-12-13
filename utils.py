from PIL import Image
from os import listdir
from os.path import splitext
import matplotlib.pyplot as plt
import os

#Funções auxiliares que utilizei

#Função pra transformar as imagens de jpg para png
def toPng():
    directory = './imgsOriginais/'
    target_directory = './imgs/'
    target = '.png'
    #lista os arquivos no diretório e percorre entre eles
    for file in listdir(directory):
        #Divide o arquivo em nome + extensão. Ex: filname = foto extensão = .jpg
        filename, extension = splitext(file)
        try:
            if extension not in ['.py', target]:
                if not os.path.exists(target_directory):
                     os.makedirs(target_directory)
                #Tenta abrir o arquivo
                im = Image.open(directory + filename + extension)
                #Salva como filename + target, sendo target = .png
                im.save(target_directory + filename + target)
        except OSError:
                print(OSError)

#Função que plota as imagens e mostra na tela
#Utilizei para baixar uma imagem só com todas as imagens e seus respectivos valores de K
def displayImages():
    K = [5,10,20,40,60,80,128]
    for file in listdir('./imgs'):
        fig, axes = plt.subplots(4, 2, figsize=(8, 16))  # Create a 4x2 grid for images
        filename, extension = splitext(file)
        j=0
        for i in K:
            img_path = f'./rslts/{filename}_k{i}{extension}'
            img = plt.imread(img_path)
            axes[j // 2, j % 2].imshow(img)
            axes[j // 2, j % 2].axis('off')
            axes[j // 2, j % 2].set_title(f"K: {i}", fontsize=12)
            j+=1
        img_path = './imgs/' + file
        img = plt.imread(img_path)
        axes[j // 2, j % 2].imshow(img)
        axes[j // 2, j % 2].axis('off')
        axes[j // 2, j % 2].set_title(f"Original", fontsize=12)
        plt.tight_layout()
        plt.show()

