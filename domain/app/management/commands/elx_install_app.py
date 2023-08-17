from django.core.management.base import BaseCommand, CommandError
from domain.app.services.versions import VersionService

class Command(BaseCommand):
    help = "Closes the specified poll for voting"

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='Indicates the number of users to be created')

    def handle(self, *args, **options):
        username = options["username"]
        
        VersionService().install()
        self.stdout.write(
                self.style.SUCCESS('Successfully, Rodando o manager da ELIXIR {}'.format(username))
            )