from Modules import *

def gymmembership():
    
    print('wecome to Edyoda gym online portal!\n')
    
    
    while True:
        print('\n1:Member\n2:Superuser\n0:exit\n');
        while True:
            g = input();
        
            if g.isnumeric() and (g=='1' or g=='2' or g=='0'):
                break
            else:
                print('Enter valid inputs.\n')
    
        if g == '1':
	    
            print('\nif your number doesnt exist in database, it will again go back to menu.\nPlease enter contact no. for logging in - \n');
            x = input();

            if x in f.user:
    	        member(x);
            else:
                print('\nThis Contact number doesnt exist in our database\n');
	             
        
            
        
        if g =='2':
            print('Welcome Boss!');
            print('Please enter your portal password.');
            while True:
                x = input();
                if x == '********':
                    break
                else:
                    print('Password is incorrect\n')
            
                
            superuser();
        
        if g =='0':
            break;
    
    
        

def superuser():
    print('Welcome Boss!\n')
    
    
    while True:
        
        print('Here are the list of things you can do.\n');
        print('1:Create Member\n2:View Memeber\n3:Delete Member\n4:Update Memeber\n5:Create Regimen\n6:View Regimen\n7:Delete Regimen\n8:Update Regimen\n0:exit')
        while True:
            x = input();
            if x.isnumeric() and int(x)<= 8 and int(x)>=0 :
                break;
            else:
                print('Enter a valid input');
        
    
        if int(x) ==1:
            f.Create_member();
        if int(x) ==2:
            f.View_member();
        if int(x) ==3:
            f.Delete_member();
        if int(x) ==4:
            f.Update_member();
        if int(x) ==5:
            f.Create_Regimen();
        if int(x) ==6:
            f.View_Regimen();
        if int(x) == 7:
            f.Delete_Regimen();
        if int(x) ==8:
            f.Update_Regimen();
        if int(x)  ==0:
            break;
        
def  member(a):
    
    while True:
        print('1: \nMy Regimen\n2:My Profile\n0:Exit\n');
        while True:
            x = input();
            if x.isnumeric() and int(x)<= 2 and int(x)>=0 :
                break;
            else:
                print('Enter a valid input');
        if x=='1':
            regimen = f.userregimen[a];
             
            for i in regimen:
                print(i,' : ',regimen[i]);
            
        if x=='2':
            for i in f.user[a]:
                print(i,': ',f.user[a][i]);
            
        if x=='0':
            break;
gymmembership();