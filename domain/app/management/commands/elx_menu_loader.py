from django.core.management.base import BaseCommand, CommandError
from core.app.services.menu import MenuService

class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Indicates the number of users to be created')

    def handle(self, *args, **options):
        username = options["username"]
        
        MenuService().load()
        self.stdout.write(
                self.style.SUCCESS('Successfully, Carregamento de menu {}'.format(username))
            )