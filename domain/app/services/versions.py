'''
@autor Simone Lima
'''
import pandas as pd
from .files import AppFilesPath
from domain.app.models import VersionModel, ReleaseNoteModel, ReleaseNoteType
from domain.utils.check_value_utils import CheckValuesUtils
from domain.utils.file_utils import CSVColumnsName, CSV_EXTENSION
from django.db import transaction

class VersionService:
    def install(self):
        installed_versions = VersionModel.objects.find_all()
        versions:dict = {}
        df = pd.read_csv(AppFilesPath.VERSIONS)
        for index, row in df.iterrows():
            version_instance = self.__create_version_instance(row)
            if self.__is_installed(version_instance, installed_versions):
                print('Ignorando  a versao: {} porque ja foi instalada! '.format(version_instance.version))              
            else:
                print('Preparando  a versao: {} {}'.format(version_instance.version, version_instance.name))
                release_notes = self.__create_release_notes_instances(version_instance)
                versions[version_instance.version] = (version_instance,release_notes)

        self.__create_version_with_related_items(versions)
        
    # Cria instancia da versao apartir do ficheiro
    def __create_version_instance(self, row):
        version_name = row[CSVColumnsName.NAME.value]
        version_number = row[CSVColumnsName.NUMBER.value]
        CheckValuesUtils.non_empties([version_name,version_number])  
        return VersionModel.factory(version_name,version_number)
    
    # Cria instancias de release notes da versao apartir do ficheiro
    def __create_release_notes_instances(self, version_instance, ):
        rn_df = pd.read_csv('{}{}{}'.format(AppFilesPath.REALESE_NOTES,version_instance.version,CSV_EXTENSION))
        release_notes = []
        for rn_index, rn_row in rn_df.iterrows():
            description = rn_row[CSVColumnsName.DESCRIPTION.value]
            note_type = rn_row[CSVColumnsName.TYPE.value]
            CheckValuesUtils.non_empties([description,note_type])
            ReleaseNoteType.validate(note_type)
            release_notes.append(ReleaseNoteModel.factory(description,note_type))
        return release_notes
    
    def __is_installed(self,version_instance:VersionModel, installed_versions:list[VersionModel]):
        if not installed_versions:
            return False
        
        for instaled_version in installed_versions:
            if float(instaled_version.version) == float(version_instance.version):
                return True
            return False


    @transaction.atomic
    def __create_version_with_related_items(self, versions:dict):
        if versions:
            for key, values in versions.items():
                version_instance = values[0]
                print('Instalando  a versao: {} {}'.format(version_instance.version, version_instance.name))
                #print(key," : ",values)
                
                version_instance.save()
                version_instance.release_notes.set(values[1],bulk=False )
                #print(values[0])
                #print(values[1])
                print('Versao: {} {} instalada com sucesso!'.format(version_instance.version, version_instance.name))

    
