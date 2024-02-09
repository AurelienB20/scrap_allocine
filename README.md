# scrap_allocine

Introduction
Bienvenue dans le projet de scrapping en temps réel avec MongoDB. Ce projet offre deux versions distinctes pour répondre à vos besoins spécifiques. Vous pouvez choisir entre la version avec scrapping en temps réel et la version avec intégration MongoDB pour stocker les données.

Instructions d'utilisation :
Clonez le dépôt : git clone https://github.com/AurelienB20/scrap_allocine.git
cd scrap_allocine

Versions Disponibles
1. Scrapping en Temps Réel
La version avec scrapping en temps réel permet de collecter les données en temps réel à partir de différentes sources. Cette approche offre une mise à jour instantanée des informations et est idéale pour les projets nécessitant des données en temps réel.
cd scrapping_allocine

creation de l'image 
docker build -t scrap_img .

creation du container 
docker run --name allocine_container -p 5000:5000 -it scrap_img

pour voir le resultat connectez vous sur votre navigateur à localhost:5000 

si vous voulez stopper le conteneur sans le supprimer 
docker stop allocine_container

et pour le relancer 
docker start allocine_container

2. Intégration MongoDB
La version avec intégration MongoDB offre la possibilité de stocker les données scrappées dans une base de données MongoDB. Cela permet une gestion efficace des données et facilite l'analyse à long terme.

cd scrapping_allocine_with_mongo

creation de l'image 
docker build -t scrap_img_with_mongo .

creation du container 
docker run --name allocine_container_with_mongo -p 5000:5000 -it scrap_img_with_mongo

pour voir le resultat connectez vous sur votre navigateur à localhost:5000 

si vous voulez stopper le conteneur sans le supprimer 
docker stop allocine_container_with_mongo

et pour le relancer 
docker start allocine_container_with_mongo







choix techniques

flask 

Le choix de Flask pour une application web de scraping sur Allociné peut se justifier par sa légèreté, sa simplicité, sa facilité d'apprentissage, son intégration aisée avec le web scraping en Python, sa flexibilité, une communauté active, un déploiement facile, et la possibilité de créer rapidement des API REST. En résumé, Flask offre une approche minimaliste et efficace pour des projets web de taille modérée.

mongo db 

Nous avons choisi MongoDB car c'est un choix adapté pour le scraping sur Allociné en raison de sa flexibilité de stockage de données non structurées, de son modèle sans schéma fixe, de son évolutivité horizontale, de son langage de requête basé sur JSON, de son indexation, et de son large usage industriel avec une communauté active.

scrapping en temps reel 

Le choix du scraping en temps réel a été privilégié pour garantir des données instantanément mises à jour depuis Allociné, assurant ainsi une réactivité optimale de l'application. Cette approche permet également une automatisation continue, une adaptation aisée aux changements du site, et une minimisation des délais entre la publication des données et leur disponibilité pour les utilisateurs.



