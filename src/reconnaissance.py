from image import Image
import numpy as np

def lecture_modeles(chemin_dossier):
    fichiers= ['_0.png','_1.png','_2.png','_3.png','_4.png','_5.png','_6.png', 
            '_7.png','_8.png','_9.png']
    liste_modeles = []
    for fichier in fichiers:
        model = Image()
        model.load(chemin_dossier + fichier)
        liste_modeles.append(model)
    return liste_modeles


def reconnaissance_chiffre(image, liste_modeles, S):
    vec = []
    liste_modeles = lecture_modeles('../assets/')
    image_binarisee = image.binarisation(S)
    image_localisee = image_binarisee.localisation()
    for i in range(len(liste_modeles)):
        image_resize = image_localisee.resize(liste_modeles[i].H, liste_modeles[i].W)
        score = image_resize.similitude(liste_modeles[i])
        vec.append(score)
    result = np.where(vec == np.amax(vec))
    return int(result[0][0])

