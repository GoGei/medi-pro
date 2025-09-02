from django import forms


class BaseModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=commit)
        if not self.request:
            return instance

        if instance.id and hasattr(instance, 'modify'):
            instance.modify(self.request.user, commit=commit)
        elif hasattr(instance, 'created_by_id'):
            instance.created_by_id = self.request.user.id
            if commit:
                instance.save(update_fields=['created_by_id'])

        return instance
