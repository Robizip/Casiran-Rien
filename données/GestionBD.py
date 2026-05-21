import sqlite3 # Interaction avec la base de donnée
from hashlib import pbkdf2_hmac # Pour générer le mot de passe hashé
from hmac import compare_digest # Pour vérifier au niveau de la connection si le mot de passe est bon
from os import urandom # Pour générer le sel aléatoire nécessaire pour hashlib

base_donnee = sqlite3.connect("données/BaseDonnéeCasino.db")
curseur = base_donnee.cursor()

#------------------------------------------------------------------------
#Verifier si un pseudo existe déjà
def VerificationCompte(pseudo):
    verification = curseur.execute(
        """
        SELECT 1
        FROM Base_Données_Comptes
        WHERE Pseudo = ?
        """,
        (pseudo,))
    
    return verification.fetchone() != None 
#------------------------------------------------------------------------
#Créer un compte
def CreationCompte(pseudo,mdp,nom,prenom):
    sel = urandom(16) # Génération d’un sel aléatoire. Est en bytes.
    # Hashage du mot de passe
    mdp_chiffre = pbkdf2_hmac("sha256", mdp.encode(), sel, 100_000)

    curseur.execute(
        """
        INSERT INTO Base_Données_Comptes
        (Identifiant, Pseudo, MotDePasse, Nom, Sel, Prénom, Argent)
        VALUES (NULL, ?, ?, ?, ?, ?, ?)
        """,
        (pseudo,mdp_chiffre,nom,sel,prenom,0))
    base_donnee.commit()
#------------------------------------------------------------------------
#Se connecter à un compte
def ConnexionCompte(pseudo,mdp) :
        verification = curseur.execute(
        "SELECT MotDePasse, Sel FROM Base_Données_Comptes WHERE Pseudo = ?",
        (pseudo,)).fetchone() # Récupération d’un éventuel mot de passe hashé avec son sel d’après un pseudo donné

        if not verification : # Si le compte n’existe pas
            return False
        hash_stocke, sel = verification

        # Hashage du texte entré dans le champ du mot de passe dans la connexion
        nouveau_hash = pbkdf2_hmac("sha256", mdp.encode(), sel, 100_000)

        return compare_digest(hash_stocke,nouveau_hash) # Vérification finale pour savoir si le mot de passe est correct.

#------------------------------------------------------------------------
#Récupérer l’argent du compte connecté
def RecupArgent(compte) :
    argent_stock_compte = curseur.execute("""
                                            SELECT Argent
                                            FROM Base_Données_Comptes
                                            WHERE Pseudo = ?""",
                                            (compte,)).fetchone()
    if argent_stock_compte :
        return argent_stock_compte[0]
    else :
        return 0
#------------------------------------------------------------------------
#Update l’argent du compte connexté
def AjoutArgent(ajout,compte) :
    curseur.execute(
        """
        UPDATE Base_Données_Comptes
        SET Argent = Argent + ?
        WHERE Pseudo = ?
        """,
       (ajout, compte)
    )
    base_donnee.commit()
#------------------------------------------------------------------------