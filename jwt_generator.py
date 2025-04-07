from typing import Dict
import datetime
import jwt  # Ajout de la bibliothèque PyJWT


class JWTGenerator:
    def __init__(self, private_key: str, algorithm: str = "RS256"):
        """
        Initialise le générateur de JWT.

        Args:
            private_key (str): La clé privée pour signer le JWT.
            algorithm (str): L'algorithme de signature (par défaut RS256).
        """
        self.private_key = private_key
        self.algorithm = algorithm

    def generate_token(self, payload: Dict, expiration_minutes: int = 60) -> str:
        """
        Génère un token JWT signé.

        Args:
            payload (dict): Les données à inclure dans le payload du JWT.
            expiration_minutes (int): Durée de validité du token en minutes (par défaut 60).

        Returns:
            str: Le token JWT signé.
        """
        # Ajouter l'heure d'expiration au payload
        payload["exp"] = datetime.datetime.utcnow() + datetime.timedelta(minutes=expiration_minutes)
        payload["iat"] = datetime.datetime.utcnow()

        # Générer le token signé
        token = jwt.encode(payload, self.private_key, algorithm=self.algorithm)
        return token