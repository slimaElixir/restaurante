from django.db import models
'''
@autor Simone Lima
'''
class GenericQuerySet(models.query.QuerySet):

    def find_all(self):
        return self.all()

    def find_active(self):
        return self.filter(active=True,delected=False)

    def find_delected(self):
        return self.filter(active=False,delected=True)

    def find_inactive(self):
        return self.filter(active=False,delected=False)

    def get_by_id(self,id):
        return self.get(pk=id)

class CodedQuerySet(GenericQuerySet):
    def get_by_code(self,code):
        return self.get(code=code)
    
class DescriptionedQuerySet(GenericQuerySet):
    def get_by_description(self,description):
        return self.get(description=description)
    
class NamedQuerySet(GenericQuerySet):
    def get_by_name(self,name):
        return self.get(name=name)