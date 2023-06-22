from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from missions.models import Mission


@receiver(post_save, sender=Mission)
def mission_created_signal(sender, instance, update_fields, **kwargs):
    driver = instance.driver

    if driver:
        if driver.mission_set.filter(done=False).exists():
            driver.free = False
            driver.save()
        else:
            driver.free = True
            driver.save()


@receiver(post_delete, sender=Mission)
def mission_created_signal(sender, instance, **kwargs):
    driver = instance.driver

    if driver:
        if driver.mission_set.filter(done=False).exists():
            driver.free = False
            driver.save()
        else:
            driver.free = True
            driver.save()
