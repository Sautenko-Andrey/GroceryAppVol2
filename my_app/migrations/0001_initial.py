# Generated by Django 4.1.7 on 2023-03-09 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dishes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_name', models.CharField(max_length=100)),
                ('count_persons', models.CharField(max_length=2)),
                ('time_create', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'verbose_name': 'Поиск блюд',
                'verbose_name_plural': 'Поиск блюд',
            },
        ),
        migrations.CreateModel(
            name='InfoAboutDishes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название блюда')),
                ('img', models.ImageField(upload_to='', verbose_name='Изображение блюда')),
            ],
            options={
                'verbose_name': 'Информация о блюдах',
                'verbose_name_plural': 'Информация о блюдах',
            },
        ),
        migrations.CreateModel(
            name='ItemsPicsFromNet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=150, null=True)),
                ('picture', models.ImageField(upload_to='')),
                ('description', models.TextField(null=True)),
            ],
            options={
                'verbose_name': 'Изображения из сети',
                'verbose_name_plural': 'Изображения из сети',
            },
        ),
        migrations.CreateModel(
            name='MainPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('under_title', models.CharField(max_length=100, null=True)),
                ('text_on_page', models.TextField(blank=True)),
                ('main_logo', models.ImageField(null=True, upload_to='media/%Y/%m/%d/')),
            ],
            options={
                'verbose_name': 'Контент главной страницы',
                'verbose_name_plural': 'Контент главной страницы',
            },
        ),
        migrations.CreateModel(
            name='RelevantMarkets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('market_name', models.CharField(max_length=25, verbose_name='Название маркета')),
            ],
            options={
                'verbose_name': 'Досутпные супермаркеты',
                'verbose_name_plural': 'Досутпные супермаркеты',
            },
        ),
        migrations.CreateModel(
            name='SetOfProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=150)),
                ('amount', models.CharField(max_length=20)),
                ('request_time', models.DateTimeField(auto_now_add=True)),
                ('atb_choice', models.BooleanField(null=True)),
                ('eko_choice', models.BooleanField(null=True)),
                ('varus_choice', models.BooleanField(null=True)),
                ('silpo_choice', models.BooleanField(null=True)),
                ('ashan_choice', models.BooleanField(null=True)),
                ('novus_choice', models.BooleanField(null=True)),
                ('metro_choice', models.BooleanField(null=True)),
                ('nash_kray_choice', models.BooleanField(null=True)),
                ('fozzy_choice', models.BooleanField(null=True)),
                ('owner', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Набор продуктов',
                'verbose_name_plural': 'Набор продуктов',
            },
        ),
        migrations.CreateModel(
            name='SitePolitics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('terms_of_use', models.TextField()),
                ('privacy_policy', models.TextField()),
                ('cookie_policy', models.TextField()),
            ],
            options={
                'verbose_name': 'Пользовательские соглашения',
                'verbose_name_plural': 'Пользовательские соглашения',
            },
        ),
        migrations.CreateModel(
            name='UserItemNameUpload_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_item_name', models.CharField(max_length=100)),
                ('time_create', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Название товара пользователя_2',
                'verbose_name_plural': 'Название товара пользователя_2',
            },
        ),
        migrations.CreateModel(
            name='UserPhotoUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_image', models.ImageField(null=True, upload_to='')),
            ],
            options={
                'verbose_name': 'Изображение пользователя',
                'verbose_name_plural': 'Изображение пользователя',
            },
        ),
        migrations.CreateModel(
            name='UserPhotoUploadModel_2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='photos/user/')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Фото пользователя2',
                'verbose_name_plural': 'Фото пользователя2',
                'ordering': ['-id'],
            },
        ),
    ]
