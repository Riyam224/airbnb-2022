
from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class About(models.Model):
    what_we_do = models.TextField(_("what we do"))
    our_mission = models.TextField(_("our mission"))
    our_goals = models.TextField(_("our goals"))
    image = models.ImageField(_("image"), upload_to='about/')

    

    class Meta:
        verbose_name = _("About")
        verbose_name_plural = _("Abouts")

    def __str__(self):
        return str(self.id)



class FAQ(models.Model):
    title = models.CharField(_("title"), max_length=150)
    description = models.TextField(_("description"))

    

    class Meta:
        verbose_name = _("FAQ")
        verbose_name_plural = _("FAQs")

    def __str__(self):
        return self.title

 