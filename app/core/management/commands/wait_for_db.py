"Django Command to wait for the database to be available"

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self ,*args, **options):
        print "Waiting for database..."
        time.sleep(10)
        print "Database ready!"


from djangorestframefwork import rest_framework


app = rest_framework.setup_app(
) from DjangoTemplates