# documents/forms.py

from django import forms
from .models import AgentDocument

class AgentDocumentForm(forms.ModelForm):
    class Meta:
        model = AgentDocument
        fields = ['agent', 'document_type']  # Обратите внимание на то, что поля должны совпадать с моделью
        widgets = {
            'agent': forms.Select(attrs={'class': 'form-control'}),
            'document_type': forms.Select(choices=AgentDocument.ACTION_CHOICES, attrs={'class': 'form-control'}),
        }
