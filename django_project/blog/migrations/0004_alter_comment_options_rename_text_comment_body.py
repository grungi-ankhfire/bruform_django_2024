# Generated by Django 5.1.1 on 2024-10-29 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_date']},
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='text',
            new_name='body',
        ),
    ]