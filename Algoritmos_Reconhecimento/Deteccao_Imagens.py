import cv2
import numpy as np
from Banco_Dados.Operacoes_BD import OperacoesCrud

classificador = cv2.CascadeClassifier("haarcascade-frontalface-default.xml")
classificador_olho = cv2.CascadeClassifier("haarcascade-eye.xml")

camera = cv2.VideoCapture(0)
amostra = 1
numeroAmostras = 25

acoes_dml = OperacoesCrud()
id_usuario = int(acoes_dml.gerar_id_usuario())
nome = input("Digite o seu Nome: ")
while nome == "":
    print("_"*80)
    print("Por favor digite o seu nome.")
acoes_dml.inserir(id_usuario, nome)

largura = 220
altura = 220
print("_"*80)
print("Capturando Fotos...")


while True:
    conectado, imagem = camera.read()
    imagem_cinza = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    faces_detectadas = classificador.detectMultiScale(imagem_cinza, scaleFactor=1.5, minSize=(150, 150))

    for(x, y, l, a) in faces_detectadas:
        cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 0, 255), 2)
        regiao = imagem[y:y + a, x:x + l]
        regiao_cinza_olho = cv2.cvtColor(regiao, cv2.COLOR_BGR2GRAY)
        olhos_detectados = classificador_olho.detectMultiScale(regiao_cinza_olho)
        for ox, oy, ol, oa in olhos_detectados:
            cv2.rectangle(regiao, (ox, oy), (ox + ol, oy + oa), (0, 255, 0), 2)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("Taxa de Iluminosidade: ", np.average(imagem_cinza))
                if np.average(imagem_cinza) > 110:
                    imagemFace = cv2.resize(imagem_cinza[y:y + a, x:x + l], (largura, altura))
                    cv2.imwrite("../fotos/pessoa.{0}.{1}.jpg".format(id_usuario, amostra), imagemFace)
                    print("[Foto {0} capturada com sucesso.]".format(amostra))
                    amostra += 1

    cv2.imshow("Face", imagem)
    cv2.waitKey(1)
    if amostra >= numeroAmostras + 1:
        break
print("Faces Capturadas com sucesso.")
camera.release()
cv2.destroyAllWindows()
