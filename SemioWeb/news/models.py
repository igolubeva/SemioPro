from django.db import models


class News (models.Model):
    title = models.CharField(max_length=70)
    description = models.CharField(max_length=191)
    pub_date = models.DateTimeField()
    text = models.TextField()

    class Meta:
        verbose_name = u"Новость"
        verbose_name_plural = u"Новости"
