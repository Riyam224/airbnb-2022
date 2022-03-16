from xml.parsers.expat import model
from django.db import models
from django.forms import ImageField
from django.utils.translation import gettext as _

# Create your models here.


class Settings(models.Model):
    site_name = models.CharField(_("site name"), max_length=150)
    logo = models.ImageField(_("logo"), upload_to='settings/')
    phone = models.CharField(_("phone"), max_length=520)
    email = models.CharField(_("email"), max_length=520)
    address =  models.CharField(_("address"), max_length=520)
    description = models.TextField(_("description"))
    fb_link = models.URLField(_("fb link"), max_length=200)
    twitter_link = models.URLField(_("twitter link"), max_length=200)
    instagram_link = models.URLField(_("instagram link"), max_length=200)


    

    class Meta:
        verbose_name = _("Settings")
        verbose_name_plural = _("Settingss")

    def __str__(self):
        return self.site_name

 