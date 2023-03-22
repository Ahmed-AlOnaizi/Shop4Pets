# Generated by Django 2.2.28 on 2023-03-21 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('pet_type', models.CharField(choices=[('dog', 'Dog'), ('cat', 'Cat'), ('bird', 'Bird'), ('fish', 'Fish'), ('hamster', 'Hamster')], max_length=10)),
                ('age', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='pets/')),
            ],
        ),
    ]