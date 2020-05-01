import cv2
import numpy as np
import os

eigenface = cv2.face.EigenFaceRecognizer_create(num_components=50, threshold=10202)
fisherface = cv2.face.FisherFaceRecognizer_create()
lbph = cv2.face.LBPHFaceRecognizer_create()


def get_imagem_com_id():
    caminhos = [os.path.join("../fotos", f) for f in os.listdir("../fotos")]
    # print(caminhos)
    faces = []
    ids = []
    for caminho_imagens in caminhos:
        imagem_face = cv2.cvtColor(cv2.imread(caminho_imagens), cv2.COLOR_BGR2GRAY)
        id = int(os.path.split(caminho_imagens)[-1].split('.')[1])
        print(id)
        ids.append(id)
        faces.append(imagem_face)
        cv2.imshow("Face", imagem_face)
        cv2.waitKey(10)
    return np.array(ids), faces


ids, faces = get_imagem_com_id()
# print(ids)
# print(faces)

print("_" * 80)
print("Treinamento....")
eigenface.train(faces, ids)
eigenface.write("classificadorEigen.yml")

fisherface.train(faces, ids)
fisherface.write("classificadorFisher.yml")

lbph.train(faces, ids)
lbph.write("classificadorLBPH.yml")
print("_" * 80)
print("Treinamento realizado...")
