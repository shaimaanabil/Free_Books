from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Author(models.Model):

    class Meta:
        verbose_name = "Author"
        verbose_name_plural = "Authors"

    author_id = models.AutoField("Author ID", primary_key=True)
    name = models.CharField("Author name", max_length=50)
    pic = models.ImageField("Author Picture", blank=True, upload_to="author_pic")
    bio = models.TextField("Bio", blank=True)
    birth_date = models.DateField("Date of Birth", null=True, blank=True)
    death_date = models.DateField("Date of Death", null=True, blank=True)

    def __str__(self):
        return self.name

class Category(models.Model):

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    category_id = models.AutoField("Category", primary_key=True)
    name = models.CharField("Category Name", max_length=50)
    pic = models.ImageField("Categor Cover", blank=True, upload_to='category_cover')

    def __str__(self):
        return self.name


class Book(models.Model):

    class Meta:
        verbose_name = "Book"
        verbose_name_plural = "Books"

    book_id = models.AutoField("Book ID", primary_key=True)
    author = models.ForeignKey(Author, related_name="Write", on_delete=models.CASCADE, verbose_name="Author")
    title = models.CharField("Book Name", max_length=50)
    category = models.ForeignKey(Category, related_name="has_books", on_delete=models.CASCADE, default='')
    publish_date = models.DateField("Published at", null=True, blank=True)
    country = models.CharField("Country", max_length=50, blank=True)
    link = models.URLField("Link", blank=True)
    pic = models.ImageField("Book Cover", blank=True, upload_to='book_cover')
    summary = models.TextField("Summary", blank=True)

    def __str__(self):
        return self.title




class Profile(models.Model):
    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    birth_date = models.DateField("Date of Birth", null=True, blank=True)
    pic = models.ImageField("Profile Picture", blank=True, upload_to='user_profiles')
    bio = models.TextField("Bio", blank=True)
    favourite_category = models.ManyToManyField(Category, through='FavouriteCategory', related_name='favored_by')
    rating = models.ManyToManyField(Book, through='Rate', related_name='rated_by')
    reading = models.ManyToManyField(Book, through='Read', related_name='read_by')
    wish = models.ManyToManyField(Book, through='WishList', related_name='wished_by')
    follows = models.ManyToManyField(Author, through='Follower', related_name='followed_by')

    def __str__(self):
        return self.user.first_name


class Rate(models.Model):

    class Meta:
        verbose_name = "Rate"
        verbose_name_plural = "Rates"
        unique_together = (('user', 'book'),)

    rate_id = models.AutoField("Rate ID", primary_key=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="User")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Book")
    score = models.PositiveSmallIntegerField()

    def __str__(self):
        return str(self.rate_id)



class Read(models.Model):

    class Meta:
        verbose_name = "Read"
        verbose_name_plural = "Reads"
        unique_together = (('user', 'book'),)

    read_id = models.AutoField("Read ID", primary_key=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="User")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Book")

    def __str__(self):
        return str(self.read_id)


class WishList(models.Model):

    class Meta:
        verbose_name = "WishList"
        verbose_name_plural = "WishLists"
        unique_together = (('user', 'book'),)

    wish_id = models.AutoField("Wish ID", primary_key=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="User")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, verbose_name="Book")

    def __str__(self):
        return str(self.wish_id)


class Follower(models.Model):

    class Meta:
        verbose_name = "Follower"
        verbose_name_plural = "Followers"
        unique_together = (('user', 'author'),)

    follow_id = models.AutoField("Follow ID", primary_key=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="User")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Author")

    def __str__(self):
        return str(self.follow_id)


class FavouriteCategory(models.Model):

    class Meta:
        verbose_name = "FavouriteCategory"
        verbose_name_plural = "FavouriteCategories"
        unique_together = (('user', 'category'),)

    favorite_id = models.AutoField("Favorite ID", primary_key=True)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="User")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Category")

    def __str__(self):
        return str(self.favorite_id)
