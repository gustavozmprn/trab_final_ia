import cv2
from os import listdir
from os.path import splitext
import numpy as np

#Função que aplica o Kmeans separadamente
def kMeans(im, im_vet, K, criteria):
    #Utilizei os valores que já estavam no exemplo do kmeans do cv2
    attempts = 10
    #Executa o kmeans do próprio cv2, ret, label e center já eram as variáveis presentes no exemplo que peguei
    ret,label,center = cv2.kmeans(im_vet,K,None,criteria, attempts, cv2.KMEANS_PP_CENTERS)
    center = np.uint8(center)
    res = center[label.flatten()]
    return res.reshape(im)


def execKMeans(K):
    #Criteria também já estava assim no exemplo do cv2
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    #Itera entre as imagens presentes no dir imgs
    for file in listdir('./imgs'):
        filename, extension = splitext(file)
        try:
            if (extension == '.png'):
                #Lê a imagem
                img = cv2.imread(f'imgs/{filename}{extension}')
                #Tenta converter de BGR pra RGB
                img_convert = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
                img.shape
                vectorized = img.reshape(-1,3)
                vectorized = np.float32(vectorized)
                #Pra cada valor de K ele tenta aplicar o Kmeans chamando a função acima e escrevendo já no dir rslts
                for index in [K] :
                    cv2.imwrite(f'rslts/{filename}_k{index}{extension}', kMeans(img_convert.shape, vectorized, index, criteria))
        except OSError:
            print('Problema ao tentar executar o kmeans na imagem: %s' % file)