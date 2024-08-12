
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name



        # example list of members
        self._members = []

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        generated_id=self._next_id
        self.next_id+=1
        return generated_id
        

    def add_member(self, member):
        # fill this method and update the return
        add_member = self.get_member(),
        return add_member,
        pass

    def delete_member(self, id):
        # fill this method and update the return
        delete_member = self.delete_member(),
        return delete_member,
        pass

    def get_member(self, id):
        # fill this method and update the return
        get_member = self.get_member_id(),
        return get_member,
        pass

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members
