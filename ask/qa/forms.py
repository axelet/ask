from django import forms
from django.contrib.auth.models import User
from qa.models import Question, Answer


class FeedbackForm(forms.Form):
    email = forms.EmailField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)

    def clean(self):
        if is_spam(self.clean_data):
            raise forms.ValidationError('Сообщение спам', code='spam')

class AskForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)

    def clean(self):
        if not self.cleaned_data['title'].strip() or not self.cleaned_data['text'].strip():
            raise forms.ValidationError('Одно или несколько полей пустое.')

    def save(self):
        ask = Question(**self.cleaned_data)
        ask.author = User.objects.filter(pk=2)[0]
        ask.save()
        return ask

class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField()

    def clean(self):
        if not self.cleaned_data['text'].strip() or not self.cleaned_data['text'].strip():
            raise forms.ValidationError('Одно или несколько полей пустое.')

    def save(self, question):
        self.cleaned_data["question"] = question
        answer = Answer(**self.cleaned_data)
        # answer.question = Question.objects.get(pk=self.cleaned_data["question"])
        answer.author = User.objects.get(pk=2)
        answer.save()
        return answer
