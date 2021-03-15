user =dict();
userregimen=dict();
newregimen = dict();

bmi_le_185 ={'Mon':'Chest','Tue':'Biceps','Wed':'Rest','Thu':'Back','Fri':'Triceps','Sat':'Rest','Sun':'Rest'};
bmi_le_25 ={'Mon':'Chest','Tue':'Biceps','Wed':'Cardio/Abs','Thu':'Back','Fri':'Triceps','Sat':'Legs','Sun':'Rest'};
bmi_le_30 ={'Mon':'Chest','Tue':'Biceps','Wed':'Abs/Cardio','Thu':'Back','Fri':'Triceps','Sat':'Legs','Sun':'Cardio'};
bmi_ge_30 ={'Mon':'Chest','Tue':'Biceps','Wed':'Cardio','Thu':'Back','Fri':'Triceps','Sat':'Cardio','Sun':'Cardio'};
regimens = [bmi_le_185,bmi_le_25,bmi_le_30,bmi_ge_30]

def Create_member():
    u=dict();
    
    u['\nName']=input('Name : ');
    u['Age'] = input('Age : ');
    u['Gender'] = input('Gender : ');
    u['Mobile number'] = input('Mobile number : ');
    u['Email'] = input('Email : ');
    while True:
        u['BMI']=input('BMI : ');
        if u['BMI'].isnumeric():
            break;
        else:
            print('Enter a positive number.\n')
    u['Membership'] = input('Membership Duration in months(1,3,6 or12) : ');
    
    user[u['Mobile number']]=u;
    
    
    
    while True:
        print('\n There are 2 types of workouts regimens in Edyoda Gym:\n');
        print('1:BMI based Regimens\n2:Celebrity Regimens\n0:Exit');
        print('What would you like to opt for?\n');
        print('If you have opted just now, you can exit.');
        while True:
            o = input();
            if o.isnumeric and (o=='1' or o=='2'or o=='0'):
                break;
            else:
                print('Enter a valid input.\n');
                
        if o=='1':
            userregimen[u['Mobile number']] = Regimen(int(u['BMI']));
            print('Your workout regimen is created\n');
                                                      
        if o =='2':
            if len(newregimen)==0:
               print('Currently, There are no celebrity regimens available here.\n');
                                                      
            else:                                          
                print('These are the Celebrity Regimens:\n');
                for z in newregimens:
                    print(z,'\n');
                print('Please enter the regimen name, you want to opt for.\n')                                      
                while True:
                     v = input();                                 
                     if v in newregimens:
                          break;
                     else:
                          print('Enter a valid input.\n');                            
                userregimen[u['Mobile number']] = newregimen[v];                                      
                                                      
        if o == '0':                                            
             break;                                     
                                                      
def View_member():
    if len(user) ==0:
        print('There are no members in this gym');
    else:
        print('Please enter the contact number\n');
        while True:
        
           i = input();
           if i in user:
               for j in user[i]:
                   print(j,': ',user[i][j]);
               break;
                   
           else:
               print('Entered contact number doesnt exist\n');\
               break;
            
    
            
def Delete_member():
    print('Please enter the contact number\n');
    while True:
        
        i = input();
        if i in user:
            for r in user.keys():
            
                if r == i:
                   del user[i];
                print('Member has been deleted');
                break;
            break;
        else:
            print('Entered contact number doesnt exist\n');
            break;
            
        

def Update_member():
    print('Please enter the contact number\n');
    while True:
        
        i = input();
        if i in user:
            _ = user[i]['Membership'];
            print ('Your Membership duration is ', _,'\n');
            
        
            print('1:Extend\n2:Revoke\n0:exit\n');
            while True :
                b = input();
                if b == '0' or b=='1' or b=='2':
                   break;
                else:
                   print('Enter a valid input\n');
                
            if b =='1':
                while True:
                
                    print('Enter the number of months to be extended : \n');
                    k = input();
                    if k.isnumeric():
                       break;
                    else:
                       print('Enter a valid input\n');
                _ = str(int(_) +int(k));
                print ('Your Membership extended by ', k,'months\n');
                user[i]['Membership'] = _;
                break;
        
            if b =='2':
                print('Do you really want the revoke the membership?\n');
                print('Yes - Revoke     No - Cancel');
                while True:
                   l =input();
                   if l =='Yes' or l =='No':
                      break;
                   else:
                      print('Enter a valid input\n');
                    
                if l =='Yes':
                   user[i]['Membership'] = '0';
                   print ('Your Membership is revoked\n');
                
                
                if l =='No':
                
                   print('Your Membership is not revoked\n');
                   break;
                break;
            
            if b=='0':
                break;
            break;
            
        else:
           print('Entered contact number doesnt exist\n');
           break;
    
    
    
    
    
            
            
def Create_Regimen():
    print('Enter the title of new workout regimen\n');
    x = input();
    u=dict();
    
    u['Mon']= input('Mon : ');
    u['Tue']= input('Tue : ');
    u['Wed']= input('Wed : ');
    u['Thu']= input('Thu : ');
    u['Fri']= input('Fri : ');
    u['Sat']= input('Sat : ');
    u['Sun']= input('Sun : ');
    
    newregimen[x] =u;
    
