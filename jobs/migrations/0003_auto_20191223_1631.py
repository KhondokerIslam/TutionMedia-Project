# Generated by Django 3.0 on 2019-12-23 10:31

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20191223_1626'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='Class',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('PR', 'Primary (1-5)'), ('JU', 'Junior (6-8)'), ('SSC', 'Scondary (9-10)'), ('HSC', 'Higher Secondary (11-12)')], max_length=15),
        ),
        migrations.AlterField(
            model_name='job',
            name='Medium',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('BM', 'Bangla Medium'), ('EM', 'English Medium'), ('EV', 'English Version(National Curriculam)')], default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='job',
            name='Tution_Type',
            field=models.CharField(choices=[('PR', 'Private'), ('BC', 'Batch'), ('PB', 'Both Private and Batch')], default='', max_length=15),
        ),
    ]