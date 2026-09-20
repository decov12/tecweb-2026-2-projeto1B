from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=2000)
    tags = models.ManyToManyField(
        Tag,
        blank=True,
        related_name='notes',
    )

    def __str__(self):
        resposta=""
        resposta+=str(self.id)
        resposta+=". "
        resposta+=self.title
        return resposta
