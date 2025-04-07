from jwt_generator import JWTGenerator
import jwt  # Assurez-vous d'avoir installé la bibliothèque PyJWT

# Token JWT fourni
token = "eyJhbGciOiJSUzUxMiIsInR5cCI6IkpXVCIsImtpZCI6IjE2MTM2Mzc2NTYiLCJvcmcuYXBlcmVvLmNhcy5zZXJ2aWNlcy5SZWdpc3RlcmVkU2VydmljZSI6IjQwMCJ9.eyJzdWIiOiJhMDQ4N19wZnMiLCJyb2xlcyI6W10sImlzcyI6Imh0dHBzOi8vYXV0aC5wcGFsbS5mci9vaWRjIiwibm9uY2UiOiIiLCJjbGllbnRfaWQiOiJhMDQ4N19wZnMiLCJhdWQiOiJhMDQ4N19wZnMiLCJncmFudF90eXBlIjoiY2xpZW50X2NyZWRlbnRpYWxzIiwicGVybWlzc2lvbnMiOltdLCJzY29wZSI6W10sInNjb3BlcyI6W10sInN0YXRlIjoiIiwiZXhwIjoxNzQ0MDEwOTgyLCJpYXQiOjE3NDQwMTA2ODIsImp0aSI6IkFULTEwMjgwLS1hVjB0b0hNdXJwenZCdFVJZ0VYOG50Vi1VVzF4SUVLIn0.aN-VUoh4YW3B__Jj7UnGp-zI2pClYgesxtjzy4nGSAvAV6rmQPyh2NVKa5jS28YMJc0P_yuOjxrDJ5kB3So24TyDSq4ZvHpfwyxdojF1qdAS4OwrMPU13FU19LsTWq3OX4BpV5YxgZH3y1eArsibYkUOEgEYNoZTfUO_mj1-ov77AzUnGyodrpKBETdHqHG41DctvOhmbrNGI9vcc0joCv_iE9mM9M5Pkc1TjWdj009RbWj0Kw4PkAjI1kggzMDrA0oIefR_IJMyYZhvX4xY5nRtm4g1tBDpjVGBxLZGK6dfhvWEB6m6xuFASPro4chI8eVVzOMfGHXf50M4ZakhOA"

# Fonction pour décoder le JWT sans vérification
def decode_jwt_without_verification(token, algorithms=["RS256"]):
    """
    Décoder un JWT sans vérifier la signature.

    Args:
        token (str): Le token JWT à décoder.
        algorithms (list): Liste des algorithmes à utiliser pour le décodage.

    Returns:
        dict: Le payload décodé du JWT.
        dict: Les headers du JWT.

    Raises:
        ValueError: Si le décodage échoue.
    """
    try:
        # Récupération des headers
        headers = jwt.get_unverified_header(token)
        # Décodage du payload sans vérification
        payload = jwt.decode(token, options={"verify_signature": False}, algorithms=algorithms)
        return headers, payload
    except Exception as e:
        raise ValueError(f"Erreur lors du décodage du JWT : {e}")

# Test de décodage
def test_decode():
    try:
        # Décodage sans vérification pour le token spécifié
        headers, payload_no_verify = decode_jwt_without_verification(token)
        print("Headers du JWT :", headers)
        print("Payload décodé sans vérification :", payload_no_verify)
    except ValueError as e:
        print("Erreur :", e)

# Exemple d'utilisation
if __name__ == "__main__":
    # Charger la clé privée depuis le fichier
    with open("private_key.pem", "r") as key_file:
        private_key = key_file.read()

    # Initialiser le générateur de JWT
    generator = JWTGenerator(private_key)

    # Payload exemple
    payload = {
        "sub": "1234567890",
        "name": "John Doe",
        "admin": True
    }

    # Générer un token
    token = generator.generate_token(payload)
    print("Token généré :", token)

    # Test de décodage
    test_decode()