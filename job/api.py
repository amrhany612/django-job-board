from cgitb import lookup
from yaml import serialize
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import job
from .serializers import JobSerializer
from rest_framework import generics

# @api_view(['GET'])
# def job_list_api(request):
#     all_jobs = job.objects.all()
#     data = JobSerializer(all_jobs, many=True).data
#     return Response({'data': data})

# @api_view(['GET'])
# def job_detail_api(request,id):
#     job_detail = job.objects.get(id=id)
#     data = JobSerializer(job_detail).data
#     return Response({'data':data})


class JobListApi(generics.ListCreateAPIView):
    queryset = job.objects.all()
    serializer_class = JobSerializer


class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = JobSerializer
    queryset = job.objects.all()
    lookup_field = 'id'
def edit_job(reques,id):
    pass