from django.db import models

class dept(models.Model):
    name = models.CharField(max_length=50)
    floor = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'dept'
