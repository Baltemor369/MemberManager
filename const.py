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
START_SUSCRIPTION="date inscription"
END_SUSCRIPTION="date expiration"
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

# Values
VAL_EMPTY=""
VAL_ADD="Add"
VAL_MODIFY="Modify"

# Messages
MSG_ADD_SUCCESS="Personne ajouté avec succès"
MSG_MODIFY_SUCCESS="Personne modifié avec succès"
MSG_DEL_SUCCESS="Personne supprimé avec succès"
MSG_INVALID_NAME="Prenom ou nom : format invalide (lettre et \"-' \" uniquement)"
MSG_INVALID_GENDER="Genre : saisi invalide, sélectionnez dans la liste."
MSG_INVALID_BIRTHDAY="Date de naissance : format invalide jj/mm/AAAA"
MSG_INVALID_SUSCRIPTION="Date d'inscription ou d'expiration : format invalide jj/mm/AAAA"
MSG_INVALID_ADDRESS="Adresse : saisi vide"
MSG_INVALID_CITY="Ville : saisi vide"
MSG_INVALID_ZIPCODE="Code postal : format invalide (5 chiffres)"
MSG_INVALID_EMAIL="Email : format invalide"
MSG_INVALID_PHONE="Telephone : format invalide (10 chiffres)"
MSG_INVALID_JOB="Métier : format invalide."
MSG_INVALID_RELATIONSHIP="Situation : saisi invalide, sélectionnez dans la liste."
MSG_INVALID_KIDS="Nombre enfant : saisi invalide, sélectionnez dans la liste."
MSG_INVALID_MEMBERSHIP="Erreur : avec l'id, contacter l'administrateur."
MSG_INVALID_ROLE="Role : Saisi invalide, sélectionnez dans la liste."
MSG_NO_SELECTION="Aucune selection"
MSG_USER_NOT_FIND="Erreur : personne introuvable, contacter l'administrateur."

# Widgets text
TXT_EXIT="Quitter"
TXT_BACK="Retour"
TXT_ADD="Ajouter"
TXT_DEL="Supprimer"
TXT_MODIFY="Modifier"

# List
LIST_GENDER = ["Homme","Femme"]
LIST_ROLE = ["Inscript","Administration"]
LIST_RELATIONSHIP = ["Célibataire","Marié(e)"]

# Regex
REGEX_EMAIL = ""

# Key
KEY_ALERT="Alert"
KEY_FORM="Form"
KEY_USER="User"

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