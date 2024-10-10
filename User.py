class User:
    def __init__(self, first_name:str="", last_name:str="", gender:str="", birthday:str="", start_suscription:str="", end_suscription:str="", address:str="", city:str="", zipcode:str="", email:str="", phone:str="", job:str="", relationship_situation:str="", nb_kids:str="", membership_number:str="", membership_role:str="", id:int=0):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.birthday = birthday
        self.start_suscription = start_suscription
        self.end_suscription = end_suscription
        self.address = address
        self.city = city
        self.zipcode = zipcode
        self.email = email
        self.phone = phone
        self.job = job
        self.relationship_situation = relationship_situation
        self.nb_kids = nb_kids
        self.membership_number = membership_number
        self.membership_role = membership_role

    def __list__(self):
        return [
            self.first_name,
            self.last_name,
            self.gender,
            self.birthday,
            self.start_suscription,
            self.end_suscription,
            self.address,
            self.city,
            self.zipcode,
            self.email,
            self.phone,
            self.job,
            self.relationship_situation,
            self.nb_kids,
            self.membership_number,
            self.membership_role,
            self.id
        ]

