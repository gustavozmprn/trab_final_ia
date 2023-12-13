import src.kmeansTrab as kMeans
import src.infos as infos
import utils
import src.infos

def main():
    #Eu utilizei as funções separadamente para construir o relatório, porém se fosse utilizar em ordem e de uma vez só
    #Ficaria mais ou menos assim: 
    utils.toPng()
    for i in (5,10,20,40,60,80,128):
        kMeans.execKMeans(i)
    utils.displayImages()
    infos.allInfos()
if __name__ == '__main__':
    main()