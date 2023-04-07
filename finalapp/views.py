from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

import numpy as np
#from .views import detail_view
from django.urls import path

from django.shortcuts import (get_object_or_404,
                              render,
                              HttpResponseRedirect)
import os
import pandas as pd
import pickle

# def homepage1(request):
#     return render(request,"homepage1.html")

# def tpage(request):
#     return render(request,"t.html")



#model code form
def index(request):
    return render(request,'index.html')

my_dir = os.path.dirname(__file__)
pickle_file_path = os.path.join(my_dir, 'lr_clf.pkl')
with open(pickle_file_path, 'rb') as pickle_file:
    model = pickle.load(pickle_file)
# model=pickle.load(open(r'C:\Users\aarbs\new_project2\finalapp\lr_clf.pkl','rb+'))
def predict(request):
     if request.method=='POST':       
        temp={}
        p={} #personality dict
        d={"Strongly Disagree": 1,"Disagree":2,"Slightly Disagree":3,"Neutral":4,"Slightly Agree":5,"Agree":6,"Strongly Agree":7}
        temp['1']=int(request.POST.get('db_rating')) 
        temp['2']=int(request.POST.get('comp_arch_rating')) 
        temp['3']=int(request.POST.get('dist_comp_rating')) 
        temp['4']=int(request.POST.get('cybersecurity')) 
        temp['5']=int(request.POST.get('networking')) 
        temp['6']=int(request.POST.get('development')) 
        temp['7']=int(request.POST.get('programmingskills')) 
        temp['8']=int(request.POST.get('project_management_rating')) 
        temp['9']=int(request.POST.get('computer_forensics_fundamental_rating')) 
        temp['10']=int(request.POST.get('technical_communication_rating')) 
        temp['11']=int(request.POST.get('ai_ml_rating')) 
        temp['12']=int(request.POST.get('software_eng_rating')) 
        temp['13']=int(request.POST.get('business_analysis_rating')) 
        temp['14']=int(request.POST.get('communication_skills_rating')) 
        temp['15']=int(request.POST.get('data_science_rating')) 
        temp['16']=int(request.POST.get('troubleshooting-rating')) 
        temp['17']=int(request.POST.get('graphics-designing-rating')) 

        p['ext1']=int(d[request.POST.get('ext1')])
        p['ext2']=int(d[request.POST.get('ext2')])
        p['ext3']=int(d[request.POST.get('ext3')])
        p['ext4']=int(d[request.POST.get('ext4')])
        p['est1']=int(d[request.POST.get('est1')])
        p['est2']=int(d[request.POST.get('est2')])
        p['est3']=int(d[request.POST.get('est3')])
        p['est4']=int(d[request.POST.get('est4')])

        p['agr1']=int(d[request.POST.get('agr1')])
        p['agr2']=int(d[request.POST.get('agr2')])
        p['agr3']=int(d[request.POST.get('agr3')])
        p['agr4']=int(d[request.POST.get('agr4')])
        p['csn1']=int(d[request.POST.get('csn1')])
        p['csn2']=int(d[request.POST.get('csn2')])
        p['csn3']=int(d[request.POST.get('csn3')])
        p['csn4']=int(d[request.POST.get('csn4')])
        p['opn1']=int(d[request.POST.get('opn1')])
        p['opn2']=int(d[request.POST.get('opn2')])
        p['opn3']=int(d[request.POST.get('opn3')])
        p['opn4']=int(d[request.POST.get('opn4')])
        p['otc']=int(d[request.POST.get('otc')])
        p['hed']=int(d[request.POST.get('hed')])

        p['ste1']=int(d[request.POST.get('ste1')])
        p['ste2']=int(d[request.POST.get('ste2')])
        p['ste3']=int(d[request.POST.get('ste3')])
        p['ste4']=int(d[request.POST.get('ste4')])

        p['con']=int(d[request.POST.get('con')])
        p['emo']=int(d[request.POST.get('emo')])

        p['set1']=int(d[request.POST.get('set1')])
        p['set2']=int(d[request.POST.get('set2')])
        p['set3']=int(d[request.POST.get('set3')])
        p['set4']=int(d[request.POST.get('set4')])
        
        
        temp['otc']=p['otc']/7
        temp['hed']= p['hed']/7
        temp['ste']= (p['ste1'] + p['ste2'] + p['ste3'] + p['ste4'])/28
        temp['set']= (p['set1'] + p['set2'] + p['set3'] + p['set4'])/28
        temp['con']= p['con']/7
        temp['emo']=p['emo']/7
        # gen=0
        temp['ext'] = (p['ext1'] + p['ext2'] + p['ext3'] + p['ext4'])/28
        #neuroticism = (p[EST1] + p[EST2] + p[EST3] + p[EST4])/2.50
        temp['agr'] = (p['agr1'] + p['agr2'] + p['agr3'] + p['agr4'])/28
        temp['csn'] = (p['csn1'] + p['csn2'] + p['csn3'] + p['csn4'])/28
        temp['opn'] = (p['opn1'] + p['opn2'] + p['opn3'] + p['opn4'])/28
        # age=int(a)

        testdata=pd.DataFrame({'x':temp}).transpose()
        scoreval=model.predict(testdata)[0]
        pred=''
        if scoreval == 0:
               pred = 'AI ML Specialist'
        elif scoreval==1:
            pred = 'API Specialist'
        elif scoreval ==2:
            pred = 'Application Support Engineer'
        elif scoreval ==3:
            pred = 'Business Analyst'
        elif scoreval ==4:
            pred = 'Customer Service Executive'
        elif scoreval ==5:
            pred = 'Cyber Security Specialist'
        elif scoreval ==6:
            pred = 'Database Administrator'
        elif scoreval ==7:
            pred = 'Graphics Designer'
        elif scoreval ==8:
            pred = 'Hardware Engineer'
        elif scoreval ==9:
            pred = 'Helpdesk Engineer'
        elif scoreval ==10:
            pred = 'Information Security Specialist'
        elif scoreval ==11:
            pred = 'Networking Engineer'
        elif scoreval ==12:
            pred = 'Project Manager'
        elif scoreval ==13:
            pred = 'Software Developer'
        elif scoreval ==14:
            pred = 'Software tester'
        elif scoreval ==15:
            pred ='Technical Writer'
        
        #for top 3
        probs_1= model.predict_proba(testdata)
        
        probs=probs_1[0]
        m=len(probs)
        roles={probs[0]:'AI ML Specialist',probs[1]:'API Specialist', probs[2]:'Application Support Engineer',
        probs[3]:'Business Analyst'
        ,probs[4]:'Customer Service Executive',probs[5]:'Cyber Security Specialist',
        probs[6]:'Database Administrator'
        ,probs[7]:'Graphics Designer'
        ,probs[8]:'Hardware Engineer',probs[9]:'Helpdesk Engineer',probs[10]:'Information Security Specialist',
        probs[11]:'Networking Engineer'
        ,probs[12]:'Project Manager',probs[13]:'Software Developer',probs[14]:'Software tester',probs[15]:'Technical Writer'}

        x=np.sort(probs)
        top=x[13:16]
        l=[]

        for i in range(2,-1,-1):
            l.append([roles[top[i]],int(top[i])*100])
        
        # pages={'AI ML Specialist':'https://resources.workable.com/machine-learning-engineer-job-description#:~:text=Designing%20and%20developing%20machine%20learning,Implementing%20appropriate%20ML%20algorithms'}
        # yy=pages[l[0][0]]
        return render(request,'result.html',{'result':pred,'x':l[0][0],'y':l[1][0],'z':l[2][0]})
        #return render(request,'result.html',{'result':pred,'x':l[0][0],'y':l[1][0],'z':l[2][0],'po':yy})
