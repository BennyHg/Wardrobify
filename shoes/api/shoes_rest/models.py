from django.db import models
from django.urls import reverse

# Create your models here.
class BinVO(models.Model):
    closet_name = models.CharField(max_length=100)
    bin_number = models.PositiveSmallIntegerField()
    bin_size = models.PositiveSmallIntegerField()
    # href = models.CharField(max_length=200, unique=True)
    
    def __str__(self):
        return f" Bin number: {self.closet_name}{self.bin_number}"

class Shoe(models.Model):
    manufacturer = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    picture = models.URLField(null=True)
    bin = models.ForeignKey(
        BinVO,
        related_name="shoes",
        on_delete=models.PROTECT,
    )

    def get_api_url(self):
        return reverse("api_detail_shoe", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.manufacturer} {self.model} in {self.bin}"

 