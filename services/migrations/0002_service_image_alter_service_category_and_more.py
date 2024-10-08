# Generated by Django 5.1.1 on 2024-09-29 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='service_images/'),
        ),
        migrations.AlterField(
            model_name='service',
            name='category',
            field=models.CharField(choices=[('medical', 'Medical'), ('medical_ar', 'طبي'), ('food', 'Food'), ('food_ar', 'طعام'), ('education', 'Education'), ('education_ar', 'تعليم'), ('other', 'Other'), ('other_ar', 'آخر')], max_length=20),
        ),
        migrations.AlterField(
            model_name='service',
            name='contact_info',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='service',
            name='hours',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='service',
            name='location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
