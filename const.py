FILENAME = "members.db"
APP_NAME="MyApp"
TABLE="members"

# Fonts

FONT_TITLE = ("Arial", 21, "bold")
FONT_MESSAGE = ("Arial", 17, "bold")
FONT_LABEL = ("Arial", 7)

# Colors
DARKGREY = "#ABABAB"
LIGHTWHITE = "#EFEFEF"
GREEN = "#00FF00"
RED = "#FF0000"
ORANGE = "#EE9524"

# attributs
ID="id"
FIRST_NAME="Prenom"
LAST_NAME="nom"
GENDER="Sexe"
BIRTHDAY="Anniversaire"
START_SUBSCRIBE="Debut souscription"
END_SUBSCRIBE="Fin souscription"
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
MSG_INVALID_NAME="le prénom ou le nom de la personne ne respect aps le bon format. (lettres uniquement)"
MSG_INVALID_GENDER="Le"
MSG_INVALID_BIRTHDAY="Personne birthday is not valid"
MSG_INVALID_SUSCRIPTION="Subscription dates are not valid"
MSG_INVALID_ZIPCODE="ZIP code is not valid"
MSG_INVALID_EMAIL="Email is not valid"
MSG_INVALID_PHONE="Phone is not valid"

# Widgets text
TXT_EXIT="Quitter"
TXT_BACK="Retour"
TXT_ADD="Ajouter"

# List
LIST_GENDER = ["Homme","Femme"]
LIST_ROLE = ["Inscript","Administration"]
LIST_RELATIONSHIP = ["Célibataire","Marié(e)"]

# Regex
# REGEX_EMAIL = 

# Key
KEY_ALERT="Alert"

# design
BUTTON_STYLE = {
    "bg":"#333333",
    "fg":LIGHTWHITE
}

ROOT_STYLE = {
    "bg":DARKGREY
}

ALERT_STYLE = {
    "bg":DARKGREY,
    "font":FONT_MESSAGE
}

LABEL_STYLE = {
    "font":FONT_LABEL,
    "bg":DARKGREY,
}