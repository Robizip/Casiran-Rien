import sqlite3
import os
import hashlib
import hmac

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
    sel = os.urandom(16)
    mdp_chiffre = hashlib.pbkdf2_hmac(
        "sha256",
        mdp.encode(),
        sel,
        100_000)

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
        (pseudo,)).fetchone()

        if not verification :
            return False
        hash_stocke, sel = verification

        nouveau_hash = hashlib.pbkdf2_hmac(
        "sha256",
        mdp.encode(),
        sel,
        100_000)

        return hmac.compare_digest(hash_stocke,nouveau_hash)

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