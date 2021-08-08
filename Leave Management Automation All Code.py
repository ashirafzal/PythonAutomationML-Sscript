#!/usr/bin/env python
# coding: utf-8

# In[95]:


import mysql.connector
        
def main():
    maincursor = mydb.cursor()
    maincursor.execute("SELECT * FROM casual_leave_application where status IS NULL ORDER BY leave_id ASC");
    
    for i in maincursor:
        
        if i[7] <= 5:
            Level1(i)
        elif i[7] >= 5 and i[7] <= 10:
            Level2(i)
        elif i[7] >= 10 and i[7] <= 15:
            Level3(i)
        elif i[7] >= 15 and i[7] <= 20:
            Level4(i)
        elif i[7] >= 20 and i[7] <= 25:
            Level5(i)
        elif i[7] >= 25 and i[7] <= 30:
            Level6(i)
        else:
            Level7(i)

        
def Level1(i):
    
    mydb = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
    
    status = []
    
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM ml_casual_leave_application_model where previous_leaves >=0 and previous_leaves <=5");

    for i1 in mycursor.fetchall():
        
        if i1[10] == 1:
            status.append(1)
        else:
            status.append(0)
    
    positive = status.count(1)
    negative = status.count(0)
    
    leave_id = str(i[0])
    pers_no = str(i[1])
    first_name = str(i[2])
    designation = str(i[3])
    start_date = str(i[4])
    end_date = str(i[5])
    reason = str(i[6])
    previous_leaves = str(i[7])
    signature = str(i[8])
    date_of_application = str(i[9])
    
    if positive > negative:
        mycursor.execute('INSERT INTO suggestions (leave_id,pers_no,first_name,designation,start_date,end_date,reason,previous_leaves,signature,date_of_application,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)' , (leave_id,pers_no,first_name,designation,start_date,end_date,reason,previous_leaves,signature,date_of_application,'1','0') );
    else:
        mycursor.execute('INSERT INTO suggestions (leave_id,pers_no,first_name,designation,start_date,end_date,reason,previous_leaves,signature,date_of_application,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)' , (leave_id,pers_no,first_name,designation,start_date,end_date,reason,previous_leaves,signature,date_of_application,'0','0') );
    
    mydb.commit()
    mydb.close()
    
def Level2(i):
    
    mydb = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
    
    status = []
    
    mycursor = mydb.cursor()
    
    if 'sick' in i[6].lower():
        mycursor.execute("SELECT * FROM ml_casual_leave_application_model where previous_leaves >=5 and previous_leaves <=10 and reason = 'Sick Leave' ");
    elif 'trip' in i[6].lower():
        mycursor.execute("SELECT * FROM ml_casual_leave_application_model where previous_leaves >=5 and previous_leaves <=10 and reason = 'trip' ");
    elif 'personal commitment' in i[6].lower():
        mycursor.execute("SELECT * FROM ml_casual_leave_application_model where previous_leaves >=5 and previous_leaves <=10 and reason = 'Personal Commitment' ");
    elif 'personal issues' in i[6].lower():
        mycursor.execute("SELECT * FROM ml_casual_leave_application_model where previous_leaves >=5 and previous_leaves <=10 and reason = 'Personal Issues' ");
    elif 'hospitalized' in i[6].lower():
        mycursor.execute("SELECT * FROM ml_casual_leave_application_model where previous_leaves >=5 and previous_leaves <=10 and reason = 'hospitalized' ");
        
    for i1 in mycursor.fetchall():
        
        if i1[10] == 1:
            status.append(1)
        else:
            status.append(0)
    
    positive = status.count(1)
    negative = status.count(0)
    
    leave_id = str(i[0])
    pers_no = str(i[1])
    first_name = str(i[2])
    designation = str(i[3])
    start_date = str(i[4])
    end_date = str(i[5])
    reason = str(i[6])
    previous_leaves = str(i[7])
    signature = str(i[8])
    date_of_application = str(i[9])
    
    if positive > negative:
        mycursor.execute('INSERT INTO suggestions (leave_id,pers_no,first_name,designation,start_date,end_date,reason,previous_leaves,signature,date_of_application,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)' , (leave_id,pers_no,first_name,designation,start_date,end_date,reason,previous_leaves,signature,date_of_application,'1','0') );
    else:
        mycursor.execute('INSERT INTO suggestions (leave_id,pers_no,first_name,designation,start_date,end_date,reason,previous_leaves,signature,date_of_application,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)' , (leave_id,pers_no,first_name,designation,start_date,end_date,reason,previous_leaves,signature,date_of_application,'0','0') );
    
    mydb.commit()
    mydb.close()
    
