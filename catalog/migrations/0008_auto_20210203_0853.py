# Generated by Django 3.1.5 on 2021-02-03 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_auto_20210203_0842'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='language0',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='catalog.language'),
        ),
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(blank=True, choices=[('English', 'English'), ('Chinese', 'Chinese'), ('Japanese', 'Japanese')], default='English', help_text='Book language', max_length=20),
        ),
    ]
