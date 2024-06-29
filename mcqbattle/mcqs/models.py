from django.db import models
import uuid


# Create your models here.

#MCQ Model (fields: Ques_id, body, explanation, options)
class MCQ(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    body = models.TextField()
    explanation = models.TextField()
    options = models.JSONField()
    
