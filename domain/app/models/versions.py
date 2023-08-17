from django.db import models
from domain.utils.db.models import NamedModel, LifeCycleModel, DescriptionedModel
from .queries_set.version import VersionQuerySet
from enum import Enum, unique

@unique
class ReleaseNoteType(Enum):
    NEW_FUTURE = 'NEW FUTURE'
    FUTURE_UPGRADE = 'FUTURE UPGRADE'
    BUG = 'BUG'

    @staticmethod
    def value_exist(VALUE):
        return (
                ReleaseNoteType.NEW_FUTURE.value == VALUE
                or  ReleaseNoteType.FUTURE_UPGRADE.value == VALUE
                or  ReleaseNoteType.BUG.value == VALUE
                )
    @staticmethod
    def validate(value):
        if not ReleaseNoteType.value_exist(value):
            raise ValueError('{} nao existe!'.format(value))
    


class VersionModel(NamedModel):
    version = models.CharField(
                                max_length=100, 
                                unique=True,
                                editable=False
                            )
    objects:VersionQuerySet = VersionQuerySet.as_manager()
    def __str__(self):
        return '{} {}'.format(self.version, self.name)
    
    @classmethod
    def factory(cls, name, version):
        return cls(
            name = name,
            version = version
        )

class ReleaseNoteModel(DescriptionedModel):
    version = models.ForeignKey(
                                  VersionModel, 
                                  related_name="release_notes",
                                  on_delete=models.CASCADE
                                )
    note_type = models.CharField(
                                  max_length=100,
                                  null=True,
                                  blank=True,
                                  default=ReleaseNoteType.NEW_FUTURE.value
                                )
    @classmethod
    def factory(cls, description, note_type):
        return cls(
            description = description,
            note_type = note_type
        )
    

    


