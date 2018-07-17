from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from djangocms_text_ckeditor.fields import HTMLField


class Course(object):
    def __init__(self, **kwargs):
        for key, value in kwargs.iteritems():
            setattr(self, key, value)


@python_2_unicode_compatible
class PositionCategory(models.Model):
    name = models.CharField(verbose_name="Name", max_length=254)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Position category"
        verbose_name_plural = "Position categories"


@python_2_unicode_compatible
class PositionPact(models.Model):
    name = models.CharField(verbose_name="Name", max_length=254)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Position pact"
        verbose_name_plural = "Position pacts"


@python_2_unicode_compatible
class PositionTechnology(models.Model):
    name = models.CharField(verbose_name="Name", max_length=254)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Position technology"
        verbose_name_plural = "Position technologies"


@python_2_unicode_compatible
class Position(models.Model):
    lang = models.BooleanField(default=False, db_index=True)
    date = models.DateTimeField()
    category = models.ForeignKey("acamar_api.PositionCategory", on_delete=models.CASCADE, related_name="positions")
    place = models.CharField(max_length=254, blank=True)
    start = models.CharField(max_length=254, blank=True)
    name = models.CharField(max_length=254, blank=True)
    introduction = models.TextField(blank=True)
    title1 = models.CharField(max_length=254, blank=True)
    text1 = HTMLField(blank=True)
    title2 = models.CharField(max_length=254, blank=True)
    text2 = HTMLField(blank=True)
    title3 = models.CharField(max_length=254, blank=True)
    text3 = HTMLField(blank=True)
    title4 = models.CharField(max_length=254, blank=True)
    text4 = HTMLField(blank=True)
    title5 = models.CharField(max_length=254, blank=True)
    text5 = HTMLField(blank=True)
    title6 = models.CharField(max_length=254, blank=True)
    text6 = HTMLField(blank=True)
    user_email = models.CharField(max_length=254, blank=True)
    user_first_name = models.CharField(max_length=254, blank=True)
    user_second_name = models.CharField(max_length=254, blank=True)
    user_image = models.CharField(max_length=254, blank=True)
    user_image_url = models.URLField(max_length=254, blank=True)
    user_phone = models.CharField(max_length=254, blank=True)
    user_position = models.CharField(max_length=254, blank=True)
    technologies = models.ManyToManyField("acamar_api.PositionTechnology", related_name="positions")
    pacts = models.ManyToManyField("acamar_api.PositionPact", related_name="positions")

    def __str__(self):
        return self.name if self.name else self.title1

    class Meta:
        verbose_name = "Position"
        verbose_name_plural = "Positions"
