from django.db import models

feature_CHOICES=((0,u'Обычный символ'),
                     (1,u'Первый символ на странице'),
                     (2,u'Первый символ в строке'),
                     (3,u'Последний символ в строке'),
                     (4,u'Последний символ на странице'),
                     (5,u'Нераспознанный, Обычный'),
                     (6,u'Нераспознанный, Первый символ на странице'),
                     (7,u'Нераспознанный, Первый символ в строке'),
                     (8,u'Нераспознанный, Последний символ в строке'),
                     (9,u'Нераспознанный, Последний символ на странице'),
                     )

class signs(models.Model):
    letter = models.CharField(max_length=50)
    style = models.CharField(max_length=11)
    ID_sign =  models.CharField(max_length=11)
    grp = models.CharField(max_length=10)
    signID = models.CharField(max_length=11)
    name = models.CharField(max_length=50)

    def _get_style(self):
        return u'%s' % (self.style)

    def get_style(self):
        return u'%s' % (self.style)

    full_style = property(get_style)

    def __unicode__(self):
        return unicode(self.signID)

    class Meta:
        db_table = 'signs'
        verbose_name = u"Знамя"
        verbose_name_plural = u"Знамена"

class Chants(models.Model):
    sign = models.ForeignKey(signs, on_delete=models.CASCADE, blank=True, null=True)
    slog = models.CharField(max_length=50, blank=True, null=True)
    page = models.IntegerField(blank=True, null=True)
    num_on_page = models.IntegerField(blank=True, null=True)
    glas = models.IntegerField(blank=True, null=True)
    feature = models.IntegerField(choices=feature_CHOICES, default=0, blank=True, null=True)
    pometa = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        verbose_name = u"Нота в песнопении"
        verbose_name_plural = u"Ноты в песнопении"

    def __unicode__(self):
        return unicode(self.sign.signID)
