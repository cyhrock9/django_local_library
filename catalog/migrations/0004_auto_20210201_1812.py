# Generated by Django 3.1.5 on 2021-02-01 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_auto_20210131_1525'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name', 'first_name'], 'permissions': (('can_create_author', 'Create author'), ('can_update_author', 'Update author'), ('can_delete_author', 'Delete author'))},
        ),
    ]
