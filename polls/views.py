from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Choice

def index(request):
    questions = Question.objects.all()
    return render(request, 'polls/index.html', {'questions': questions})

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        choice = question.choice_set.get(pk=request.POST['choice'])
    except:
        return render(request, 'polls/detail.html', {
            'question': question,
            'error': "No has seleccionat cap opció.",
        })
    choice.votes += 1
    choice.save()
    return redirect('results', question_id=question.id)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})
