# Generated by Django 5.0.6 on 2024-05-26 22:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='course',
            name='view',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.RenameModel(
            old_name='CourseOrders',
            new_name='Order',
        ),
        migrations.CreateModel(
            name='CourseOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('Course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.course')),
                ('Order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.order')),
            ],
        ),
    ]