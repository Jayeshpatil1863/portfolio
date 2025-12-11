from django import forms
from django.db import models

class Survey(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    contact = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "survey_data"

    def __str__(self):
        return self.name if self.name else "Anonymous User"

class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = ['name', 'contact', 'message']