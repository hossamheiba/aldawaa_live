# Generated by Django 5.1.4 on 2024-12-10 00:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactFormSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('phone', models.IntegerField(blank=True, verbose_name='phone')),
                ('message', models.TextField(verbose_name='message')),
                ('submitted_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Contact message',
                'verbose_name_plural': 'Contact message',
            },
        ),
        migrations.CreateModel(
            name='Image_Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_banner', models.ImageField(blank=True, help_text='Optional - as you like <br> If no image is selected, an automatic image appears.', null=True, upload_to='aldawaa_departments/image_banner/', verbose_name='image banner')),
            ],
            options={
                'verbose_name': 'Contact Info',
                'verbose_name_plural': 'Contact Info',
            },
        ),
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_title', models.CharField(help_text='Maximum 30 characters<br>mandatory', max_length=30, verbose_name='card title')),
                ('card_title_en', models.CharField(help_text='Maximum 30 characters<br>mandatory', max_length=30, null=True, verbose_name='card title')),
                ('card_title_ar', models.CharField(help_text='Maximum 30 characters<br>mandatory', max_length=30, null=True, verbose_name='card title')),
                ('card_email', models.EmailField(blank=True, help_text='optional', max_length=254, null=True, verbose_name='card email')),
                ('card_phone', models.IntegerField(blank=True, help_text='optional', null=True, verbose_name='card phone')),
                ('pragraph_link', models.CharField(blank=True, help_text='optional', max_length=225, null=True, verbose_name='pragraph link')),
                ('pragraph_link_en', models.CharField(blank=True, help_text='optional', max_length=225, null=True, verbose_name='pragraph link')),
                ('pragraph_link_ar', models.CharField(blank=True, help_text='optional', max_length=225, null=True, verbose_name='pragraph link')),
                ('link_pragraph', models.URLField(blank=True, help_text='optional', null=True, verbose_name='link pragraph')),
                ('address_title', models.CharField(blank=True, help_text='optional', max_length=225, null=True, verbose_name='address title')),
                ('address_title_en', models.CharField(blank=True, help_text='optional', max_length=225, null=True, verbose_name='address title')),
                ('address_title_ar', models.CharField(blank=True, help_text='optional', max_length=225, null=True, verbose_name='address title')),
                ('address_link', models.URLField(blank=True, help_text='optional', null=True, verbose_name='address link')),
                ('Image_Banner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Contact_Us.image_banner')),
            ],
            options={
                'verbose_name': 'Contact Info',
                'verbose_name_plural': 'Contact Info',
            },
        ),
    ]
