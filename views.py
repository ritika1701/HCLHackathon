from django.shortcuts import render,redirect
from .forms import question
from django.http import HttpResponse,HttpResponseRedirect

from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Question
from django.contrib.auth.decorators import login_required




def Admin_dash(request):
    context={
    'title':"welcome to the Admin dashboard"
    ''

    }
    return render(request,"forum/Admin_dash.html",context)
def member_dashboard(request):
    context={
    'title':"welcome to the member dashboard"

    }

     return render(request,"forum/member_dashboard.html",context)
def categories(request):
    context={
    'title':"choose the category to ask the question"
    'category': category
    }
    return render(request,"forum/category.html",context)





def ask_question(request):
    if not request.user.is_authenticated ():
        return HttpResponseRedirect(reverse("member_login"))
        form=Question(request.POST or None)
        context={
        "title":"welcome to the forum dashboard"
        "form":form,
        }
        if request.method=="POST":
            form = Question(request.POST or None)
            if form.is_valid():
                print (form.cleaned_data)
                question=fprm.cleaned_data['question']
                subject=form.cleaned_data['subject']
                User_Id=User.objects.get(pk=request.user.id)

                question =Question.object.create(question=question,sub=subject,User_Id=User_Id)
                question.save()
                message.success(request,"The question is successfully posted.")
                return redirect(reverse('ask_question'))

        return render(request,"forum/posting_quest.html",context)
def latest_question(request):
      question = Question.objects.all().order_by('-timestamp')

      context={
      'title':"Latest questions are",
      'question':question,
      }
      return render(request,"forum/view_question.html",context)

def answer(request,pk):
    if not request.user.is_authenticated ():
        return HttpResponseRedirect(reverse("member_login"))
        form=answer(request.POST or None)
        context={
        "title":"Add a answer"
        "form":form,
        }
        if request.method=="POST":
            form = answer(request.POST or None)
            if form.is_valid():
                print (form.cleaned_data)
                answer=form.cleaned_data['answer']
                Ques_Id=pk
                user_Id=User.objects.get(pk=request.user.id)
                ans =Answer.object.create(answer=answer,Ques_Id=Ques_id,User_Id=User_Id)
                ans.save()
                message.success(request,"The answer is successfully posted.")
                return redirect(reverse('view_question'))

        return render(request,"forum/posting_ans.html",context)

def  view_answers(request,pk):
    question = Question.objects.get(pk=pk)
    try:
        answer = Answer.objects.get(Ques_Id=question)
    except exception as e:
        context={
        'answer':"this question is unanswered",
        }
        return render(request,"forum/view_answer.html",context)

    context={
    'title':"The answers are",
    'answer': answer,
    }
    return render(request,"forum/view_answer.html",context)

def unanswered_ques(request):
    question = Question.objects.all()
    ans={}

    for pk in question:
        try:
            answer = Answer.objects.get(Ques_id=pk)
        except exception as e:
            for j in ans :
                j.append(pk)

    context={
    'title':"the answered questions are",
    'question'= question,
    'answer'= ans,
    }
    return render(request,"forum/unasnwered_ques.html",context)

def trending_question(request):
    question = Question.objects.all().order_by('-Views')[:50]
    context={
    'title': "The most viewed questions are"
    'question':question
    }

    return render(request,"forum/trending_question.html",question)

def view_comments(request,pk):
    comment = comments.objects.all(pk=pk)
    context={
    'title':" comments"
    'comment':comment
    }
    return render(request,"forum/view_comments.html",context)

def add_comments(request,pk):
    if not request.user.is_authenticated ():
        return HttpResponseRedirect(reverse("member_login"))
        form=Comment(request.POST or None)
        context={
        "title":"Add a comment"
        "form":form,
        }
        if request.method=="POST":
            form = Comment(request.POST or None)
            if form.is_valid():
                print (form.cleaned_data)
                comment=form.cleaned_data['comment']
                Ans_Id=pk
                user_Id=User.objects.get(pk=request.user.id)
                comment = comment.object.create(comment=answ,Ques_Id=Ques_id,User_Id=User_Id)
                question.save()
                message.success(request,"The comment is successfully posted.")
                return redirect(reverse('view_comments'))

        return render(request,"forum/posting_comment.html",context)


def upvote(request,pk):
  vo = Votes.objects.filter(Ans_Id=pk)
  try:
        vo.objects.get(User_Id=request.user.id)
        HttpResponse("You have already voted for this answer")
  expect e as Exception :
        vote= vote.object.create(Ans_Id=pk,User_Id=request.user,UP/Down='U')
        HttpResponse("you upvoted for this answer")
  Totalvotes= vo.objects.filter(UP/Down='U')- vo.objects.filter(UP/Down='D')
  return HttpResponse(Totalvotes)

def downvote(request,pk):
    vo = Votes.objects.filter(Ans_Id=pk)
    try:
          vo.objects.get(User_Id=request.user.id)
          HttpResponse("You have already voted for this answer")
    expect e as Exception :
          vote= vote.object.create(Ans_Id=pk,User_Id=request.user,UP/Down='U')
          HttpResponse("you upvoted for this answer")
    Totalvotes= vo.objects.filter(UP/Down='U')- vo.objects.filter(UP/Down='D')
    return HttpResponse(Totalvotes)
#calculating views per question
#session record ke basis pr chl rha 
def views(request):
      question = get_object_or_404(Question, pk=question_id)

    if not QuestionView.objects.filter(
                    question=question,
                    session=request.session.session_key):
        view = QuestionView(question=question,
                            ip=request.META['REMOTE_ADDR'],
                            created=datetime.datetime.now(),
                            session=request.session.session_key)
        view.save()

    return HttpResponse(u"%s" % QuestionView.objects.filter(question=question).count())