def View_Regimen():
    print('There are two types of regimens in Edyoda Gym:\n');
    
    
    
    while True:
        print('1:BMI Regimens\n2: Celebrity Regimens\n0:exit');
        while True:
            x = input();
            if x =='1' or x=='2'or x=='0':
                break;
            else:
                print('Enter a valid input\n')
        
        if x=='1':
            print('Enter the BMI value:\n');
            while True:
                c = input();
                if c.isnumeric():
                    break;
                else:
                    print('Enter a valid input\n');
            h=Regimen(int(c));
            
            for q in h:
                 print(q,' : ',h[q]);                                   
                                                      
            
            
        if x=='2':
            if len(newregimen) ==0:
                print('This is empty.\n');
                
            else:
                print('These are the Celebrity regimens:\n')
                for u in newregimen:
                    print(u+'\n');
                
                print('Enter the regimen name to view it.\n')
                
                while True:
                    p = input();
                    if p in newregimen:
                       break;
                    else:
                       print('Enter a valid input.\n');
                if type(newregimen[p]) != dict:
                    print('That regimen has been deleted');
                else:
                    for j in newregimen[p]:
                        print(j," : ",newregimen[p][j],'\n');
        
        if x== '0':
            break;
            
def Delete_Regimen():
    
    if len(newregimen) ==0:
        print('There are only default regimens, you cannot delete those, you can update those.\n');
        
    else:
        print('These are the regimens, you can delete.\n');
        for t in newregimen:
            print(t+'\n');
        print('Enter the regimen name to Delete it.\n');
        while True:
            p = input();
            if p in newregimen:
            	break;
            else:
                print('Enter a valid input.\n');
            
        print('Regimen has been deleted.\n');    
        newregimen[p] ='This Regimen has been deleted.\n Please contact superuser to update your regimen.\n';
        
        
def  Update_Regimen():
    print('There are two types of regimens in Edyoda Gym:\n');
    
    
    
    while True:
        print('1:BMI Regimens\n2: Celebrity Regimens\n0:exit');
        while True:
            x = input();
            if x =='1' or x=='2'or x=='0':
                break;
            else:
            	print('Enter a valid input\n')
        
        if x=='1':
            print('Enter the BMI value to update the regimen:\n');
            while True:
                c = input();
                if c.isnumeric():
                    break;
                else:
                    print('Enter a valid input\n');
            
            if int(c)<18.5:
                bmi_le_185['Mon'] =input('Mon : ');
                bmi_le_185['Tue'] =input('Tue : ');
                bmi_le_185['Wed'] =input('Wed : ');
                bmi_le_185['Thu'] =input('Thu : ');
                bmi_le_185['Fri'] =input('Fri : ');
                bmi_le_185['Sat'] =input('Sat : ');
                bmi_le_185['Sun'] =input('Sun : ');
                
                
            if int(c)>=18.5 and int(c)<25 :
                
                bmi_le_25['Mon'] =input('Mon : ');
                bmi_le_25['Tue'] =input('Tue : ');
                bmi_le_25['Wed'] =input('Wed : ');
                bmi_le_25['Thu'] =input('Thu : ');
                bmi_le_25['Fri'] =input('Fri : ');
                bmi_le_25['Sat'] =input('Sat : ');
                bmi_le_25['Sun'] =input('Sun : ');
                
                
        
            if int(c)>=25 and int(c)<30:
                
                bmi_le_30['Mon'] =input('Mon : ');
                bmi_le_30['Tue'] =input('Tue : ');
                bmi_le_30['Wed'] =input('Wed : ');
                bmi_le_30['Thu'] =input('Thu : ');
                bmi_le_30['Fri'] =input('Fri : ');
                bmi_le_30['Sat'] =input('Sat : ');
                bmi_le_30['Sun'] =input('Sun : ');
                
            if int(c)>=30:
                
                bmi_ge_30['Mon'] =input('Mon : ');
                bmi_ge_30['Tue'] =input('Tue : ');
                bmi_ge_30['Wed'] =input('Wed : ');
                bmi_ge_30['Thu'] =input('Thu : ');
                bmi_ge_30['Fri'] =input('Fri : ');
                bmi_ge_30['Sat'] =input('Sat : ');
                bmi_ge_30['Sun'] =input('Sun : ');
                
            
        if x=='2':
            if type(newregimen) != dict():
                print('This is empty.\n');
                
            else:
                print('These are the Celebrity regimens:\n')
                for w in newregimen:
                    print(w+'\n');
                
                print('Enter the regimen name to update it.\n')
                
                while True:
                    p = input();
                    if p in newregimen:
                        break;
                    else:
                        print('Enter a valid input.\n');
                for j in newregimen[p]:
                    newregimen[p][j] = input(j,' : ');
        
        if x== '0':
            break;
    
    
       
    
def  Regimen(bmi):
    
    
    
    
    if bmi<18.5:
        return bmi_le_185;
    if bmi>=18.5 and bmi<25 :
        return bmi_le_25;
        
    if bmi>=25 and bmi<30:
        return bmi_le_30;
    if bmi>=30:
        return bmi_ge_30;
            