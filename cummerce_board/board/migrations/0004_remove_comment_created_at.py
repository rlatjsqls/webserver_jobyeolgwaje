# Generated by Django 3.2.5 on 2023-06-14 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0003_alter_comment_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='created_at',
        ),
    ]