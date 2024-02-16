# SignLanguage
# I. Logiciel à installer 
  # 1. Anaconda
     
   Voici le lien pour télécharger Annaconda: https://www.anaconda.com/download/
     
   ![image](https://github.com/Panjff/SignLanguage/assets/153745637/8cc585a1-e378-4a63-9e73-69f9b1113b88)

  # 2. Vs code

  Voici le lien pour télécharger visual studio code: https://code.visualstudio.com/download/
     
  ![image](https://github.com/Panjff/SignLanguage/assets/153745637/1e45f00e-7600-417d-86f5-6ed40388370b)


# II. Configuration

  Apres l'installation de Annaconda, ouvrir Anaconda prompt et executer les commandes suivantes:
  
  ![image](https://github.com/Panjff/SignLanguage/assets/153745637/3d275f7d-2545-4409-97c5-10ae07fa4f39)
  
  conda create --name SignLanguage
  
  conda activate SignLanguage
  
  conda install tensorflow
  
  pip install opencv-python numpy matplotlib tensorflow keras

  Ensuite, ouvrir vs code 

  ![image](https://github.com/Panjff/SignLanguage/assets/153745637/06e41a48-6151-401f-a382-840e47ab2cde)

  Ouvrir le dossier contenant le projet et enfin selectionner l'interpret python

  ![image](https://github.com/Panjff/SignLanguage/assets/153745637/e9130800-60c1-4204-976d-4810304e2b2c)

  
  ![image](https://github.com/Panjff/SignLanguage/assets/153745637/794fe8fe-17b5-4d1c-bfa5-fe7c67cc0596)

  Si vous ne trouvez pas l'interpret conda python précédemment créé, appuiyer sur "Enter a interpret path" et mettez le chemin de l'environnement conda .


# III. Explications sur le code 

Pour permettre la detection de signe en temps réel, il faut respecter 3 étapes:

  -Créer une base de données des signes à interpreter
  
  -Créer un réseau de neuronnes traitant notre base de données
  
  -Entrainer ce réseau de neuronnes

Après cela, nous pourrons détecter les signes voulus.

  # 1. Créer la base de donnnées
     
  Pour la ceeation de la base de données, on génerre un ROI (région d'intéret) où nous effectuerons nos signes.
  Pendant les 120 premieres images, on calcule l'arriere plan moyen pour la soustraction d'arrière-plan.
     
  ![Capture d'écran 2024-02-13 174027](https://github.com/Panjff/SignLanguage/assets/153745637/69fe8f80-69d5-415f-93d8-63c25d0a2d99)


  Ensuite, on laisse 300 images le temps d'effectuer le signe voulu.
  Enfin après avoir fait le signe voulu, on l'enregistre dans notre répertoire.
     

![Capture d'écran 2024-02-13 174140](https://github.com/Panjff/SignLanguage/assets/153745637/f84ae54c-decf-4ef8-ac4f-4145669db083)

  (Attention c'est à vous de spécifier le répertoire dans le code où vous voulez enregistrer les images).
      
![Capture d'écran 2024-02-13 174217](https://github.com/Panjff/SignLanguage/assets/153745637/4dc2acb4-1cbe-4b2f-8292-7e7121b2c76b)

    
  Ainsi, nous avons notre base de données que nous avons split en 2, l'un dans un dossier "test" et l'autre dans un dossier "train".

![Capture d'écran 2024-02-13 174259](https://github.com/Panjff/SignLanguage/assets/153745637/42888d35-38a3-4589-8522-a5ef9c0a3ee7)


  # 2. Créer le réseau de neuronnes et entrainer

  Les chemins des répertoires contenant les données d'entraînement et de test étant spécifiés, les images sont chargées en utilisant "ImageDataGenerator" avec une taille cible de (64,64) et une augmentation des données.
La création du modèle CNN débute par l'initialisation d'un modèle séquentiel. Ensuite, des couches de convolution, de max pooling et de couches denses sont successivement ajoutées pour construire le réseau de neurones convolutionnel (CNN). La compilation du modèle se fait en utilisant l'optimiseur Adam et la fonction de perte d'entropie croisée catégorielle.
Lors de l'entraînement du modèle, des "callbacks" sont des mécanismes qui peuvent ajuster certains aspects du processus d'apprentissage. Dans ce cas, deux callbacks sont utilisés : l'un pour réduire dynamiquement le taux d'apprentissage pendant l'entraînement, et l'autre pour arrêter prématurément l'entraînement si la performance sur les données de validation ne s'améliore pas. Le modèle est ensuite entraîné sur un ensemble de données spécifié pendant un certain nombre de cycles d'apprentissage, avec des données distinctes utilisées pour évaluer sa progression.
L'évaluation du modèle se fait en le testant sur les données spécifiées pour évaluer sa performance. Après l'entraînement, le modèle est sauvegardé, permettant ainsi son utilisation ultérieure.
Le modèle sauvegardé est chargé pour effectuer des prédictions ou une évaluation ultérieure. Ensuite, le modèle est réévalué sur les données de test pour vérifier la reproductibilité des résultats. 
Les prédictions du modèle sont ensuite affichées pour une petite série de données de test, et les étiquettes réelles correspondantes sont également affichées pour permettre la comparaison avec les prédictions du modèle. 

     
  # 3. Résultats
     
![Capture d'écran 2024-02-15 101359](https://github.com/Panjff/SignLanguage/assets/153745637/5fc65ed6-7750-4278-9814-6e11cd5527d1)

![416499004_1357577541590979_3024127245628409564_n](https://github.com/Panjff/SignLanguage/assets/153745637/5956f89d-19d6-447e-a467-d76f640f2494)

![426187557_1586242762201228_9112263679554463180_n](https://github.com/Panjff/SignLanguage/assets/153745637/85c58b62-d9a5-4c6e-a466-63351d7f2889) 

# Conclusion :

  Malgrès 1200 images par signes, la détection n'est pas optimal meme si on arrive à detecter les signes. Pour avoir un résultat optimal, il faudra essayer un autre méthode pour la création du réseau de neurones.

