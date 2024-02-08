from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from pymongo.server_api import ServerApi



def info_allocine():
    
    uri = "mongodb+srv://aurelienbenoit9:<password>@cluster0.jlhbxbj.mongodb.net/?retryWrites=true&w=majority"
    # Create a new client and connect to the server
    client = MongoClient(uri, username = "aurelienbenoit9" , password = "mdp")
    # Send a ping to confirm a successful connection
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
    
    db = client['allocine']  # Remplacez par le nom de votre base de données
    collection = db['films2']  # Remplacez par le nom de votre collection
    

    url = "https://www.allocine.fr/seance/salle_gen_csalle=B9114.html"
    response = requests.get(url)


    if response.status_code == 200:
        app.logger.info("222")

        soup = BeautifulSoup(response.text, 'html.parser')
        

        resultats = []
        films  = collection.find()
        for film in films :
            resultats.append({"nom_film": film['nom_film'], "image_url": film['image_url'], "horaires": film['horaires'], "content-text" : film['content-text']})

       
        
        client.close()
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
    print("4")
    resultats = info_allocine()
    app.logger.info(resultats)
    return render_template('index.html', resultats=resultats)

if __name__ == '__main__':
    app.run(debug=True)