from django.db import models
from users.models import Role

class BusinessElement(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    def str(self):
        return self.name

class AccessRolesRule(models.Model):
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    business_element = models.ForeignKey(BusinessElement, on_delete=models.CASCADE)
    read_permission = models.BooleanField(default=False)
    read_all_permission = models.BooleanField(default=False)
    create_permission = models.BooleanField(default=False)
    update_permission = models.BooleanField(default=False)
    update_all_permission = models.BooleanField(default=False)
    delete_permission = models.BooleanField(default=False)
    delete_all_permission = models.BooleanField(default=False)

    class Meta:
        unique_together = (('role', 'business_element'),)

    def str(self):
        return f"{self.role} - {self.business_element}"
