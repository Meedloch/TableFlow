# Utiliser une image Python
FROM python:3.13

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers
COPY . .

# Installer les dépendances
RUN pip install -r requirements.txt

# Exposer le port
EXPOSE 5000

# Commande pour démarrer l'application
CMD ["python", "run.py"]
