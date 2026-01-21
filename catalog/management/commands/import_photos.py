from pathlib import Path
from django.core.files import File
from django.core.management.base import BaseCommand, CommandError
from catalog.models import Collection, Photo
from django.utils.text import slugify

class Command(BaseCommand):
    help = "Import photos from <root>/<collection>/<image files>"

    def add_arguments(self, parser):
        parser.add_argument("--root", required=True, help="Folder with subfolders per collection")
        parser.add_argument("--publish", action="store_true", help="Mark photos as published")

    def handle(self, *args, **opts):
        root = Path(opts["root"])
        if not root.exists():
            raise CommandError(f"{root} does not exist")

        created = 0
        for col_dir in root.iterdir():
            if not col_dir.is_dir():
                continue
            col, _ = Collection.objects.get_or_create(
                name=col_dir.name,
                defaults={"slug": slugify(col_dir.name), "is_published": True},
            )
            for img_path in col_dir.glob("*.*"):
                if img_path.suffix.lower() not in {".jpg", ".jpeg", ".png", ".webp"}:
                    continue
                with img_path.open("rb") as fh:
                    photo = Photo(collection=col, title=img_path.stem, is_published=opts["publish"])
                    photo.image.save(img_path.name, File(fh), save=True)
                    created += 1

        self.stdout.write(self.style.SUCCESS(f"Imported {created} photos"))
