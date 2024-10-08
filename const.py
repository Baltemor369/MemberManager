FILENAME = "members.db"
APP_NAME="MyApp"
TABLE="members"

# Fonts
FONT_TITLE = ("Arial", 21, "bold")
FONT_MESSAGE = ("Arial", 17, "bold")
FONT_LABEL = ("Arial", 7, "bold")

# Colors
DARKGREY = "#ABABAB"
LIGHTWHITE = "#EFEFEF"
GREEN = "#00FF00"
RED = "#FF0000"
ORANGE = "#EE9524"
LIGHTBLUE = "#45ABFF"
BLACK="#000000"

# attributs
ID="id"
FIRST_NAME="Prenom"
LAST_NAME="nom"
GENDER="Genre"
BIRTHDAY="Anniversaire"
START_SUBSCRIBE="date inscription"
END_SUBSCRIBE="date expiration"
ADDRESS="Adresse"
CITY="Ville"
ZIPCODE="Code postal"
EMAIL="Email"
PHONE="Telephone"
JOB="Metier"
RELATIONSHIP_SITUATION="Situation"
NB_KIDS="Nb enfants"
MEMBERSHIP_NUMBER="Identifiant"
MEMBERSHIP_ROLE="Role"

# Messages
MSG_ADD_SUCCESS="Personne ajouté avec succès"
MSG_INVALID_NAME="Prenom ou nom : format invalide (lettre uniquement)"
MSG_INVALID_GENDER="Genre : format invalide ('Homme','Femme')"
MSG_INVALID_BIRTHDAY="Date de naissance : format invalide ('01-01-2001')"
MSG_INVALID_SUSCRIPTION="Date d'inscription ou d'expiration : format invalide ('01-01-2001')"
MSG_INVALID_ADDRESS="Adresse : saisi vide"
MSG_INVALID_CITY="Ville : saisi vide"
MSG_INVALID_ZIPCODE="Code postal : format invalide (5 chiffres)"
MSG_INVALID_EMAIL="Email : format invalide"
MSG_INVALID_PHONE="Telephone : format invalide (10 chiffres)"
MSG_INVALID_JOB="Métier : saisi vide"
MSG_INVALID_RELATIONSHIP="Situation : saisi vide"
MSG_INVALID_KIDS="Nombre enfant : saisi vide"
MSG_INVALID_MEMBERSHIP="Id : error"
MSG_INVALID_ROLE="Role : saisi vide"
MSG_NO_SELECTION="Aucune selection"

# Widgets text
TXT_EXIT="Quitter"
TXT_BACK="Retour"
TXT_ADD="Ajouter"
TXT_DEL="Supprimer"

# List
LIST_GENDER = ["Homme","Femme"]
LIST_ROLE = ["Inscript","Administration"]
LIST_RELATIONSHIP = ["Célibataire","Marié(e)"]

# Regex
REGEX_EMAIL = ""

# Key
KEY_ALERT="Alert"

# design
BUTTON_STYLE = {
    "bg":"#333333",
    "fg":LIGHTWHITE,
    "width":9
}

ROOT_STYLE = {
    "bg":LIGHTBLUE
}

ALERT_STYLE = {
    "bg":LIGHTBLUE,
    "font":FONT_MESSAGE
}

LABEL_STYLE = {
    "font":FONT_LABEL,
    "bg":LIGHTBLUE,
}