def Level3(i):
    
    mydb = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
    
    status = []
    
    mycursor = mydb.cursor()
    
    if 'sick' in i[6].lower():
        mycursor.execute("SELECT * FROM ml_casual_leave_application_model where previous_leaves >=10 and previous_leaves <=15 and reason = 'Sick Leave' ");
    elif 'trip' in i[6].lower():
        mycursor.execute("SELECT * FROM ml_casual_leave_application_model where previous_leaves >=10 and previous_leaves <=15 and reason = 'trip' ");
    elif 'personal commitment' in i[6].lower():
        mycursor.execute("SELECT * FROM ml_casual_leave_application_model where previous_leaves >=10 and previous_leaves <=15 and reason = 'Personal Commitment' ");
    elif 'personal issues' in i[6].lower():
        mycursor.execute("SELECT * FROM ml_casual_leave_application_model where previous_leaves >=10 and previous_leaves <=15 and reason = 'Personal Issues' ");
    elif 'hospitalized' in i[6].lower():
        mycursor.execute("SELECT * FROM ml_casual_leave_application_model where previous_leaves >=10 and previous_leaves <=15 and reason = 'hospitalized' ");
        
    for i1 in mycursor.fetchall():
        
        if i1[10] == 1:
            status.append(1)
        else:
            status.append(0)
    
    positive = status.count(1)
    negative = status.count(0)
    
    leave_id = str(i[0])
    pers_no = str(i[1])
    first_name = str(i[2])
    designation = str(i[3])
    start_date = str(i[4])
    end_date = str(i[5])
    reason = str(i[6])
    previous_leaves = str(i[7])
    signature = str(i[8])
    date_of_application = str(i[9])
    
    if positive > negative:
        mycursor.execute('INSERT INTO suggestions (leave_id,pers_no,first_name,designation,start_date,end_date,reason,previous_leaves,signature,date_of_application,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)' , (leave_id,pers_no,first_name,designation,start_date,end_date,reason,previous_leaves,signature,date_of_application,'1','0') );
    else:
        mycursor.execute('INSERT INTO suggestions (leave_id,pers_no,first_name,designation,start_date,end_date,reason,previous_leaves,signature,date_of_application,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)' , (leave_id,pers_no,first_name,designation,start_date,end_date,reason,previous_leaves,signature,date_of_application,'0','0') );
    
    mydb.commit()
    mydb.close()
    
def Level4(i):
    
    mydb = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
    
    status = []
    
    mycursor = mydb.cursor()
    
    if 'sick' in i[6].lower():
        mycursor.execute("SELECT * FROM ml_casual_leave_application_model where previous_leaves >=15 and previous_leaves <=20 and reason = 'Sick Leave' ");
    elif 'trip' in i[6].lower():
        mycursor.execute("SELECT * FROM ml_casual_leave_application_model where previous_leaves >=15 and previous_leaves <=20 and reason = 'trip' ");
    elif 'personal commitment' in i[6].lower():
        mycursor.execute("SELECT * FROM ml_casual_leave_application_model where previous_leaves >=15 and previous_leaves <=20 and reason = 'Personal Commitment' ");
    elif 'personal issues' in i[6].lower():
        mycursor.execute("SELECT * FROM ml_casual_leave_application_model where previous_leaves >=15 and previous_leaves <=20 and reason = 'Personal Issues' ");
    elif 'hospitalized' in i[6].lower():
        mycursor.execute("SELECT * FROM ml_casual_leave_application_model where previous_leaves >=15 and previous_leaves <=20 and reason = 'hospitalized' ");
        
    for i1 in mycursor.fetchall():
        
        if i1[10] == 1:
            status.append(1)
        else:
            status.append(0)
    
    positive = status.count(1)
    negative = status.count(0)
    
    leave_id = str(i[0])
    pers_no = str(i[1])
    first_name = str(i[2])
    designation = str(i[3])
    start_date = str(i[4])
    end_date = str(i[5])
    reason = str(i[6])
    previous_leaves = str(i[7])
    signature = str(i[8])
    date_of_application = str(i[9])
    
    if positive > negative:
        mycursor.execute('INSERT INTO suggestions (leave_id,pers_no,first_name,designation,start_date,end_date,reason,previous_leaves,signature,date_of_application,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)' , (leave_id,pers_no,first_name,designation,start_date,end_date,reason,previous_leaves,signature,date_of_application,'1','0') );
    else:
        mycursor.execute('INSERT INTO suggestions (leave_id,pers_no,first_name,designation,start_date,end_date,reason,previous_leaves,signature,date_of_application,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)' , (leave_id,pers_no,first_name,designation,start_date,end_date,reason,previous_leaves,signature,date_of_application,'0','0') );
    
    mydb.commit()
    mydb.close()
    
