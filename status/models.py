from django.conf import settings
from django.db import models

def upload_status_image(instance, filename):
    return "status/{user}/{filename}".format(user=instance.user, filename=filename)

class Status(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=10000, blank=True, null=True)
    image = models.ImageField(upload_to=upload_status_image, blank=True, null=True)
    updated_at = models.DateField(auto_now=True)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.pk)

    class Meta:
        verbose_name = 'Status Post'
        verbose_name_plural = 'Status Posts'

    ## a new property named owner, used in IsOwnerOrReadOnly permission
    @property
    def owner(self):
        return self.user