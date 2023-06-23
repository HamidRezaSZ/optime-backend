from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from missions.models import Mission


@receiver(post_save, sender=Mission)
def mission_created_signal(sender, instance, update_fields, **kwargs):
    try:
        driver = instance.driver

        if driver:
            if driver.mission_set.filter(done=False).exists():
                driver.free = False
                driver.save()
            else:
                driver.free = True
                driver.save()
    except Exception:
        pass


@receiver(post_delete, sender=Mission)
def mission_created_signal(sender, instance, **kwargs):
    try:
        driver = instance.driver

        if driver:
            if driver.mission_set.filter(done=False).exists():
                driver.free = False
                driver.save()
            else:
                driver.free = True
                driver.save()
    except Exception:
        pass
