# Generated by Django 4.2.1 on 2023-05-24 10:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flash_cards', '0003_resource_cardquestion_resources'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cardquestion',
            name='resources',
        ),
        migrations.AddField(
            model_name='cardquestion',
            name='resource',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='questions', to='flash_cards.resource'),
        ),
    ]
