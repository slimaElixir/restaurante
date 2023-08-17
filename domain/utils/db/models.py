'''
Autor: Simone Lima
'''
from django.db import models
from django.utils.text import slugify



class SlugModel(models.Model):
    slug = models.CharField(("Slug"), max_length=100, unique=True)
    def get_slug_attriute(self):
        raise NotImplementedError("Unknown slug attriute, plese implement this method") 

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.get_slug_attriute())
        super(self).save(*args, **kwargs)

    class Meta:
        abstract = True

class AbstractModel(models.Model):
    active = models.BooleanField(("Activo"), default=True)
    delected = models.BooleanField(("Apagado"), default=False)

    def delete(self, *args, **kwargs):
        print('Apagando de nosso metodo...')
        self.active = False
        self.delected = True
        super().save(*args, **kwargs)

    #objects = GenericQuerySet().as_manager()
    class Meta:
        abstract = True
        
    @property
    def status(self):
        if self.active:
            return "Activo"
        return "Inactivo"
    
class DescriptionedModel(AbstractModel):
    description = models.TextField(("Descricao"),null=True,blank=True)
    class Meta:
        abstract = True

    def __str__(self):
        return self.description
    
class NamedModel(AbstractModel):
    name = models.CharField(("Nome"),max_length=255,)
    class Meta:
        abstract = True

    def __str__(self):
        return self.name
    
class CodedModel(AbstractModel):
    code = models.CharField(("Codigo"), max_length=50, unique=True)
    #objects = CodedQuerySet().as_manager()
    class Meta:
        abstract = True

    def __str__(self):
        return "{} {}".format(self.code)
    

class LifeCycleModel(AbstractModel):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField( auto_now=True)
    
    @property
    def created_at_props(self):
        return "{}-{}-{}".format(self.created_at.day, self.created_at.month, self.created_at.year)

    class Meta:
        abstract = True

class SortableModel(models.Model):
    sort_order = models.IntegerField(editable=False, db_index=True, null=True)

    class Meta:
        abstract = True
        ordering = ("sort_order",)




  