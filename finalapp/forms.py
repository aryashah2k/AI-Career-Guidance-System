from django import forms
from .models import user_details
 
 
# creating a form
class user_details_form(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = user_details
 
        # specify fields to be used
        fields = [
            "title",
            "name_user",
            "Database_Fundamentals",
            "Computer_Architecture",
            "Distributed_Computing",
            "Cyber_Security",
            "Networking", 
            "Development",
            "Programming_Skills",
            "Project_Management", 
            "Computer_Forensics",
            "Technical_Communication",
            "AI_ML", 
            "Software_Engineering", 
            "Business_Analysis", 
            "Communication_skills", 
            "Data_Science", 
            "Troubleshooting_skills", 
            "Graphics_Designing",
            "Openness",
            "Conscientiousness", 
            "Extraversion", 
            "Agreeableness", 
            "Emotional_Range", 
            "Conversation",
            "Openness_Change",
            "Hedonism", 
            "Self_enhancement",
            "Self_transcendence"
            
        ]