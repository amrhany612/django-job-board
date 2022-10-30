from django.shortcuts import render
from matplotlib.style import context
from job.models import job
from job import views
# Create your views here.
def home(request):
    job_all = job.objects.all()
    job_detail = views.job_detail
    context={"jobs":job_all}
    return render(request,'home/index.html',context)

