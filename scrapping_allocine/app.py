from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient



def scrape_allocine():
    
    url = "https://www.allocine.fr/seance/salle_gen_csalle=B9114.html"
    response = requests.get(url)

     # Connexion à la base de données MongoDB
    #uri = "mongodb+srv://aurelienbenoit9:<password>@cluster0.jlhbxbj.mongodb.net/?retryWrites=true&w=majority"
    # Create a new client and connect to the server
    #client = MongoClient(uri, username = "aurelienbenoit9" , password = "mdp")
    #db = client['allocine']  
    #collection = db['films2']  
    
    

    if response.status_code == 200:
        
        soup = BeautifulSoup(response.text, 'html.parser')
        films = soup.find_all('div', class_='card entity-card entity-card-list movie-card-theater cf hred')
        resultats = []
        for film in films:
            
            genre_films =  [horaire.text.strip() for horaire in film.find_all('span', class_='showtimes-hour-item-value')]
            nom_film = film.find('h2', class_='meta-title').text.strip()
            # Récupérer l'URL de l'image à partir de la classe 'thumbnail-img'
            image_tag = film.find('img', class_='thumbnail-img')
            #content_text = film.find('div', class_='synopsis')
            try:
                content_text = film.find('div', class_='synopsis').find('div', class_='content-txt').text.strip()
            except AttributeError as e:
                # Si la balise ou la classe n'est pas trouvée, cela générera une exception AttributeError
                # Vous pouvez imprimer un message d'erreur ou assigner une valeur par défaut au texte, selon vos besoins.
                print(f"Une erreur s'est produite lors de la récupération du texte : {e}")
                content_text = None  # ou une valeur par défaut

            #image_url = image_tag['src'] if image_tag else None
            image_url = image_tag.get('data-src') if image_tag else None
            image_url = image_tag.get('src') if image_url is None else image_url
            
            
            horaires = [horaire.text.strip() for horaire in film.find_all('span', class_='showtimes-hour-item-value')]

            # Critère de recherche pour le nom du film
            resultats.append({"nom_film": nom_film, "image_url": image_url, "horaires": horaires, "content-text" : content_text})

        
        
        #collection.insert_many(resultats)
        return resultats
    else:
        print(3)
        return None
    
    
app = Flask(__name__)

if __name__ == '__main__':
    # Spécifiez le port ici, par exemple 8000
    app.run(host='0.0.0.0', port=5000)

# Route pour la page d'accueil
@app.route('/')
def accueil():
    # Utilise la fonction de scraping
    print("1")
    resultats = scrape_allocine()
    
    return render_template('index.html', resultats=resultats)

if __name__ == '__main__':
    app.run(debug=True)