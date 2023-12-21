from django.db import models
from django.contrib import auth


class Publisher(models.Model):
    name = models.CharField(max_length=100, help_text="The name of the Publisher")
    website = models.URLField(help_text="The Publisher website")
    email = models.EmailField(help_text="The Publisher's email address")

    def __str__(self) -> str:
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=70, help_text="The title of the book")
    publication_date = models.DateField(verbose_name="Date the book was published")
    isbn = models.CharField(max_length=20, verbose_name="ISBN number of the book")
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    contributors = models.ManyToManyField('Contributor', through="BookContributor")

    def __str__(self) -> str:
        return self.title


class Contributor(models.Model):
    first_name = models.CharField(max_length=50, help_text="The contributor's first name")
    last_name = models.CharField(max_length=50, help_text="The contributor's last name or names")
    email = models.EmailField(help_text="The contact email for the contributor")

    def __str__(self) -> str:
        return self.first_name


class BookContributor(models.Model):
    class ContributorRole(models.TextChoices):
        AUTHOR = "AUTHOR", "Author"
        CO_AUTHOR = "CO_AUTHOR", "Co-Author"
        EDITOR = "EDITOR", "Editor"
    
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)
    role = models.CharField(verbose_name="The role this contributor had in the \
                            book", choices=ContributorRole.choices,
                            max_length=20)
    

class Review(models.Model):
    content = models.TextField(help_text="The Review text")
    rating = models.IntegerField(help_text="The rating the reviewer has given")
    date_created = models.DateTimeField(auto_now_add=True, help_text="The date and time the review was \
                                        created")
    date_edited = models.DateTimeField(null=True, help_text="The date and time the review \
                                       was last edited")
    creator = models.ForeignKey(Book, on_delete=models.CASCADE, help_text="The Book this review is for")
