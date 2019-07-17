from django.db import models

class HeaderSection(models.Model):
    master_heading = models.CharField(max_length=30, blank=True, null=True)
    sub_heading = models.CharField(max_length=50, blank=True, null=True)

class PortfolioSection(models.Model):
    project_name = models.CharField(max_length=30, blank=False, null=False)
    project_image = models.FileField(upload_to='media/project_image/')
    project_description = models.TextField(max_length=5000, blank=False, null=False)
    project_github_url = models.CharField(max_length=300, blank=True, null=True)
    project_bitbucket_url = models.CharField(max_length=300, blank=True, null=True)
    project_view_url = models.CharField(max_length=5000, blank=True, null=True)
