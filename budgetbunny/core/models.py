from django.db import models

# Create your models here.
class CardInfo(models.Model):
    card_name = models.CharField(max_length=100)
    savings_amount = models.DecimalField(max_digits=10, decimal_places=2)
    checking_amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.card_name