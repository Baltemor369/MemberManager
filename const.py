FILENAME = "members.db"
APP_NAME="MyApp"
TABLE="members"

# Fonts
FONT_TITLE = ("Arial", 27, "bold")
FONT_MESSAGE = ("Arial", 21, "bold")
FONT_LABEL = ("Arial", 18, "bold")

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
DB_MEMBERSHIP_FONCTION="member_function"
DB_ACTIVITY="activity"
DB_MEMBERSHIP_ID="member_id"


# attributs
ATTR = {
    DB_ID:"ID",
    DB_FIRST_NAME:"Prénom",
    DB_LAST_NAME:"Nom",
    DB_BIRTHDAY_LAST_NAME:"Nom de naissance",
    DB_CIVILITY:"Civilité",
    DB_NATIONALITY:"Nationalité",
    DB_BIRTHDAY:"Date de naissance",
    DB_BIRTHDAY_LOCATION:"Lieu de naissance",
    DB_START_SUSCRIPTION:"Date début",
    DB_END_SUSCRIPTION:"Date fin",
    DB_ADDRESS:"Adresse Postale",
    DB_CITY:"Ville",
    DB_ZIPCODE:"Code postal",
    DB_EMAIL:"Email",
    DB_PHONE:"Telephone",
    DB_JOB:"Metier",
    DB_RELATIONSHIP_SITUATION:"Situation familiale",
    DB_NB_KIDS:"Nombre enfants",
    DB_MEMBERSHIP_FONCTION:"Fonction",
    DB_ACTIVITY:"Activité",
    DB_MEMBERSHIP_ID:"Identifiant"
}

# Values
VAL_EMPTY=""
VAL_NULL="0"
VAL_ADD="Add"
VAL_MODIFY="Modify"
VAL_EMPTY_ALERT=("", None)

# Messages
#Success msg
MSG_ADD_SUCCESS="Personne ajouté avec succès"
MSG_MODIFY_SUCCESS="Personne modifié avec succès"
MSG_DEL_SUCCESS="Personne supprimé avec succès"
MSG_CSV_SUCCESS="Exportation CSV avec succès"
# error msg
# add form
MSG_INVALID_NAME="Prénom ou nom : format invalide (lettre et \"-' \" uniquement)"
MSG_INVALID_CIVILITY="Civilité : saisi invalide, sélectionnez dans la liste."
MSG_INVALID_NATION="Nationalité : saisi invalide, sélectionnez dans la liste."
MSG_INVALID_BIRTHDAY="Date de naissance : format invalide jj/mm/AAAA"
MSG_INVALID_LOCATION_BIRTHDAY="Date de naissance : format invalide jj/mm/AAAA"
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
# main menu
MSG_NO_SELECTION="Aucune selection"
# unexpected error
MSG_USER_NOT_FIND="Erreur : User empty in add_client, contacter l'administrateur."
MSG_CSV_ERROR="Erreur lors de l'exportation, contacter l'administrateur."
MSG_SAVING_DATA="Erreur lors de la sauvegarde dans la BDD, contacter l'administrateur."
MSG_UPDATE_DATA="Erreur lors de l'update dans la BDD, contacter l'administrateur."

# Widgets text
TXT_EXIT="Quitter"
TXT_BACK="Retour"
TXT_ADD="Ajouter"
TXT_DEL="Supprimer"
TXT_MODIFY="Modifier"
TXT_EXPORT="Exporter"
TXT_SEARCH="Recherche"
TXT_CLEAR="Réinitialiser"
TXT_SEARCH_LABEL="Rechecher par numéro adhérent :"
TXT_ADVANCED_SEARCH="Recherche avancée"
TXT_PERSONAL_INFO="Informations personnelles"
TXT_CONTACT_INFO="Informations de contact"
TXT_SITUATION_INFO="Situation"
TXT_ASSOCIATION_INFO="Informations association"


