# Generated by Django 5.1.4 on 2024-12-10 00:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ImageBannerStrategic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_banner_strategic', models.ImageField(blank=True, help_text='Optional - as you like <br> If no image is selected, an automatic image appears.', null=True, upload_to='Strategic/image_banner_strategic/', verbose_name='Image Banner strategic')),
            ],
            options={
                'verbose_name': 'strategic',
                'verbose_name_plural': 'strategic',
            },
        ),
        migrations.CreateModel(
            name='Partner_Brands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner_image', models.ImageField(upload_to='Strategic/partner_image/', verbose_name='partner_image')),
                ('image_banner_strategic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Strategic_Partnerships.imagebannerstrategic')),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner_title', models.CharField(help_text='Maximum 100 characters', max_length=100, verbose_name='partner title')),
                ('partner_title_en', models.CharField(help_text='Maximum 100 characters', max_length=100, null=True, verbose_name='partner title')),
                ('partner_title_ar', models.CharField(help_text='Maximum 100 characters', max_length=100, null=True, verbose_name='partner title')),
                ('partner_content', models.TextField(help_text='Maximum 2000 characters', max_length=2000, verbose_name='partner content')),
                ('partner_content_en', models.TextField(help_text='Maximum 2000 characters', max_length=2000, null=True, verbose_name='partner content')),
                ('partner_content_ar', models.TextField(help_text='Maximum 2000 characters', max_length=2000, null=True, verbose_name='partner content')),
                ('partner_image', models.ImageField(upload_to='Strategic/partner_image/', verbose_name='partner image')),
                ('image_banner_strategic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Strategic_Partnerships.imagebannerstrategic')),
            ],
            options={
                'verbose_name': 'Testimonial',
                'verbose_name_plural': 'Testimonial',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_banner_inside_page', models.ImageField(blank=True, help_text='Optional - as you like <br> If no image is selected, an automatic image appears.', null=True, upload_to='Strategic/image_banner/', verbose_name='image banner inside page')),
                ('partner_title', models.CharField(help_text='Maximum 100 characters', max_length=100, verbose_name='partner title')),
                ('partner_title_en', models.CharField(help_text='Maximum 100 characters', max_length=100, null=True, verbose_name='partner title')),
                ('partner_title_ar', models.CharField(help_text='Maximum 100 characters', max_length=100, null=True, verbose_name='partner title')),
                ('partner_description', models.TextField(help_text='Maximum 2000 characters', max_length=2000, verbose_name='partner description')),
                ('partner_description_en', models.TextField(help_text='Maximum 2000 characters', max_length=2000, null=True, verbose_name='partner description')),
                ('partner_description_ar', models.TextField(help_text='Maximum 2000 characters', max_length=2000, null=True, verbose_name='partner description')),
                ('partner_main_image', models.ImageField(upload_to='Strategic/partner_main_image/', verbose_name='partner main image')),
                ('first_person_name', models.CharField(help_text='Maximum 100 characters', max_length=100, verbose_name='first person name')),
                ('first_person_name_en', models.CharField(help_text='Maximum 100 characters', max_length=100, null=True, verbose_name='first person name')),
                ('first_person_name_ar', models.CharField(help_text='Maximum 100 characters', max_length=100, null=True, verbose_name='first person name')),
                ('first_person_position', models.CharField(help_text='Maximum 100 characters', max_length=100, verbose_name='first person position')),
                ('first_person_position_en', models.CharField(help_text='Maximum 100 characters', max_length=100, null=True, verbose_name='first person position')),
                ('first_person_position_ar', models.CharField(help_text='Maximum 100 characters', max_length=100, null=True, verbose_name='first person position')),
                ('first_person_image', models.ImageField(upload_to='Strategic/Person_Prtner/', verbose_name='first person image')),
                ('second_person_name', models.CharField(help_text='Maximum1 100 characters', max_length=100, verbose_name='second person name')),
                ('second_person_name_en', models.CharField(help_text='Maximum1 100 characters', max_length=100, null=True, verbose_name='second person name')),
                ('second_person_name_ar', models.CharField(help_text='Maximum1 100 characters', max_length=100, null=True, verbose_name='second person name')),
                ('second_person_position', models.CharField(help_text='Maximum 100 characters', max_length=100, verbose_name='second person position')),
                ('second_person_position_en', models.CharField(help_text='Maximum 100 characters', max_length=100, null=True, verbose_name='second person position')),
                ('second_person_position_ar', models.CharField(help_text='Maximum 100 characters', max_length=100, null=True, verbose_name='second person position')),
                ('second_person_image', models.ImageField(upload_to='Strategic/Person_Prtner/', verbose_name='second person image')),
                ('slug', models.SlugField(blank=True, max_length=100, null=True)),
                ('image_banner_strategic', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Strategic_Partnerships.imagebannerstrategic')),
                ('Testimonial', models.OneToOneField(help_text='If you add a Testimonial Card, you must save and continue editing before typing any entry for it to appear in the drop-down list.', on_delete=django.db.models.deletion.CASCADE, to='Strategic_Partnerships.testimonial')),
            ],
            options={
                'verbose_name': 'Partner',
                'verbose_name_plural': 'Partner',
            },
        ),
    ]