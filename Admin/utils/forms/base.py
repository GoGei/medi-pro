from django import forms


class BaseModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

    def save_on_create(self, commit=True):
        if self.request:
            self.cleaned_data['created_by'] = self.request.user
        return super().save(commit=commit)

    def save_on_edit(self, commit=True):
        instance = super().save(commit=commit)
        if self.request and hasattr(instance, 'modify'):
            instance.modify(self.request.user)

        return instance
