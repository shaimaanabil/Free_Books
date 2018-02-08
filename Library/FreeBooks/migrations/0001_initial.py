# Generated by Django 2.0.2 on 2018-02-08 23:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('author_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Author ID')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('death_date', models.DateField(blank=True, null=True, verbose_name='Date of Death')),
                ('pic_url', models.URLField(blank=True, verbose_name='Picture URL')),
                ('name', models.CharField(max_length=50, verbose_name='Author name')),
                ('bio', models.TextField(blank=True, verbose_name='Bio')),
            ],
            options={
                'verbose_name_plural': 'Authors',
                'verbose_name': 'Author',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Book ID')),
                ('publish_date', models.DateField(blank=True, null=True, verbose_name='Published at')),
                ('summary', models.TextField(blank=True, verbose_name='Summary')),
                ('country', models.CharField(blank=True, max_length=50, verbose_name='Country')),
                ('link', models.URLField(blank=True, verbose_name='Link')),
                ('name', models.CharField(max_length=50, verbose_name='Book Name')),
                ('pic_url', models.URLField(blank=True, verbose_name='Picture URL')),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Write', to='FreeBooks.Author')),
            ],
            options={
                'verbose_name_plural': 'Books',
                'verbose_name': 'Book',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Category_id')),
                ('name', models.CharField(max_length=50, verbose_name='Category Name')),
            ],
            options={
                'verbose_name_plural': 'Categorys',
                'verbose_name': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('email', models.EmailField(blank=True, max_length=50, verbose_name='Email')),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='Date of Birth')),
                ('pic_url', models.URLField(blank=True, verbose_name='Picture URL')),
                ('name', models.CharField(max_length=50, verbose_name='Author name')),
                ('favourite_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favorite_category', to='FreeBooks.Category')),
            ],
            options={
                'verbose_name_plural': 'Profiles',
                'verbose_name': 'Profile',
            },
        ),
        migrations.CreateModel(
            name='Read',
            fields=[
                ('read_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Read ID')),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FreeBooks.Book')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FreeBooks.Profile')),
            ],
            options={
                'verbose_name_plural': 'Reads',
                'verbose_name': 'Read',
            },
        ),
        migrations.CreateModel(
            name='WishList',
            fields=[
                ('wish_id', models.AutoField(primary_key=True, serialize=False, verbose_name='Read ID')),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FreeBooks.Book')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FreeBooks.Profile')),
            ],
            options={
                'verbose_name_plural': 'WishLists',
                'verbose_name': 'WishList',
            },
        ),
        migrations.AlterUniqueTogether(
            name='wishlist',
            unique_together={('user_id', 'book_id')},
        ),
        migrations.AlterUniqueTogether(
            name='read',
            unique_together={('user_id', 'book_id')},
        ),
    ]