from django.db import models
from django.urls import reverse

class LocationVO(models.Model):
    import_href = models.CharField(max_length=200, unique=True, null=True)
    closet_name = models.CharField(max_length=100)
    section_number = models.PositiveSmallIntegerField()
    shelf_number = models.PositiveSmallIntegerField()

    def get_api_url(self):
        return reverse("api_location", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.closet_name} - {self.section_number}/{self.shelf_number}"

    class Meta:
        ordering = ("closet_name", "section_number", "shelf_number")

class Hat(models.Model):
    name = models.CharField(max_length=100)
    fabric = models.CharField(max_length=50)
    style = models.CharField(max_length=50)
    color = models.CharField(max_length=50)
    picture_url = models.URLField(null=True)

    location = models.ForeignKey(
        LocationVO,
        related_name="hats",
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.name
