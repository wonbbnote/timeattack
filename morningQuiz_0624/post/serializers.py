from rest_framework import serializers
from .models import Company, JobPost, JobPostSkillSet


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields= ["company_name", "business_area"]

class JobPostSerializer(serializers.ModelSerializer):
    company_name = CompanySerializer()
    class Meta:
        model = JobPost
        fields= ["job_type", "company_name", "job_description", "salary"]

class JobPostSkillSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPostSkillSet
        fields= ["skill_set", "job_post"]