def Level5(i):
    
    mydb = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
    
    status = []
    
    mycursor = mydb.cursor()
    
    if 'sick' in i[6].lower():
        mycursor.execute("SELECT * FROM ml_casual_leave_application_model where previous_leaves >=20 and previous_leaves <=25 and reason = 'Sick Leave' ");
    elif 'trip' in i[6].lower():
        mycursor.execute("SELECT * FROM ml_casual_leave_application_model where previous_leaves >=20 and previous_leaves <=25 and reason = 'trip' ");
    elif 'personal commitment' in i[6].lower():
        mycursor.execute("SELECT * FROM ml_casual_leave_application_model where previous_leaves >=20 and previous_leaves <=25 and reason = 'Personal Commitment' ");
    elif 'personal issues' in i[6].lower():
        mycursor.execute("SELECT * FROM ml_casual_leave_application_model where previous_leaves >=20 and previous_leaves <=25 and reason = 'Personal Issues' ");
    elif 'hospitalized' in i[6].lower():
        mycursor.execute("SELECT * FROM ml_casual_leave_application_model where previous_leaves >=20 and previous_leaves <=25 and reason = 'hospitalized' ");
        
    for i1 in mycursor.fetchall():
        
        if i1[10] == 1:
            status.append(1)
        else:
            status.append(0)
    
    positive = status.count(1)
    negative = status.count(0)
    
    leave_id = str(i[0])
    pers_no = str(i[1])
    first_name = str(i[2])
    designation = str(i[3])
    start_date = str(i[4])
    end_date = str(i[5])
    reason = str(i[6])
    previous_leaves = str(i[7])
    signature = str(i[8])
    date_of_application = str(i[9])
    
    if positive > negative:
        mycursor.execute('INSERT INTO suggestions (leave_id,pers_no,first_name,designation,start_date,end_date,reason,previous_leaves,signature,date_of_application,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)' , (leave_id,pers_no,first_name,designation,start_date,end_date,reason,previous_leaves,signature,date_of_application,'1','0') );
    else:
        mycursor.execute('INSERT INTO suggestions (leave_id,pers_no,first_name,designation,start_date,end_date,reason,previous_leaves,signature,date_of_application,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)' , (leave_id,pers_no,first_name,designation,start_date,end_date,reason,previous_leaves,signature,date_of_application,'0','0') );

    mydb.commit()
    mydb.close()
    
