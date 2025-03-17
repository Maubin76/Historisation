import json
from django.core.management import BaseCommand
from Application.models import Personne  # Adjust import if needed

class Command(BaseCommand):
    help = "Convert a JSON file into an instance of an object"

    def handle(self, *args, **options):
        """Method that converts a JSON file into an object"""

        # JSON file example
        json_data = '''{
            "model": "Application.Personne",
            "pk": 1,
            "fields": {
                "first_name": "Pierre",
                "last_name": "Paul",
                "age": 28,
                "address": "Somewhere"
            }
        }'''

        # Parse JSON
        data = json.loads(json_data)

        # Extract fields
        fields = data.get("fields", {})

        # Create Personne instance
        personne = Personne.objects.create(
            first_name=fields.get("first_name"),
            last_name=fields.get("last_name"),
            age=fields.get("age"),
            address=fields.get("address")
        )

        # Print all instance details
        self.stdout.write(self.style.SUCCESS(f"Personne Created:"))
        self.stdout.write(f"  ID: {personne.id}")
        self.stdout.write(f"  First Name: {personne.first_name}")
        self.stdout.write(f"  Last Name: {personne.last_name}")
        self.stdout.write(f"  Age: {personne.age}")
        self.stdout.write(f"  Address: {personne.address}")
