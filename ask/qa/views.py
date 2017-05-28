from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest, Http404
from django.shortcuts import render, get_object_or_404
from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm

# q = Question(title="Halo")
# # q = q.objects.create(title="Py")
# q.title = "Halo2"
# q.objects
# q.save()


def add_question(request):
    axelet = User.objects.get(pk=1)
    lst = []
    q = Question(id=2, title="2", text="2", added_at="2017-01-02", rating=0, author=axelet, likes=[])
    lst.append(q)
    q = Question(id=3, title="3", text="3", added_at="2017-01-03", rating=0, author=axelet, likes=[])
    lst.append(q)
    q = Question(id=4, title="4", text="4", added_at="2017-01-04", rating=0, author=axelet, likes=[])
    lst.append(q)
    q = Question(id=5, title="5", text="5", added_at="2017-01-05", rating=0, author=axelet, likes=[])
    lst.append(q)
    q = Question(id=6, title="6", text="6", added_at="2017-01-06", rating=0, author=axelet, likes=[])
    lst.append(q)
    q = Question(id=7, title="7", text="7", added_at="2017-01-07", rating=0, author=axelet, likes=[])
    lst.append(q)
    q = Question(id=8, title="8", text="8", added_at="2017-01-08", rating=0, author=axelet, likes=[])
    lst.append(q)
    q = Question(id=9, title="9", text="9", added_at="2017-01-09", rating=0, author=axelet, likes=[])
    lst.append(q)
    q = Question(id=10, title="10", text="10", added_at="2017-01-10", rating=0, author=axelet, likes=[])
    lst.append(q)
    q = Question(id=11, title="11", text="11", added_at="2017-01-11", rating=0, author=axelet, likes=[])
    lst.append(q)
    q = Question(id=12, title="12", text="12", added_at="2017-01-12", rating=0, author=axelet, likes=[])
    lst.append(q)

    for question in lst:
        question.save()

    return HttpResponse(q.title, content_type='text/plain')


def view_question(request, *args, **kwargs):
    question = get_object_or_404(Question, pk=args[0])
    answers = Answer.objects.filter(question=question)
    if request.method == 'POST':
        a = AnswerForm(request.POST)
        if a.is_valid():
            answer = a.save(question)
            url = question.get_absolute_url()
            return HttpResponseRedirect(url)
    else:
        a = AnswerForm()
    return render(request, 'question.html', {
        'Question': question,
        'Answers': answers,
        'answer_form': a,
    })
    # return HttpResponse(' | '.join(q.get_full_info()) + '\n\n' + '\n'.join([x.text for x in answers]),
    #                     content_type='text/plain',
    #                     charset="CP1251"
    #                     )


def test(request, *args, **kwargs):
    # try:
    #     id = request.GET.get('id')
    #     obj = Question.objects.get(pk=id)
    #     obj
    # except Question.DoesNotExist:
    #     raise Http404
    obj = get_object_or_404(Question, pk=1)
    return HttpResponse(obj.text, content_type='text/plain', charset="CP1251")


def new(request):
    questions = Question.objects.order_by("-id")
    # questions = Question.objects.new_questions()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/question/'
    page = paginator.page(page)
    return render(request, 'page.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
        'limit': limit,
    })


def popular(request):
    questions = Question.objects.order_by("-rating")
    # questions = Question.objects.new()
    limit = request.GET.get('limit', 10)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/question/'
    page = paginator.page(page)
    return render(request, 'page.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
        'limit': limit,
    })


def ask(request):
    if request.method == 'POST':
        q = AskForm(request.POST)
        if q.is_valid():
            question = q.save()
            url = question.get_absolute_url()
            return HttpResponseRedirect(url)
    else:
        q = AskForm()
    return render(request, 'ask.html', {
        'ask_form': q
    })


