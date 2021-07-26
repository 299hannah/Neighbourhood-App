# Generated by Django 3.2.5 on 2021-07-26 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0005_rename_neighbourbood_post_neighbourhood'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='neighbourbood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hood.neighbourhood'),
        ),
        migrations.AlterField(
            model_name='post',
            name='neighbourhood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hood.neighbourhood'),
        ),
    ]
