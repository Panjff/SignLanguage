# SignLanguage
# I. Logiciel à installer 
  1. Anaconda
     
     https://www.anaconda.com/download/
     
     ![image](https://github.com/Panjff/SignLanguage/assets/153745637/8cc585a1-e378-4a63-9e73-69f9b1113b88)

  3. Vs code

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

  1. Créer la base de donnnées
     
     On crée un ROI (région d'intéret) où nous effectuerons nos signes.
     Pendant les 120 premieres images, on calcule l'arriere plan moyen pour la soustraction d'arrière-plan.
     
     ![image](https://github.com/Panjff/SignLanguage/assets/153745637/7f60ad65-b20a-4538-a2df-7b3c4adf84b3)


     Ensuite, on laisse 300 images le temps d'effectuer le signe voulu.
     Enfin après avoir fait le signe voulu, on l'enregistre dans notre répertoire.
     
     ![image](https://github.com/Panjff/SignLanguage/assets/153745637/2405d1d5-34fc-4286-a619-61ca7f2c4fe6)


     (Attention c'est à vous de spécifier le répertoire dans le code où vous voulez enregistrer les images).
      
![image](https://github.com/Panjff/SignLanguage/assets/153745637/2d0003f7-e614-48c3-b1ae-35977be5a85d)

    
  Ainsi, nous avons notre base de données que nous avons split en 2, l'un dans un dossier "test" et l'autre dans un dossier "train".

 ![image](https://github.com/Panjff/SignLanguage/assets/153745637/3398cded-f3c5-418f-b6c0-b965f4e3e862)


  2. Créer le réseau de neuronnes et entrainer

      

     
  3. Résultats
     
     Malgrès 1200 images par signes, la détection n'est pas optimal. 

# Conclusion :


