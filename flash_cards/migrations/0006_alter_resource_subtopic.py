# Generated by Django 4.2.1 on 2023-05-24 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flash_cards', '0005_resource_subtopic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='subtopic',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resources', to='flash_cards.subtopic'),
        ),
    ]