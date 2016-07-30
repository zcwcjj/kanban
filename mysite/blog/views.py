from django.shortcuts import render
from .tasks import add
from django.template import Context, Template
from django.http import HttpResponse

# Create your views here.
def view1(request):
	
	result = add.delay(2,2)

	if result.ready():
		t = Template("my name is {{ name }}");
		c = Context({'name':"nowmagic"})
		return HttpResponse(t.render(c))
	else:
		t = Template("my name is {{ name }}");
		c = Context({'name':"not done"})
		return HttpResponse(t.render(c))		


