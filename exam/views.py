from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core import urlresolvers
from django.contrib import messages
import datetime
import survey.settings

from models import Question, Survey, Category
from forms import ResponseForm

def index2(request):
    return HttpResponse("Hello, world. You're at the poll index.")

def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)


########################################################################################3
def Index(request):
	return render(request, 'index.html')

def SurveyDetail(request, id):
	survey = Survey.objects.get(id=id)
	category_items = Category.objects.filter(survey=survey)
	categories = [c.name for c in category_items]
	print 'categories for this survey:'
	print categories
	if request.method == 'POST':
		form = ResponseForm(request.POST, survey=survey)
		if form.is_valid():
			response = form.save()
			return HttpResponseRedirect("/exam/confirm/%s" % response.interview_uuid)
	else:
		form = ResponseForm(survey=survey)
		print form
		# TODO sort by category
	return render(request, 'survey.html', {'response_form': form, 'survey': survey, 'categories': categories})

def Confirm(request, uuid):
	email = survey.settings.support_email
	return render(request, 'confirm.html', {'uuid':uuid, "email": email})


