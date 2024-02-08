# Utilisez une image de base avec Python
FROM python:3.9

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez le contenu local dans le conteneur à /app
COPY . /app

# Installez les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Spécifiez la commande à exécuter lors du démarrage du conteneur
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app_with_mongo:app", "-w", "4"]

