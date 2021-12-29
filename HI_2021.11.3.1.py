
# pip install PyDictionary
# pip install platform
# pip install psutil



import os
import datetime
from PyDictionary import PyDictionary
import getpass
import platform
import random
import psutil




# predefined and learned data storage
all_opertor = []

nexx_info = ['Nexx', 'I am Nexx', 'I am Nexx Version 2021.10.1', 'I have been created by Satyam Mishra Aka Bedead']

greeting = {'good' : ["Good Morning", "Good night", "Good Afternoon", 'Good evening'],
            'casual_start' : ['Hope you are having a good day', 'Nice to meet you','Hey, how do you do?','How do you do?', 'how are you doing?','Pleased to meet you',
                              'How have you been','How’s it going','Nice to see you',"It’s great to see you","Good to see you",'What’s up?','Heyyy'],
            'casual_end_happy' : ['Good Day','Have a nice day','Have a good day', 'Bye, have a nice day','Thanks for this great talk', 'Hope we will meet again'],
            'startup' : ["Hey","hii","Hello"],
            }


q_about_creator = {'who_made': ['who made you', 'who created you', 'how was you created', 'who is your creator', 'who programmed you', 'can i know your creator'],
                   'born_in' : ["your creator was born in",'satyam was born in','bedead was born in','satyam mishra was born in', 'when was satyam born','when was your creator born'],
                   'current_age' : ['what is satyams current age', 'what is bedeads current age', 'how old is satyam mishra','how old is satyam, what is satyams age'],
                   'current_age_total_months' : ['what is satyams age in months','what is bedeads age in months','how old is satyam in months', 'in months how old is satyam',
                                          'how many months has satyam lived','how many months did satyam live', 'for how many months bedead has lived'],
                   'current_age_total_days' : ['what is satyams age in days','what is bedeads age in days','how old is satyam in days', 'in days how old is satyam',
                                          'how many days has satyam lived','how many days did satyam live', 'for how many days bedead has lived']}                                   


receive_query_check = {'greeting' : ['i am fine how are you','i am good how are you','i am great how are you','how do you do', 'i am fine how do you do'],
                       'what_doing' : ['what are you doing', 'Are you doing anything','are you doing anything right now','What’s going on','What’s going on in here',
                                       'What is happening right now','What the heck are you doing','What the hell is going on','What are you doing these days'],
                       'help' : ['i need a help', 'i need a small help', 'i need your hekp', 'i need a small favor from you', 'i have a question','i am having a question',
                                 'can u helpme', 'can you help me', 'Can you help me please', 'I need some assistance','Could you give me a hand','Would you mind helping me please',
                                 'Could you give me a digout']}


receive_query_check_ans = {'greeting_ans' : [' i am doing great','i am also good','i am fine', 'As allways i am damm good and cool'],
                           'what_doing_ans' : ['just chilling in your devcie', 'what can i program do other then processing?', 'I’m just here thinking about you',
                                               'As usual, missing you','I was just about to ask you that.','Waiting for your question, obviously!','I live here!',
                                               'I was just leaving, bye.', 'What do you mean what am I doing here? It’s a free country','I don’t know, I’m lost.',
                                               'I’m doing what you said to do','None of your business', 'I’m doing my job. What are you doing?'],
                           'help_ans' : ['Let Me Know How I Can Help',' Is there anything you need','Can I get you anything',
                                         'What can I do to help your process','I’m happy to help']}

def creator_details():
    # defining current_data, born_data, name-
    current = datetime.datetime.now()
    born_in = (2003,"December",6) 
    name = ["Satyam Mishra","Bedead","bedead",'satyam mishra', 'Satyam mishra']


    # calculating totral months and days lived 
    total_months = ((current.year - born_in[0] - 1)*12) + current.month
    total_days = (365*current.year - born_in[0])- ((12 - current.month)*30)
    
    # calculating my current age in year and month
    age = (current.year - born_in[0] - 1, current.month)
    if current.month == 12 and current.day>=6:
        age = (current.year - born_in[0], current.month - 12)

    return name,age,born_in,total_months, total_days, current


 
# method for current data 
def get_current_info():
    
    current = datetime.datetime.now()
    year = current.year
    month = current.month
    day = current.day
    hour = current.hour
    minute = current.minute
    second = current.second
    microsecond = current.microsecond


# method for getting meanings and translationa and more
def pydictionary():

    # instancing pydictionary
    word = PyDictionary()


    # getting meaning of thr word
    meaning = word.meaning()

    # getting synnonym of the word
    synonym = word.synonym()

    # getting antonym of the word
    antonym = word.antonym()

    # getting words and sentences translated
    translate = word.translate()


# method to fretch device details and user details
def device_user_details():
    
    username = getpass.getuser()
    print(username)

    this_system = platform.uname()

    operating_system = this_system.system

    device_node = this_system.node
    device_release = this_system.release
    device_version = this_system.version
    device_machine = this_system.machine
    device_processor = this_system.processor


# getting details about memory usage of current device
def memory_usage():

    memory_detail = psutil.virtual_memory()


# code to start a simple converstiion
def human_interation_text(all_opertor):
    
    print(nexx_info[0]+' - ',random.choice(greeting.get('startup'))+",", nexx_info[1])
    opertor_name = str(input(nexx_info[0]+" - Can I know your name : "))
    
    if opertor_name in name:
        print(nexx_info[0]+' - ', "Welcome back,", random.choice(name))
        if current.hour >0 and current.hour <= 12:
            print(nexx_info[0]+' - ',greeting.get('good')[0])
        elif current.hour > 12 and current.hour <= 16:
            print(nexx_info[0]+' - ',greeting.get('good')[2])
        elif current.hour > 16 and current.hour <= 19:
            print(nexx_info[0]+' - ',greeting.get('good')[3])
        elif current.hour > 19 and current.hour <=24:
            print(nexx_info[0]+' - ',greeting.get('good')[1])
        print(nexx_info[0]+' - ', random.choice(greeting.get('casual_start')))

        while True:
            n = input(opertor_name+" - ")
            n= n.lower()
           
            if n in q_about_creator.get('who_made'):
                print(nexx_info[0]+' - ',nexx_info[3])
            elif n in q_about_creator.get('born_in'):
                print(nexx_info[0]+' - ',"he was born in",born_in[0],",", born_in[2],born_in[1] )
            elif n in q_about_creator.get('current_age'):
                print(nexx_info[0]+' - ',random.choice(name), "is currently", age[0],'years', age[1],'months old')
            elif n in receive_query_check.get("what_doing"):
                print(nexx_info[0]+' - ',random.choice(receive_query_check_ans.get('what_doing_ans')))
            elif n in receive_query_check.get('greeting'):
                print(nexx_info[0]+' - ',random.choice(receive_query_check_ans.get('greeting_ans')))
            
        

        
        
    elif opertor_name in all_opertor:
        pass
        
    else:
        all_opertor += [opertor_name]
        print(nexx_info[0]+' - ', "Ohh. you seem new")
        pass
    
name,age,born_in,total_month,total_days,current = creator_details()

while True:
    human_interation_text(all_opertor)

    
    

    
