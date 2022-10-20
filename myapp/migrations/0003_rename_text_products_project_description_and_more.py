# Generated by Django 4.1.2 on 2022-10-18 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_products'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='text',
            new_name='project_description',
        ),
        migrations.AddField(
            model_name='products',
            name='project_name',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]