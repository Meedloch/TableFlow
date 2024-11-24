# TableFlow - Devis instantanés pour groupes

Une application web conçue pour simplifier les réservations de tables pour les restaurants, avec des fonctionnalités adaptées pour les clients et les restaurateurs.

---

## **Fonctionnalités**

### **Pour les Clients :**
- Réserver une table avec des options de menu personnalisées.
- Recevoir un devis instantané basé sur le nombre de personnes et les choix de menu.
- Obtenir un numéro unique pour retrouver facilement une réservation.
- Rechercher une réservation par numéro.

### **Pour les Restaurateurs :**
- Gérer les réservations via une base de données centralisée.
- Attribuer automatiquement un numéro unique à chaque réservation.
- Préparer une interface d'administration (en cours de développement).

---

## **Technologies Utilisées**

### **Frontend :**
- **HTML5 / CSS3** : Interface utilisateur responsive.
- **JavaScript (ES6)** : Gestion des interactions dynamiques.
- **Bootstrap 5** : Design moderne et mobile-friendly.

### **Backend :**
- **Python 3.12** : Langage principal.
- **Flask** : Framework pour la gestion des routes et API.
- **Flask-CORS** : Gestion des requêtes cross-origin.

### **Base de Données :**
- **MySQL** : Gestion des données de réservation.

### **Déploiement :**
- **Docker** : Conteneurisation pour un déploiement simplifié.
- **AWS EC2** : Hébergement cloud.

---

## **Installation et Configuration**

### **Prérequis**
- [Docker](https://www.docker.com/) installé.
- Un serveur MySQL fonctionnel (géré par Docker Compose).

### **Étapes d'installation**
1. Clonez le projet :
   ```bash
   git clone https://github.com/votre-utilisateur/votre-repo.git
   cd votre-repo

2. Configurez les variables d'environnement : Créez un fichier .env avec les paramètres suivants :
   ```bash
    DB_HOST=db
    DB_USER=root
    DB_PASSWORD=password
    DB_NAME=reservations
3. Lancez les conteneurs Docker :
    ```bash
   docker-compose up --build
4. Accédez à l'application
    - Frontend : http://ec2-13-53-125-177.eu-north-1.compute.amazonaws.com:8080/
    - Backend API : http://ec2-13-53-125-177.eu-north-1.compute.amazonaws.com:5000/

## **Utilisation**

### **1. Réserver une Table**
- Rendez-vous sur la page de réservation via le frontend (http://localhost:8080).
- Remplissez les informations nécessaires :
  - **Nombre de personnes**.
  - **Choix du menu** : classique, dégustation, avec ou sans supplément vin.
  - **Date et heure** : dans les horaires disponibles du restaurant.
  - **Coordonnées** : nom, prénom, e-mail et numéro de téléphone.
- Cliquez sur "Réserver". Vous serez redirigé vers une page contenant un numéro de réservation unique et un récapitulatif des détails.

### **2. Rechercher une Réservation**
- Sur la page d'accueil, utilisez le champ de recherche prévu pour les réservations.
- Entrez le numéro unique de réservation fourni lors de la confirmation.
- Les détails de la réservation s'afficheront, incluant :
  - Nombre de personnes.
  - Options de menu choisies.
  - Date et heure de réservation.
  - Coordonnées du client.

### **3. Administration (à venir)**
- Une interface dédiée sera disponible pour les restaurateurs :
  - **Consulter** toutes les réservations.
  - **Rechercher** une réservation spécifique par numéro, e-mail ou nom.
  - **Annuler ou modifier** des réservations.

## **Auteurs**

- **Olivier CHABAUT**

### Remerciements
Un grand merci à toutes les personnes ayant contribué à ce projet ou offert leur soutien, conseils et retour d'expérience.

