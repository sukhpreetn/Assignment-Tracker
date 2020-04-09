#0002_create_initial_grades.py

from django.db import migrations


def create_grades(apps, schema_editor):
    Grade = apps.get_model('tracker', 'Grade')
    Grade.objects.create(name='Grade1', color='#343a40')
    Grade.objects.create(name='Grade2', color='#343a40')
    Grade.objects.create(name='Grade3', color='#007bff')
    Grade.objects.create(name='Grade4', color='#28a745')
    Grade.objects.create(name='Grade5', color='#17a2b8')


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_grades),
    ]