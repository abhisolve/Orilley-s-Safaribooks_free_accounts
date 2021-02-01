from django.db import models
from django.utils import timezone


class SafariAccount(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    is_expired = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_expired = models.DateTimeField(null=True, blank=True)
    expires_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return "{} - {}".format(self.email, self.is_expired)

    class Meta:
        verbose_name = "Safari Account"
        verbose_name_plural = "Safari Accounts"
    
    def save(self, *args, **kwargs):
        self.expires_at = timezone.now()+timezone.timedelta(days=10)
        super(SafariAccount, self).save(*args, **kwargs)