# List
LIST_CIVILITY = ["M","Mme","Mlle"]
LIST_FUNCTION = ["Membre","Secrétaire", "Secrétaire adjoint", "Trésorier","Trésorier adjoint","Vice Président","Président"]
LIST_RELATIONSHIP = ["Célibataire","Marié(e)","Veuf(ve)"]
LIST_NATION = [
    "France", "Afghanistan", "Albania", "Algeria", "Andorra", "Angola",
    "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria",
    "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados",
    "Belarus", "Belgium", "Belize", "Benin", "Bhutan",
    "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei",
    "Bulgaria", "Burkina Faso", "Burundi", "Cabo Verde", "Cambodia",
    "Cameroon", "Canada", "Central African Republic", "Chad", "Chile",
    "China", "Colombia", "Comoros", "Congo (Congo-Brazzaville)", "Costa Rica",
    "Croatia", "Cuba", "Cyprus", "Czechia (Czech Republic)", "Denmark",
    "Djibouti", "Dominica", "Dominican Republic", "Ecuador", "Egypt",
    "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia", "Eswatini (fmr. 'Swaziland')",
    "Ethiopia", "Fiji", "Finland", "Gabon",
    "Gambia", "Georgia", "Germany", "Ghana", "Greece",
    "Grenada", "Guatemala", "Guinea", "Guinea-Bissau", "Guyana",
    "Haiti", "Honduras", "Hungary", "Iceland", "India",
    "Indonesia", "Iran", "Iraq", "Ireland", "Israel",
    "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan",
    "Kenya", "Kiribati", "Kuwait", "Kyrgyzstan", "Laos",
    "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya",
    "Liechtenstein", "Lithuania", "Luxembourg", "Madagascar", "Malawi",
    "Malaysia", "Maldives", "Mali", "Malta", "Marshall Islands",
    "Mauritania", "Mauritius", "Mexico", "Micronesia", "Moldova",
    "Monaco", "Mongolia", "Montenegro", "Morocco", "Mozambique",
    "Myanmar (formerly Burma)", "Namibia", "Nauru", "Nepal", "Netherlands",
    "New Zealand", "Nicaragua", "Niger", "Nigeria", "North Korea",
    "North Macedonia", "Norway", "Oman", "Pakistan", "Palau",
    "Palestine State", "Panama", "Papua New Guinea", "Paraguay", "Peru",
    "Philippines", "Poland", "Portugal", "Qatar", "Romania",
    "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia", "Saint Vincent and the Grenadines",
    "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", "Senegal",
    "Serbia", "Seychelles", "Sierra Leone", "Singapore", "Slovakia",
    "Slovenia", "Solomon Islands", "Somalia", "South Africa", "South Korea",
    "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname",
    "Sweden", "Switzerland", "Syria", "Tajikistan", "Tanzania",
    "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago",
    "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda",
    "Ukraine", "United Arab Emirates", "United Kingdom", "United States of America", "Uruguay",
    "Uzbekistan", "Vanuatu", "Venezuela", "Vietnam", "Yemen",
    "Zambia", "Zimbabwe"
]
LIST_ACTIF = ["Inactif","Actif"]
LIST_SUS_CHAR = ["--"]

# Regex
REGEX_EMAIL = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
REGEX_DATE_1 = r"(\d{2})[\/\-.]?(\d{2})[\/\-.]?(\d{2})$"
REGEX_DATE_2 = r"(\d{2})[\/\-.]?(\d{2})[\/\-.]?(\d{4})$"
REGEX_NAME = r"^[a-zA-Z\s-]+$"
REGEX_SANITIZED = r"[\'\";\\\n\t|><()&*#%]"

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

BUTTON_STYLE_LONG = {
    "bg":"#333333",
    "fg":LIGHTWHITE,
    "width":15
}

ROOT_STYLE = {
    "bg":LIGHTBLUE
}

ALERT_STYLE = {
    "font":FONT_MESSAGE,
    "bg":LIGHTBLUE
}

LABEL_STYLE = {
    "font":FONT_LABEL,
    "bg":LIGHTBLUE,
}

TITLE_STYLE = {
    "font":FONT_TITLE,
    "bg":LIGHTBLUE,
}