from django.db import models #building blocks for db
from django.urls import reverse  #generates a URL from a page's name instead of hardcoding it

#First model: Domain (5 categories that my project falls under: CV, NLP, ML, Web Dev and Other)
class Domain(models.Model):
    name = models.CharField(max_length=60, unique=True)
    slug = models.SlugField(unique=True)
    accent = models.CharField(max_length=20, default = "blue")
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    tagline = models.CharField(max_length=100)
    description = models.TextField()
    domain = models.ForeignKey(Domain, on_delete=models.CASCADE, related_name="projects")
    image = models.ImageField(upload_to="projects/images/") #pip install pillow
    tech_stack = models.CharField(max_length=100)
    github_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order", "title"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"slug": self.slug})


class SkillGroup(models.Model):
    name = models.CharField(max_length=50)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return self.name

    
class Skill(models.Model):
    name = models.CharField(max_length=50)
    group = models.ForeignKey(SkillGroup, on_delete=models.CASCADE, related_name="skills")
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return self.name


class Certification(models.Model):
    name = models.CharField(max_length=100)
    organization = models.CharField(max_length=100)
    url = models.URLField(blank=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order", "name"]

    def __str__(self):
        return self.name