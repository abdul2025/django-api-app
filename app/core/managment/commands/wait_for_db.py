"""
Django command to wait for databases to be available
"""

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    
    def handle(self, *args: Any, **options: Any):
        pass