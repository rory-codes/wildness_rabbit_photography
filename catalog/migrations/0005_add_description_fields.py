from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = [
        ("catalog", "0003_alter_photo_options"),
    ]
    operations = [
        migrations.AddField(
            model_name="collection",
            name="description",
            field=models.TextField(blank=True, default=""),
            preserve_default=False,
        ),
    ]