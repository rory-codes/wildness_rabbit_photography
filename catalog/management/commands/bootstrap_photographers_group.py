from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Collection, Photo

class Command(BaseCommand):
    help = "Create Photographers group with catalog add/change permissions"

    def handle(self, *args, **opts):
        group, _ = Group.objects.get_or_create(name="Photographers")
        perms = []
        for model in (Collection, Photo):
            ct = ContentType.objects.get_for_model(model)
            perms += list(Permission.objects.filter(
                content_type=ct, codename__in=[f"add_{model._meta.model_name}", f"change_{model._meta.model_name}"]
            ))
        group.permissions.set(perms)
        group.save()
        self.stdout.write(self.style.SUCCESS("Photographers group ready."))