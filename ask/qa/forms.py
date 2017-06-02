from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import PBKDF2PasswordHasher
from qa.models import Question, Answer


class FeedbackForm(forms.Form):
    email = forms.EmailField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

    def clean(self):
        if is_spam(self.clean_data):
            raise forms.ValidationError('Сообщение спам', code='spam')


class AnswerForm(forms.Form):
    text = forms.CharField(label='Answer', widget=forms.Textarea)
    # question = forms.IntegerField()

    def __init__(self, user, question, *args, **kwargs):
        self.user = user
        self.question = question
        super(AnswerForm, self).__init__(*args, **kwargs)

    def clean(self):
        if not self.cleaned_data['text'].strip() or not self.cleaned_data['text'].strip():
            raise forms.ValidationError('Одно или несколько полей пустое.')

    def save(self):
        self.cleaned_data['author'] = self.user
        self.cleaned_data['question'] = self.question
        answer = Answer(**self.cleaned_data)
        answer.save()
        return answer


class AskForm(forms.Form):
    title = forms.CharField(label='Question title:')
    text = forms.CharField(label='Description:', widget=forms.Textarea)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(AskForm, self).__init__(*args, **kwargs)

    def clean(self):
        if not self.cleaned_data['title'].strip() or not self.cleaned_data['text'].strip():
            raise forms.ValidationError('Одно или несколько полей пустое.')

    def save(self):
        self.cleaned_data['author'] = self.user
        ask = Question(**self.cleaned_data)
        ask.save()
        return ask


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def save(self):
        usr = super(SignUpForm, self).save(commit=False)
        password = self.cleaned_data['password']
        hasher = PBKDF2PasswordHasher()
        usr.password = hasher.encode(password, hasher.salt(), 36000)
        usr.save()
        return usr


