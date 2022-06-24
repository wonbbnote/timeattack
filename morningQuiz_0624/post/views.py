from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status

from post.serializers import JobPostSerializer
from .models import (
    JobPostSkillSet,
    JobType,
    JobPost,
    Company
)
from django.db.models.query_utils import Q


class SkillView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        job_serializer = JobPostSerializer(data=request.data)

        skills = self.request.query_params.getlist('skills', '')
        print("skills = ", end=""), print(skills)

        return Response(status=status.HTTP_200_OK)


class JobView(APIView):

    def post(self, request):
        jobpost_serializer = JobPostSerializer(data=request.data)
        job_type = int( request.data.get("job_type", None) )
        company_name = request.data.get("company_name", None)
        print("??")

        if jobpost_serializer.is_valid():
            category_instance = get_object_or_404(JobType, id=request.data['job_type'])

            jobpost_serializer.save(job_type=category_instance)
            return Response({"message": "ddd"}, status=status.HTTP_200_OK)
        print("??dddd")

        return Response(jobpost_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # job_description = request.data.get("job_description", None)
        # salary = int( request.data.get("salary", None) )

        # jobpost = JobPost.objects.create(job_type=job_type, 
        # company=company_name, job_description=job_description, salary=salary)
        # jobpost.save()



