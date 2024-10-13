FILENAME = "members.db"
APP_NAME="MyApp"
TABLE="members"

# Fonts
FONT_TITLE = ("Arial", 17, "bold")
FONT_MESSAGE = ("Arial", 17, "bold")
FONT_LABEL = ("Arial", 13, "bold")

# Colors
DARKGREY = "#ABABAB"
LIGHTWHITE = "#EFEFEF"
GREEN = "#00FF00"
RED = "#FF0000"
ORANGE = "#EE9524"
LIGHTBLUE = "#45ABFF"
BLACK="#000000"

# Database col
DB_ID="ID"
DB_FIRST_NAME="first_name"
DB_LAST_NAME="last_name"
DB_BIRTHDAY_LAST_NAME="day_last_name"
DB_CIVILITY="civility"
DB_NATIONALITY="nationality"
DB_BIRTHDAY="birthday"
DB_BIRTHDAY_LOCATION="birthday_location"
DB_START_SUSCRIPTION="start_subscription"
DB_END_SUSCRIPTION="end_subscription"
DB_ADDRESS="address"
DB_CITY="city"
DB_ZIPCODE="zipcode"
DB_EMAIL="email"
DB_PHONE="phone"
DB_JOB="job"
DB_RELATIONSHIP_SITUATION="relationship"
DB_NB_KIDS="nb_kids"
DB_MEMBERSHIP_FONCTION="member_fonction"
DB_ACTIVITY="ativity"
DB_MEMBERSHIP_NUMBER="member_id"


# attributs
ID="ID"
FIRST_NAME="Prénom"
LAST_NAME="Nom"
BIRTHDAY_LAST_NAME="Nom de naissance"
CIVILITY="Civilité"
NATIONALITY="Nationalité"
BIRTHDAY="Date de naissance"
BIRTHDAY_LOCATION="Lieu de naissance"
START_SUSCRIPTION="Date début"
END_SUSCRIPTION="date fin"
ADDRESS="Adresse"
CITY="Ville"
ZIPCODE="Code postal"
EMAIL="Email"
PHONE="Telephone"
JOB="Metier"
RELATIONSHIP_SITUATION="Situation"
NB_KIDS="Nombre enfants"
MEMBERSHIP_ROLE="Fonction"
ACTIVITY="Activité"
MEMBERSHIP_NUMBER="Identifiant membre"

# Values
VAL_EMPTY=""
VAL_ADD="Add"
VAL_MODIFY="Modify"

# Messages
MSG_ADD_SUCCESS="Personne ajouté avec succès"
MSG_MODIFY_SUCCESS="Personne modifié avec succès"
MSG_DEL_SUCCESS="Personne supprimé avec succès"
MSG_CSV_SUCCESS="Exportation CSV avec succès"
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
MSG_CSV_ERROR="Erreur lors de l'exportation, contacter l'administrateur."
MSG_SAVING_DATA="Erreur lors de la sauvegarde dans la BDD."

# Widgets text
TXT_EXIT="Quitter"
TXT_BACK="Retour"
TXT_ADD="Ajouter"
TXT_DEL="Supprimer"
TXT_MODIFY="Modifier"
TXT_EXPORT="Exporter"
TXT_SEARCH="Rechecher par numéro adhérent :"


# List
LIST_GENDER = ["Homme","Femme"]
LIST_ROLE = ["Président","Vice Président","Secrétaire", "Secrétaire adjoint", "Trésorier","Trésorier adjoint","Membre"]
LIST_RELATIONSHIP = ["Célibataire","Marié(e)","Veuf(ve)"]

# Regex
REGEX_EMAIL = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

# Key
KEY_ALERT="Alert"
KEY_FORM="Form"
KEY_USER="User"
KEY_DATA="Data"
KEY_SEARCH="Search"

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

TITLE_STYLE = {
    "font":FONT_TITLE,
    "bg":LIGHTBLUE,
}