def Level6(i):
    
    mydb = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
    
    status = []
    
    mycursor = mydb.cursor()
    
    if 'sick' in i[6].lower():
        mycursor.execute("SELECT * FROM ml_casual_leave_application_model where previous_leaves >=25 and previous_leaves <=30 and reason = 'Sick Leave' ");
    elif 'trip' in i[6].lower():
        mycursor.execute("SELECT * FROM ml_casual_leave_application_model where previous_leaves >=25 and previous_leaves <=30 and reason = 'trip' ");
    elif 'personal commitment' in i[6].lower():
        mycursor.execute("SELECT * FROM ml_casual_leave_application_model where previous_leaves >=25 and previous_leaves <=30 and reason = 'Personal Commitment' ");
    elif 'personal issues' in i[6].lower():
        mycursor.execute("SELECT * FROM ml_casual_leave_application_model where previous_leaves >=25 and previous_leaves <=30 and reason = 'Personal Issues' ");
    elif 'hospitalized' in i[6].lower():
        mycursor.execute("SELECT * FROM ml_casual_leave_application_model where previous_leaves >=25 and previous_leaves <=30 and reason = 'hospitalized' ");
        
    for i1 in mycursor.fetchall():
        
        if i1[10] == 1:
            status.append(1)
        else:
            status.append(0)
    
    positive = status.count(1)
    negative = status.count(0)
    
    leave_id = str(i[0])
    pers_no = str(i[1])
    first_name = str(i[2])
    designation = str(i[3])
    start_date = str(i[4])
    end_date = str(i[5])
    reason = str(i[6])
    previous_leaves = str(i[7])
    signature = str(i[8])
    date_of_application = str(i[9])
    
    if positive > negative:
        mycursor.execute('INSERT INTO suggestions (leave_id,pers_no,first_name,designation,start_date,end_date,reason,previous_leaves,signature,date_of_application,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)' , (leave_id,pers_no,first_name,designation,start_date,end_date,reason,previous_leaves,signature,date_of_application,'1','0') );
    else:
        mycursor.execute('INSERT INTO suggestions (leave_id,pers_no,first_name,designation,start_date,end_date,reason,previous_leaves,signature,date_of_application,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)' , (leave_id,pers_no,first_name,designation,start_date,end_date,reason,previous_leaves,signature,date_of_application,'0','0') );
    
    mydb.commit()
    mydb.close()
    
def Level7(i):
    
    mydb = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
    
    status = []
    
    mycursor = mydb.cursor()
    
    if 'sick' in i[6].lower():
        mycursor.execute("SELECT * FROM ml_casual_leave_application_model where previous_leaves >=30 and reason = 'Sick Leave' ");
    elif 'trip' in i[6].lower():
        mycursor.execute("SELECT * FROM ml_casual_leave_application_model where previous_leaves >=30 and reason = 'trip' ");
    elif 'personal commitment' in i[6].lower():
        mycursor.execute("SELECT * FROM ml_casual_leave_application_model where previous_leaves >=30 and reason = 'Personal Commitment' ");
    elif 'personal issues' in i[6].lower():
        mycursor.execute("SELECT * FROM ml_casual_leave_application_model where previous_leaves >=30 and reason = 'Personal Issues' ");
    elif 'hospitalized' in i[6].lower():
        mycursor.execute("SELECT * FROM ml_casual_leave_application_model where previous_leaves >=30 and reason = 'hospitalized' ");
        
    for i1 in mycursor.fetchall():
        
        if i1[10] == 1:
            status.append(1)
        else:
            status.append(0)
    
    positive = status.count(1)
    negative = status.count(0)
    
    leave_id = str(i[0])
    pers_no = str(i[1])
    first_name = str(i[2])
    designation = str(i[3])
    start_date = str(i[4])
    end_date = str(i[5])
    reason = str(i[6])
    previous_leaves = str(i[7])
    signature = str(i[8])
    date_of_application = str(i[9])
    
    if positive > negative:
        mycursor.execute('INSERT INTO suggestions (leave_id,pers_no,first_name,designation,start_date,end_date,reason,previous_leaves,signature,date_of_application,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)' , (leave_id,pers_no,first_name,designation,start_date,end_date,reason,previous_leaves,signature,date_of_application,'1','0') );
    else:
        mycursor.execute('INSERT INTO suggestions (leave_id,pers_no,first_name,designation,start_date,end_date,reason,previous_leaves,signature,date_of_application,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)' , (leave_id,pers_no,first_name,designation,start_date,end_date,reason,previous_leaves,signature,date_of_application,'0','0') );
    
    mydb.commit()
    mydb.close()
    
host_name = "localhost"
user_name = "root"
user_password = ""
db_name = "mi_model"

main()

print('\n','Done','\n')


# In[ ]:




