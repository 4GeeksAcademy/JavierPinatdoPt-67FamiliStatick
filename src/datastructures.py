from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # Lista de miembros
        self._members = [{
            "id":self._generateId(),
            "first_name": "Jhon",
            "last_name": self.last_name,
            "age":33,
            "lucky_numbers": [7, 13, 22]
        },
        {
            "id":self._generateId(),
            "first_name": "Jane",
            "last_name": self.last_name,
            "age":35,
            "lucky_numbers": [10, 14, 3]
        },
        {
            "id":self._generateId(),
            "first_name": "Jimmy",
            "last_name": self.last_name,
            "age":5,
            "lucky_numbers": 1,
        }]

    # Funcion genera un id aleatorio
    def _generateId(self):
        return randint (0, 99999)
    
    # Funcion que añade un miembro
    def add_member(self, member):
        self._members.append(member)
        return self._members
    
    # Funcion que borra miembro
    def delete_member(self, id):
        for member in self._members:
            if member["id"] == id:
                self._members.remove(member)
                return member
            
    # Funcion que trae un miembro
    def get_member(self, id):
        for member in self._members:
            if member["id"] == id:
                return member
            
   # Funcion que trae todos los miembros
    def get_all_members(self):
        return self._members
