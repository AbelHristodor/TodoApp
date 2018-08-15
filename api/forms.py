from django import forms
from .models import Todo

class TodoForm(forms.ModelForm):
    """Form definition for Todo."""

    def __init__(self, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)
    
    class Meta:
        """Meta definition for Todoform."""

        model = Todo
        fields = ('details', 'due_date')

