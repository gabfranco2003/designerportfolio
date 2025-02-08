from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')  # For project images

    def __str__(self):
        return self.title

class Hero(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    image = models.URLField(max_length=2080)  # For hero images

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Hero"  # Correct pluralization in admin

class AboutMe(models.Model):
    title = models.CharField(max_length=200, default="About Me")  # Allow customization
    content = models.TextField()
    image = models.ImageField(upload_to='about_me_images/', blank=True, null=True) # Optional image
    # Add other fields as needed (e.g., skills, experience, etc.)

    def __str__(self):
        return self.title  # Or a more descriptive representation
    
    class Meta:
        verbose_name_plural = "About Me" # Correct pluralization in admin

class ContactInfo(models.Model):
    email = models.EmailField()
    linkedin = models.URLField(blank=True, null=True)  # Optional LinkedIn URL
    instagram = models.URLField(blank=True, null=True)  # Optional Instagram
    # Add other contact details as needed

    def __str__(self):
        return "Contact Information"  # Or a more descriptive representation

    class Meta:
        verbose_name_plural = "Contact Information"
        
class Skill(models.Model):
    CATEGORY_CHOICES = [
        ('FE', 'Front-End'),
        ('BE', 'Back-End'),
        ('Design', 'Design'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Skills"
        ordering = ['category', 'name']  # Order by category and then name
        
class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)  # Optional end date
    description = models.TextField(blank=True, null=True) # Optional description

    def __str__(self):
        return f"{self.degree} at {self.institution}"

    class Meta:
        ordering = ['-end_date', '-start_date']  # Most recent first
        
class Experience(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)  # Optional end date
    description = models.TextField(blank=True, null=True) # Optional description

    def __str__(self):
        return f"{self.title} at {self.company}"

    class Meta:
        ordering = ['-end_date', '-start_date']  # Most recent first