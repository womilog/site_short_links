from django import forms

from main.models import Link


class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['full_url', 'short_url']
        labels = {'full_url': 'Полная ссылка', 'short_url': 'Сокращенная ссылка'}

    def clean_short_url(self):
        short_url = self.cleaned_data['short_url']
        if Link.objects.filter(short_url=short_url).exists():
            raise forms.ValidationError('Сокращенная ссылка уже существует')
        return short_url


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=255)
    email = forms.EmailField(label='Email')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))

