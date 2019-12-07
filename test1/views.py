from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound,Http404
# Create your views here.
from .models import Candidate, Poll, Choice, Boardlist
from django.db.models import Sum
from django.views.decorators.csrf import csrf_exempt
import datetime
from django.shortcuts import render, redirect
from .form import PostForm
from .models import Post


# def index(request):
#     candidates=Candidate.objects.all()
#     str='' 
#     for candidate in candidates:
#         str += "<p> {} {}번({})<br>".format(candidate.name,candidate.partynum,candidate.area)
#         str+=candidate.introduction+"</p>"
#     return HttpResponse(str) 
def index(request):
    candidates=Candidate.objects.all()
    context={'candidates' : candidates}
    return render(request,'test1/index.html',context) 

def board(request):
    boardlist=Boardlist.objects.all()
    context={'boardlist' : boardlist}
    return render(request,'test1/board.html',context) 

def writeboard(request):
    
    return render(request,'test1/writeboard.html') 
@csrf_exempt
def writemanage(request):
    names=request.POST['names']
    introductions=request.POST['introductions']
    boardlist = Boardlist(name = names, introduction=introductions)
    boardlist.save()
    return HttpResponseRedirect("board")
@csrf_exempt
def deleteboard(request):
    names=request.POST['deletename']
    deleteunit=Boardlist.objects.get(name=names)
    deleteunit.delete()
    return HttpResponseRedirect("board")

# def areas(request,area):
#     today=datetime.datetime.now()
    
#     try:
#         poll = Poll.objects.get(area = area, start_date= today, end_date=today) # get에 인자로 조건을 전달해줍니다. 
#         print(poll)
#         candidates = Candidate.objects.filter(area = area) # Candidate의 area와 매개변수 area가 같은 객체만 불러오기
#     except:
#         poll=None
#         print(poll)
#         candidates=None
#     context={'candidates':candidates,'area':area,'poll':poll}
#     return render(request,'test1/area.html',context)
def areas(request, area):
    today = datetime.datetime.now()
    
    try :
        poll = Poll.objects.get(area = area) # get에 인자로 조건을 전달해줍니다. 
        
        candidates = Candidate.objects.filter(area = area) # Candidate의 area와 매개변수 area가 같은 객체만 불러오기
    except:
        poll = None
        candidates = None
    context = {'candidates': candidates,
    'area' : area,
    'poll' : poll }
    return render(request, 'test1/area.html', context)

def polls(request, poll_id):
    poll = Poll.objects.get(pk = poll_id)
    selection = request.POST.get('choice','')
    print(poll)
    try: 

        choice = Choice.objects.get(poll_id = poll.id, candidate_id = selection)
        choice.votes += 1
        choice.save()  
    except:

        #최초로 투표하는 경우, DB에 저장된 Choice객체가 없기 때문에 Choice를 새로 생성합니다
        choice = Choice(poll_id = poll_id, candidate_id = selection, votes = 1)
        choice.save()

    return HttpResponseRedirect("/areas/{}/results".format(poll.area))

def results(request, area):
    candidates = Candidate.objects.filter(area = area)
    polls = Poll.objects.filter(area = area)
    poll_results = []
    for poll in polls:
        result = {}
        result['start_date'] = poll.start_date
        result['end_date'] = poll.end_date

        # poll.id에 해당하는 전체 투표수
        total_votes = Choice.objects.filter(poll_id = poll.id).aggregate(Sum('votes'))
        result['total_votes'] = total_votes['votes__sum']

        rates = [] #지지율
        for candidate in candidates:
            # choice가 하나도 없는 경우 - 예외처리로 0을 append
            try:
                choice = Choice.objects.get(poll = poll, candidate = candidate)
                rates.append(
                    round(choice.votes * 100 / result['total_votes'], 1)
                    )
            except :
                rates.append(0)
        result['rates'] = rates
        poll_results.append(result)

    context = {'candidates':candidates, 'area':area,
    'poll_results' : poll_results}
    return render(request, 'test1/results.html', context)

def candidates(request, name):
    # candidate=Candidate.objects.get(name=name)
    try:
        candidate=Candidate.objects.get(name=name)
    except:
        return HttpResponseNotFound("없는 페이지")
        raise Http404
    # candidate=get_object_or_404(Candidate,name=name)
    return HttpResponse(candidate.name)
