import cv2
import os
from os import listdir
from os.path import splitext
from PIL import Image

#Contém as funções que fiz para pegar as informações das imagens

#Pega as informações de uma imagem separada, passando a imagem e possivelmente o path dela
def imgInfo(file, path):
    #Se não existir path ele vai tentar pegar a imagens do diretório rslts
    if path == None:
        image_path = f"./rslts/{file}"
    else:
        image_path = path
    im = cv2.imread(image_path)
    #Faz uma tupla (ou N-upla nesse caso com 5 infos) e retorna
    infos = file + "png", round(os.path.getsize(image_path)/1024/1024,3), im.shape[1], im.shape[0], uniqueColors(image_path)
    return infos
    

#Mesma lógica da função acima, unica diferença é que itera pelas imagens de um diretório em específico
#Deixei como imgs pois as ultimas infos que peguei foram das imagens presentes nesse diretório
def allInfos():
    for file in listdir('./imgs'):
        filename, extension = splitext(file)
        im = cv2.imread(f"./imgs/{filename}{extension}")
        infos = filename + extension, round(os.path.getsize(f'./imgs/{filename}{extension}')/1024/1024,3), im.shape[1], im.shape[0], uniqueColors(f"./imgs/{filename}{extension}")
        print(infos)

#Função que lista as cores unicas
def uniqueColors(image_path):
    #Abre a imagem
    img = Image.open(image_path)
    #Converte pra RGB (Se for os resultados já vai estar em RGB no lugar de BGR prob)
    img = img.convert('RGB')
    #width e height
    width, height = img.size
    #cria um set pra salvar o valor único das cores
    unique_colors = set()
    #Itera entre o width e height adicionando as cores no set, quando a cor já foi adicionada só soma
    for y in range(height):
        for x in range(width):
            pixel = img.getpixel((x, y))
            unique_colors.add(pixel)
    #Retorna o tamanho do set
    return len(unique_colors)
