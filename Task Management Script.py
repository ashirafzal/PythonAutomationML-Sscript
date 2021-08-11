#!/usr/bin/env python
# coding: utf-8

# In[253]:


import mysql.connector
import pymysql
import pymysql.cursors
    
def level1(task_id,no_of_task):
    
    status = []
    
    mydb = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
    
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM ml_task_model where complexity_level = 'Entry' and duration >= 1 and duration <= 3 ORDER BY id ASC");
    
    for i1 in mycursor.fetchall():
        
        if i1[9] == 1:
            status.append(1)
        else:
            status.append(0)
    
    positive = status.count(1)
    negative = status.count(0)
    
    if positive > negative:
        
        pers_name = ''
        
        mydb3 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor3 = mydb3.cursor()
        query_string = "SELECT * FROM task_assigned WHERE task_id = '%s' and status = 'Pending' "
        cursor3.execute(query_string, (task_id,))
        
        remaining_task = []
        personid = 0
        
        for i2 in cursor3:
            personid = i2[1]
            remaining_task.append(i2[0])
        
        remaining_task_sum = sum(remaining_task)
        
        mydb3.commit()
        mydb3.close()
        
        mydb4 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor4 = mydb4.cursor()
        query_string = "SELECT * FROM employee WHERE pers_no = '%s' "
        cursor4.execute(query_string, (personid,))
        
        for i3 in cursor4:
            pers_name = i3[1]+' '+i3[2]
        
        mydb4.commit()
        mydb4.close()
        
        remaining_task_sum = str(remaining_task_sum)
        personid = str(personid)
        task_id = str(task_id)
        pers_name = str(pers_name)
        
        mydb5 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor5 = mydb5.cursor()
        
        cursor5.execute('INSERT INTO task_suggetions (pers_no,task_id,pers_name,remaining_task,reason,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s)' , (personid,task_id,pers_name,remaining_task_sum,'The probability task done in time is high','1','0') );
        
        mydb5.commit()
        mydb5.close()
        
    else:
        
        pers_name = ''
        
        mydb3 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor3 = mydb3.cursor()
        query_string = "SELECT * FROM task_assigned WHERE task_id = '%s' and status = 'Pending' "
        cursor3.execute(query_string, (task_id,))
        
        remaining_task = []
        personid = 0
        
        for i2 in cursor3:
            personid = i2[1]
            remaining_task.append(i2[0])
        
        remaining_task_sum = sum(remaining_task)
        
        mydb3.commit()
        mydb3.close()
        
        mydb4 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor4 = mydb4.cursor()
        query_string = "SELECT * FROM employee WHERE pers_no = '%s' "
        cursor4.execute(query_string, (personid,))
        
        for i3 in cursor4:
            pers_name = i3[1]+' '+i3[2]
        
        mydb4.commit()
        mydb4.close()
        
        remaining_task_sum = str(remaining_task_sum)
        personid = str(personid)
        task_id = str(task_id)
        pers_name = str(pers_name)
        
        mydb5 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor5 = mydb5.cursor()
        
        cursor5.execute('INSERT INTO task_suggetions (pers_no,task_id,pers_name,remaining_task,reason,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s)' , (personid,task_id,pers_name,remaining_task_sum,'The probability task done in time is high','0','0') );
        
        mydb5.commit()
        mydb5.close()
        
    mydb.commit()
    mydb.close()
    
def level2(task_id,no_of_task):
    
    status = []
    
    mydb = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
    
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM ml_task_model where complexity_level = 'Entry' and complexity_level = 'Intermediate' and duration >= 1 and duration <= 3 ORDER BY id ASC");
    
    for i1 in mycursor.fetchall():
        
        if i1[9] == 1:
            status.append(1)
        else:
            status.append(0)
    
    positive = status.count(1)
    negative = status.count(0)
    
    if positive > negative:
        pers_name = ''
        
        mydb3 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor3 = mydb3.cursor()
        query_string = "SELECT * FROM task_assigned WHERE task_id = '%s' and status = 'Pending' "
        cursor3.execute(query_string, (task_id,))
        
        remaining_task = []
        personid = 0
        
        for i2 in cursor3:
            personid = i2[1]
            remaining_task.append(i2[0])
        
        remaining_task_sum = sum(remaining_task)
        
        mydb3.commit()
        mydb3.close()
        
        mydb4 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor4 = mydb4.cursor()
        query_string = "SELECT * FROM employee WHERE pers_no = '%s' "
        cursor4.execute(query_string, (personid,))
        
        for i3 in cursor4:
            pers_name = i3[1]+' '+i3[2]
        
        mydb4.commit()
        mydb4.close()
        
        remaining_task_sum = str(remaining_task_sum)
        personid = str(personid)
        task_id = str(task_id)
        pers_name = str(pers_name)
        
        mydb5 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor5 = mydb5.cursor()
        
        cursor5.execute('INSERT INTO task_suggetions (pers_no,task_id,pers_name,remaining_task,reason,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s)' , (personid,task_id,pers_name,remaining_task_sum,'The probability task done in time is high','1','0') );
        
        mydb5.commit()
        mydb5.close()
    else:
        
        pers_name = ''
        
        mydb3 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor3 = mydb3.cursor()
        query_string = "SELECT * FROM task_assigned WHERE task_id = '%s' and status = 'Pending' "
        cursor3.execute(query_string, (task_id,))
        
        remaining_task = []
        personid = 0
        
        for i2 in cursor3:
            personid = i2[1]
            remaining_task.append(i2[0])
        
        remaining_task_sum = sum(remaining_task)
        
        mydb3.commit()
        mydb3.close()
        
        mydb4 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor4 = mydb4.cursor()
        query_string = "SELECT * FROM employee WHERE pers_no = '%s' "
        cursor4.execute(query_string, (personid,))
        
        for i3 in cursor4:
            pers_name = i3[1]+' '+i3[2]
        
        mydb4.commit()
        mydb4.close()
        
        remaining_task_sum = str(remaining_task_sum)
        personid = str(personid)
        task_id = str(task_id)
        pers_name = str(pers_name)
        
        mydb5 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor5 = mydb5.cursor()
        
        cursor5.execute('INSERT INTO task_suggetions (pers_no,task_id,pers_name,remaining_task,reason,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s)' , (personid,task_id,pers_name,remaining_task_sum,'The probability task done in time is high','0','0') );
        
        mydb5.commit()
        mydb5.close()
        
    
    mydb.commit()
    mydb.close()
    
def level3(task_id,no_of_task):
    
    status = []
    
    mydb = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
    
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM ml_task_model where complexity_level = 'Entry' and complexity_level = 'Intermediate' and complexity_level = 'Expert' and duration >= 1 and duration <= 3 ORDER BY id ASC");
    
    for i1 in mycursor.fetchall():
        
        if i1[9] == 1:
            status.append(1)
        else:
            status.append(0)
    
    positive = status.count(1)
    negative = status.count(0)
    
    if positive > negative:
        
        pers_name = ''
        
        mydb3 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor3 = mydb3.cursor()
        query_string = "SELECT * FROM task_assigned WHERE task_id = '%s' and status = 'Pending' "
        cursor3.execute(query_string, (task_id,))
        
        remaining_task = []
        personid = 0
        
        for i2 in cursor3:
            personid = i2[1]
            remaining_task.append(i2[0])
        
        remaining_task_sum = sum(remaining_task)
        
        mydb3.commit()
        mydb3.close()
        
        mydb4 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor4 = mydb4.cursor()
        query_string = "SELECT * FROM employee WHERE pers_no = '%s' "
        cursor4.execute(query_string, (personid,))
        
        for i3 in cursor4:
            pers_name = i3[1]+' '+i3[2]
            
        mydb4.commit()
        mydb4.close()
        
        remaining_task_sum = str(remaining_task_sum)
        personid = str(personid)
        task_id = str(task_id)
        pers_name = str(pers_name)
        
        mydb5 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor5 = mydb5.cursor()
        
        cursor5.execute('INSERT INTO task_suggetions (pers_no,task_id,pers_name,remaining_task,reason,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s)' , (personid,task_id,pers_name,remaining_task_sum,'The probability task done in time is high','1','0') );
        
        mydb5.commit()
        mydb5.close()
        
    else:
        
        pers_name = ''
        
        mydb3 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor3 = mydb3.cursor()
        query_string = "SELECT * FROM task_assigned WHERE task_id = '%s' and status = 'Pending' "
        cursor3.execute(query_string, (task_id,))
        
        remaining_task = []
        personid = 0
        
        for i2 in cursor3:
            personid = i2[1]
            remaining_task.append(i2[0])
        
        remaining_task_sum = sum(remaining_task)
        
        mydb3.commit()
        mydb3.close()
        
        mydb4 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor4 = mydb4.cursor()
        query_string = "SELECT * FROM employee WHERE pers_no = '%s' "
        cursor4.execute(query_string, (personid,))
        
        for i3 in cursor4:
            pers_name = i3[1]+' '+i3[2]
        
        mydb4.commit()
        mydb4.close()
        
        remaining_task_sum = str(remaining_task_sum)
        personid = str(personid)
        task_id = str(task_id)
        pers_name = str(pers_name)
        
        mydb5 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor5 = mydb5.cursor()
        
        cursor5.execute('INSERT INTO task_suggetions (pers_no,task_id,pers_name,remaining_task,reason,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s)' , (personid,task_id,pers_name,remaining_task_sum,'The probability task done in time is high','0','0') );
        
        mydb5.commit()
        mydb5.close()
    
    mydb.commit()
    mydb.close()
    
def level4(task_id,no_of_task):
    
    status = []
    
    mydb = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
    
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM ml_task_model where complexity_level = 'Entry' and duration >= 3 and duration <= 6 ORDER BY id ASC");
    
    for i1 in mycursor.fetchall():
        
        if i1[9] == 1:
            status.append(1)
        else:
            status.append(0)
    
    positive = status.count(1)
    negative = status.count(0)
    
    if positive > negative:
        
        pers_name = ''
        
        mydb3 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor3 = mydb3.cursor()
        query_string = "SELECT * FROM task_assigned WHERE task_id = '%s' and status = 'Pending' "
        cursor3.execute(query_string, (task_id,))
        
        remaining_task = []
        personid = 0
        
        for i2 in cursor3:
            personid = i2[1]
            remaining_task.append(i2[0])
        
        remaining_task_sum = sum(remaining_task)
        
        mydb3.commit()
        mydb3.close()
        
        mydb4 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor4 = mydb4.cursor()
        query_string = "SELECT * FROM employee WHERE pers_no = '%s' "
        cursor4.execute(query_string, (personid,))
        
        for i3 in cursor4:
            pers_name = i3[1]+' '+i3[2]
        
        mydb4.commit()
        mydb4.close()
        
        remaining_task_sum = str(remaining_task_sum)
        personid = str(personid)
        task_id = str(task_id)
        pers_name = str(pers_name)
        
        mydb5 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor5 = mydb5.cursor()
        
        cursor5.execute('INSERT INTO task_suggetions (pers_no,task_id,pers_name,remaining_task,reason,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s)' , (personid,task_id,pers_name,remaining_task_sum,'The probability task done in time is high','1','0') );
        
        mydb5.commit()
        mydb5.close()
        
    else:
        
        pers_name = ''
        
        mydb3 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor3 = mydb3.cursor()
        query_string = "SELECT * FROM task_assigned WHERE task_id = '%s' and status = 'Pending' "
        cursor3.execute(query_string, (task_id,))
        
        remaining_task = []
        personid = 0
        
        for i2 in cursor3:
            personid = i2[1]
            remaining_task.append(i2[0])
        
        remaining_task_sum = sum(remaining_task)
        
        mydb3.commit()
        mydb3.close()
        
        mydb4 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor4 = mydb4.cursor()
        query_string = "SELECT * FROM employee WHERE pers_no = '%s' "
        cursor4.execute(query_string, (personid,))
        
        for i3 in cursor4:
            pers_name = i3[1]+' '+i3[2]
        
        mydb4.commit()
        mydb4.close()
        
        remaining_task_sum = str(remaining_task_sum)
        personid = str(personid)
        task_id = str(task_id)
        pers_name = str(pers_name)
        
        mydb5 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor5 = mydb5.cursor()
        
        cursor5.execute('INSERT INTO task_suggetions (pers_no,task_id,pers_name,remaining_task,reason,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s)' , (personid,task_id,pers_name,remaining_task_sum,'The probability task done in time is high','0','0') );
        
        mydb5.commit()
        mydb5.close()
        
    mydb.commit()
    mydb.close()
    
def level5(task_id,no_of_task):
    
    status = []
    
    mydb = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
    
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM ml_task_model where complexity_level = 'Entry' and complexity_level = 'Intermediate' and duration >= 3 and duration <= 6 ORDER BY id ASC");
    
    for i1 in mycursor.fetchall():
        
        if i1[9] == 1:
            status.append(1)
        else:
            status.append(0)
    
    positive = status.count(1)
    negative = status.count(0)
    
    if positive > negative:
        
        pers_name = ''
        
        mydb3 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor3 = mydb3.cursor()
        query_string = "SELECT * FROM task_assigned WHERE task_id = '%s' and status = 'Pending' "
        cursor3.execute(query_string, (task_id,))
        
        remaining_task = []
        personid = 0
        
        for i2 in cursor3:
            personid = i2[1]
            remaining_task.append(i2[0])
        
        remaining_task_sum = sum(remaining_task)
        
        mydb3.commit()
        mydb3.close()
        
        mydb4 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor4 = mydb4.cursor()
        query_string = "SELECT * FROM employee WHERE pers_no = '%s' "
        cursor4.execute(query_string, (personid,))
        
        for i3 in cursor4:
            pers_name = i3[1]+' '+i3[2]
        
        mydb4.commit()
        mydb4.close()
        
        remaining_task_sum = str(remaining_task_sum)
        personid = str(personid)
        task_id = str(task_id)
        pers_name = str(pers_name)
        
        mydb5 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor5 = mydb5.cursor()
        
        cursor5.execute('INSERT INTO task_suggetions (pers_no,task_id,pers_name,remaining_task,reason,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s)' , (personid,task_id,pers_name,remaining_task_sum,'The probability task done in time is high','1','0') );
        
        mydb5.commit()
        mydb5.close()
        
    else:
        print('not allow')
    
    mydb.commit()
    mydb.close()
    
def level6(task_id,no_of_task):
    
    status = []
    
    mydb = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
    
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM ml_task_model where complexity_level = 'Entry' and complexity_level = 'Intermediate' and complexity_level = 'Expert' and duration >= 3 and duration <= 6 ORDER BY id ASC");
    
    for i1 in mycursor.fetchall():
        
        if i1[9] == 1:
            status.append(1)
        else:
            status.append(0)
    
    positive = status.count(1)
    negative = status.count(0)
    
    if positive > negative:
        
        pers_name = ''
        
        mydb3 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor3 = mydb3.cursor()
        query_string = "SELECT * FROM task_assigned WHERE task_id = '%s' and status = 'Pending' "
        cursor3.execute(query_string, (task_id,))
        
        remaining_task = []
        personid = 0
        
        for i2 in cursor3:
            personid = i2[1]
            remaining_task.append(i2[0])
        
        remaining_task_sum = sum(remaining_task)
        
        mydb3.commit()
        mydb3.close()
        
        mydb4 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor4 = mydb4.cursor()
        query_string = "SELECT * FROM employee WHERE pers_no = '%s' "
        cursor4.execute(query_string, (personid,))
        
        for i3 in cursor4:
            pers_name = i3[1]+' '+i3[2]
        
        mydb4.commit()
        mydb4.close()
        
        remaining_task_sum = str(remaining_task_sum)
        personid = str(personid)
        task_id = str(task_id)
        pers_name = str(pers_name)
        
        mydb5 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor5 = mydb5.cursor()
        
        cursor5.execute('INSERT INTO task_suggetions (pers_no,task_id,pers_name,remaining_task,reason,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s)' , (personid,task_id,pers_name,remaining_task_sum,'The probability task done in time is high','1','0') );
        
        mydb5.commit()
        mydb5.close()
        
    else:
        
        pers_name = ''
        
        mydb3 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor3 = mydb3.cursor()
        query_string = "SELECT * FROM task_assigned WHERE task_id = '%s' and status = 'Pending' "
        cursor3.execute(query_string, (task_id,))
        
        remaining_task = []
        personid = 0
        
        for i2 in cursor3:
            personid = i2[1]
            remaining_task.append(i2[0])
        
        remaining_task_sum = sum(remaining_task)
        
        mydb3.commit()
        mydb3.close()
        
        mydb4 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor4 = mydb4.cursor()
        query_string = "SELECT * FROM employee WHERE pers_no = '%s' "
        cursor4.execute(query_string, (personid,))
        
        for i3 in cursor4:
            pers_name = i3[1]+' '+i3[2]
        
        mydb4.commit()
        mydb4.close()
        
        remaining_task_sum = str(remaining_task_sum)
        personid = str(personid)
        task_id = str(task_id)
        pers_name = str(pers_name)
        
        mydb5 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor5 = mydb5.cursor()
        
        cursor5.execute('INSERT INTO task_suggetions (pers_no,task_id,pers_name,remaining_task,reason,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s)' , (personid,task_id,pers_name,remaining_task_sum,'The probability task done in time is high','0','0') );
        
        mydb5.commit()
        mydb5.close()
        
    
    mydb.commit()
    mydb.close()
    
def level7(task_id,no_of_task):
    
    status = []
    
    mydb = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
    
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM ml_task_model where complexity_level = 'Entry' and duration >= 6 and duration <= 9 ORDER BY id ASC");
    
    for i1 in mycursor.fetchall():
        
        if i1[9] == 1:
            status.append(1)
        else:
            status.append(0)
    
    positive = status.count(1)
    negative = status.count(0)
    
    if positive > negative:
        
        pers_name = ''
        
        mydb3 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor3 = mydb3.cursor()
        query_string = "SELECT * FROM task_assigned WHERE task_id = '%s' and status = 'Pending' "
        cursor3.execute(query_string, (task_id,))
        
        remaining_task = []
        personid = 0
        
        for i2 in cursor3:
            personid = i2[1]
            remaining_task.append(i2[0])
        
        remaining_task_sum = sum(remaining_task)
        
        mydb3.commit()
        mydb3.close()
        
        mydb4 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor4 = mydb4.cursor()
        query_string = "SELECT * FROM employee WHERE pers_no = '%s' "
        cursor4.execute(query_string, (personid,))
        
        for i3 in cursor4:
            pers_name = i3[1]+' '+i3[2]
        
        mydb4.commit()
        mydb4.close()
        
        remaining_task_sum = str(remaining_task_sum)
        personid = str(personid)
        task_id = str(task_id)
        pers_name = str(pers_name)
        
        mydb5 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor5 = mydb5.cursor()
        
        cursor5.execute('INSERT INTO task_suggetions (pers_no,task_id,pers_name,remaining_task,reason,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s)' , (personid,task_id,pers_name,remaining_task_sum,'The probability task done in time is high','1','0') );
        
        mydb5.commit()
        mydb5.close()
        
    else:
        
        pers_name = ''
        
        mydb3 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor3 = mydb3.cursor()
        query_string = "SELECT * FROM task_assigned WHERE task_id = '%s' and status = 'Pending' "
        cursor3.execute(query_string, (task_id,))
        
        remaining_task = []
        personid = 0
        
        for i2 in cursor3:
            personid = i2[1]
            remaining_task.append(i2[0])
        
        remaining_task_sum = sum(remaining_task)
        
        mydb3.commit()
        mydb3.close()
        
        mydb4 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor4 = mydb4.cursor()
        query_string = "SELECT * FROM employee WHERE pers_no = '%s' "
        cursor4.execute(query_string, (personid,))
        
        for i3 in cursor4:
            pers_name = i3[1]+' '+i3[2]
        
        mydb4.commit()
        mydb4.close()
        
        remaining_task_sum = str(remaining_task_sum)
        personid = str(personid)
        task_id = str(task_id)
        pers_name = str(pers_name)
        
        mydb5 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor5 = mydb5.cursor()
        
        cursor5.execute('INSERT INTO task_suggetions (pers_no,task_id,pers_name,remaining_task,reason,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s)' , (personid,task_id,pers_name,remaining_task_sum,'The probability task done in time is high','0','0') );
        
        mydb5.commit()
        mydb5.close()
        
    
    mydb.commit()
    mydb.close()
    
def level8(task_id,no_of_task):
    
    status = []
    
    mydb = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
    
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM ml_task_model where complexity_level = 'Entry' and complexity_level = 'Intermediate' and duration >= 6 and duration <= 9 ORDER BY id ASC");
    
    for i1 in mycursor.fetchall():
        
        if i1[9] == 1:
            status.append(1)
        else:
            status.append(0)
    
    positive = status.count(1)
    negative = status.count(0)
    
    if positive > negative:
        
        pers_name = ''
        
        mydb3 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor3 = mydb3.cursor()
        query_string = "SELECT * FROM task_assigned WHERE task_id = '%s' and status = 'Pending' "
        cursor3.execute(query_string, (task_id,))
        
        remaining_task = []
        personid = 0
        
        for i2 in cursor3:
            personid = i2[1]
            remaining_task.append(i2[0])
        
        remaining_task_sum = sum(remaining_task)
        
        mydb3.commit()
        mydb3.close()
        
        mydb4 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor4 = mydb4.cursor()
        query_string = "SELECT * FROM employee WHERE pers_no = '%s' "
        cursor4.execute(query_string, (personid,))
        
        for i3 in cursor4:
            pers_name = i3[1]+' '+i3[2]
        
        mydb4.commit()
        mydb4.close()
        
        remaining_task_sum = str(remaining_task_sum)
        personid = str(personid)
        task_id = str(task_id)
        pers_name = str(pers_name)
        
        mydb5 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor5 = mydb5.cursor()
        
        cursor5.execute('INSERT INTO task_suggetions (pers_no,task_id,pers_name,remaining_task,reason,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s)' , (personid,task_id,pers_name,remaining_task_sum,'The probability task done in time is high','1','0') );
        
        mydb5.commit()
        mydb5.close()
        
    else:
        
        pers_name = ''
        
        mydb3 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor3 = mydb3.cursor()
        query_string = "SELECT * FROM task_assigned WHERE task_id = '%s' and status = 'Pending' "
        cursor3.execute(query_string, (task_id,))
        
        remaining_task = []
        personid = 0
        
        for i2 in cursor3:
            personid = i2[1]
            remaining_task.append(i2[0])
        
        remaining_task_sum = sum(remaining_task)
        
        mydb3.commit()
        mydb3.close()
        
        mydb4 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor4 = mydb4.cursor()
        query_string = "SELECT * FROM employee WHERE pers_no = '%s' "
        cursor4.execute(query_string, (personid,))
        
        for i3 in cursor4:
            pers_name = i3[1]+' '+i3[2]
        
        mydb4.commit()
        mydb4.close()
        
        remaining_task_sum = str(remaining_task_sum)
        personid = str(personid)
        task_id = str(task_id)
        pers_name = str(pers_name)
        
        mydb5 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor5 = mydb5.cursor()
        
        cursor5.execute('INSERT INTO task_suggetions (pers_no,task_id,pers_name,remaining_task,reason,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s)' , (personid,task_id,pers_name,remaining_task_sum,'The probability task done in time is high','0','0') );
        
        mydb5.commit()
        mydb5.close()
        
    mydb.commit()
    mydb.close()
    
def level9(task_id,no_of_task):
    
    status = []
    
    mydb = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
    
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM ml_task_model where complexity_level = 'Entry' and complexity_level = 'Intermediate' and complexity_level = 'Expert' and duration >= 6 and duration <= 9 ORDER BY id ASC");
    
    for i1 in mycursor.fetchall():
        
        if i1[9] == 1:
            status.append(1)
        else:
            status.append(0)
    
    positive = status.count(1)
    negative = status.count(0)
    
    if positive > negative:
        
        pers_name = ''
        
        mydb3 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor3 = mydb3.cursor()
        query_string = "SELECT * FROM task_assigned WHERE task_id = '%s' and status = 'Pending' "
        cursor3.execute(query_string, (task_id,))
        
        remaining_task = []
        personid = 0
        
        for i2 in cursor3:
            personid = i2[1]
            remaining_task.append(i2[0])
        
        remaining_task_sum = sum(remaining_task)
        
        mydb3.commit()
        mydb3.close()
        
        mydb4 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor4 = mydb4.cursor()
        query_string = "SELECT * FROM employee WHERE pers_no = '%s' "
        cursor4.execute(query_string, (personid,))
        
        for i3 in cursor4:
            pers_name = i3[1]+' '+i3[2]
        
        mydb4.commit()
        mydb4.close()
        
        remaining_task_sum = str(remaining_task_sum)
        personid = str(personid)
        task_id = str(task_id)
        pers_name = str(pers_name)
        
        mydb5 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor5 = mydb5.cursor()
        
        cursor5.execute('INSERT INTO task_suggetions (pers_no,task_id,pers_name,remaining_task,reason,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s)' , (personid,task_id,pers_name,remaining_task_sum,'The probability task done in time is high','1','0') );
        
        mydb5.commit()
        mydb5.close()
        
    else:
        
        pers_name = ''
        
        mydb3 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor3 = mydb3.cursor()
        query_string = "SELECT * FROM task_assigned WHERE task_id = '%s' and status = 'Pending' "
        cursor3.execute(query_string, (task_id,))
        
        remaining_task = []
        personid = 0
        
        for i2 in cursor3:
            personid = i2[1]
            remaining_task.append(i2[0])
        
        remaining_task_sum = sum(remaining_task)
        
        mydb3.commit()
        mydb3.close()
        
        mydb4 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor4 = mydb4.cursor()
        query_string = "SELECT * FROM employee WHERE pers_no = '%s' "
        cursor4.execute(query_string, (personid,))
        
        for i3 in cursor4:
            pers_name = i3[1]+' '+i3[2]
        
        mydb4.commit()
        mydb4.close()
        
        remaining_task_sum = str(remaining_task_sum)
        personid = str(personid)
        task_id = str(task_id)
        pers_name = str(pers_name)
        
        mydb5 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor5 = mydb5.cursor()
        
        cursor5.execute('INSERT INTO task_suggetions (pers_no,task_id,pers_name,remaining_task,reason,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s)' , (personid,task_id,pers_name,remaining_task_sum,'The probability task done in time is high','0','0') );
        
        mydb5.commit()
        mydb5.close()
    
    mydb.commit()
    mydb.close()
    
def level10(task_id,no_of_task):
    
    status = []
    
    mydb = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
    
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM ml_task_model where complexity_level = 'Entry' and duration >= 9 and duration <= 12 ORDER BY id ASC");
    
    for i1 in mycursor.fetchall():
        
        if i1[9] == 1:
            status.append(1)
        else:
            status.append(0)
    
    positive = status.count(1)
    negative = status.count(0)
    
    if positive > negative:
        
        pers_name = ''
        
        mydb3 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor3 = mydb3.cursor()
        query_string = "SELECT * FROM task_assigned WHERE task_id = '%s' and status = 'Pending' "
        cursor3.execute(query_string, (task_id,))
        
        remaining_task = []
        personid = 0
        
        for i2 in cursor3:
            personid = i2[1]
            remaining_task.append(i2[0])
        
        remaining_task_sum = sum(remaining_task)
        
        mydb3.commit()
        mydb3.close()
        
        mydb4 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor4 = mydb4.cursor()
        query_string = "SELECT * FROM employee WHERE pers_no = '%s' "
        cursor4.execute(query_string, (personid,))
        
        for i3 in cursor4:
            pers_name = i3[1]+' '+i3[2]
        
        mydb4.commit()
        mydb4.close()
        
        remaining_task_sum = str(remaining_task_sum)
        personid = str(personid)
        task_id = str(task_id)
        pers_name = str(pers_name)
        
        mydb5 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor5 = mydb5.cursor()
        
        cursor5.execute('INSERT INTO task_suggetions (pers_no,task_id,pers_name,remaining_task,reason,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s)' , (personid,task_id,pers_name,remaining_task_sum,'The probability task done in time is high','1','0') );
        
        mydb5.commit()
        mydb5.close()
        
    else:
        
        pers_name = ''
        
        mydb3 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor3 = mydb3.cursor()
        query_string = "SELECT * FROM task_assigned WHERE task_id = '%s' and status = 'Pending' "
        cursor3.execute(query_string, (task_id,))
        
        remaining_task = []
        personid = 0
        
        for i2 in cursor3:
            personid = i2[1]
            remaining_task.append(i2[0])
        
        remaining_task_sum = sum(remaining_task)
        
        mydb3.commit()
        mydb3.close()
        
        mydb4 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor4 = mydb4.cursor()
        query_string = "SELECT * FROM employee WHERE pers_no = '%s' "
        cursor4.execute(query_string, (personid,))
        
        for i3 in cursor4:
            pers_name = i3[1]+' '+i3[2]
        
        mydb4.commit()
        mydb4.close()
        
        remaining_task_sum = str(remaining_task_sum)
        personid = str(personid)
        task_id = str(task_id)
        pers_name = str(pers_name)
        
        mydb5 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor5 = mydb5.cursor()
        
        cursor5.execute('INSERT INTO task_suggetions (pers_no,task_id,pers_name,remaining_task,reason,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s)' , (personid,task_id,pers_name,remaining_task_sum,'The probability task done in time is high','0','0') );
        
        mydb5.commit()
        mydb5.close()
    
    mydb.commit()
    mydb.close()
    
def level11(task_id,no_of_task):
    
    status = []
    
    mydb = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
    
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM ml_task_model where complexity_level = 'Entry' and complexity_level = 'Intermediate' and duration >= 9 and duration <= 12 ORDER BY id ASC");
    
    for i1 in mycursor.fetchall():
        
        if i1[9] == 1:
            status.append(1)
        else:
            status.append(0)
    
    positive = status.count(1)
    negative = status.count(0)
    
    if positive > negative:
        
        pers_name = ''
        
        mydb3 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor3 = mydb3.cursor()
        query_string = "SELECT * FROM task_assigned WHERE task_id = '%s' and status = 'Pending' "
        cursor3.execute(query_string, (task_id,))
        
        remaining_task = []
        personid = 0
        
        for i2 in cursor3:
            personid = i2[1]
            remaining_task.append(i2[0])
        
        remaining_task_sum = sum(remaining_task)
        
        mydb3.commit()
        mydb3.close()
        
        mydb4 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor4 = mydb4.cursor()
        query_string = "SELECT * FROM employee WHERE pers_no = '%s' "
        cursor4.execute(query_string, (personid,))
        
        for i3 in cursor4:
            pers_name = i3[1]+' '+i3[2]
        
        mydb4.commit()
        mydb4.close()
        
        remaining_task_sum = str(remaining_task_sum)
        personid = str(personid)
        task_id = str(task_id)
        pers_name = str(pers_name)
        
        mydb5 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor5 = mydb5.cursor()
        
        cursor5.execute('INSERT INTO task_suggetions (pers_no,task_id,pers_name,remaining_task,reason,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s)' , (personid,task_id,pers_name,remaining_task_sum,'The probability task done in time is high','1','0') );
        
        mydb5.commit()
        mydb5.close()
        
    else:
        
        pers_name = ''
        
        mydb3 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor3 = mydb3.cursor()
        query_string = "SELECT * FROM task_assigned WHERE task_id = '%s' and status = 'Pending' "
        cursor3.execute(query_string, (task_id,))
        
        remaining_task = []
        personid = 0
        
        for i2 in cursor3:
            personid = i2[1]
            remaining_task.append(i2[0])
        
        remaining_task_sum = sum(remaining_task)
        
        mydb3.commit()
        mydb3.close()
        
        mydb4 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor4 = mydb4.cursor()
        query_string = "SELECT * FROM employee WHERE pers_no = '%s' "
        cursor4.execute(query_string, (personid,))
        
        for i3 in cursor4:
            pers_name = i3[1]+' '+i3[2]
        
        mydb4.commit()
        mydb4.close()
        
        remaining_task_sum = str(remaining_task_sum)
        personid = str(personid)
        task_id = str(task_id)
        pers_name = str(pers_name)
        
        mydb5 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor5 = mydb5.cursor()
        
        cursor5.execute('INSERT INTO task_suggetions (pers_no,task_id,pers_name,remaining_task,reason,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s)' , (personid,task_id,pers_name,remaining_task_sum,'The probability task done in time is high','0','0') );
        
        mydb5.commit()
        mydb5.close()
    
    mydb.commit()
    mydb.close()
    
def level12(task_id,no_of_task):
    
    status = []
    
    mydb = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
    
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM ml_task_model where complexity_level = 'Entry' and complexity_level = 'Intermediate' and complexity_level = 'Expert' and duration >= 9 and duration <= 12 ORDER BY id ASC");
    
    for i1 in mycursor.fetchall():
        
        if i1[9] == 1:
            status.append(1)
        else:
            status.append(0)
    
    positive = status.count(1)
    negative = status.count(0)
    
    if positive > negative:
        
        pers_name = ''
        
        mydb3 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor3 = mydb3.cursor()
        query_string = "SELECT * FROM task_assigned WHERE task_id = '%s' and status = 'Pending' "
        cursor3.execute(query_string, (task_id,))
        
        remaining_task = []
        personid = 0
        
        for i2 in cursor3:
            personid = i2[1]
            remaining_task.append(i2[0])
        
        remaining_task_sum = sum(remaining_task)
        
        mydb3.commit()
        mydb3.close()
        
        mydb4 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor4 = mydb4.cursor()
        query_string = "SELECT * FROM employee WHERE pers_no = '%s' "
        cursor4.execute(query_string, (personid,))
        
        for i3 in cursor4:
            pers_name = i3[1]+' '+i3[2]
        
        mydb4.commit()
        mydb4.close()
        
        remaining_task_sum = str(remaining_task_sum)
        personid = str(personid)
        task_id = str(task_id)
        pers_name = str(pers_name)
        
        mydb5 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor5 = mydb5.cursor()
        
        cursor5.execute('INSERT INTO task_suggetions (pers_no,task_id,pers_name,remaining_task,reason,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s)' , (personid,task_id,pers_name,remaining_task_sum,'The probability task done in time is high','1','0') );
        
        mydb5.commit()
        mydb5.close()
        
    else:
        
        pers_name = ''
        
        mydb3 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor3 = mydb3.cursor()
        query_string = "SELECT * FROM task_assigned WHERE task_id = '%s' and status = 'Pending' "
        cursor3.execute(query_string, (task_id,))
        
        remaining_task = []
        personid = 0
        
        for i2 in cursor3:
            personid = i2[1]
            remaining_task.append(i2[0])
        
        remaining_task_sum = sum(remaining_task)
        
        mydb3.commit()
        mydb3.close()
        
        mydb4 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor4 = mydb4.cursor()
        query_string = "SELECT * FROM employee WHERE pers_no = '%s' "
        cursor4.execute(query_string, (personid,))
        
        for i3 in cursor4:
            pers_name = i3[1]+' '+i3[2]
        
        mydb4.commit()
        mydb4.close()
        
        remaining_task_sum = str(remaining_task_sum)
        personid = str(personid)
        task_id = str(task_id)
        pers_name = str(pers_name)
        
        mydb5 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor5 = mydb5.cursor()
        
        cursor5.execute('INSERT INTO task_suggetions (pers_no,task_id,pers_name,remaining_task,reason,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s)' , (personid,task_id,pers_name,remaining_task_sum,'The probability task done in time is high','0','0') );
        
        mydb5.commit()
        mydb5.close()
    
    mydb.commit()
    mydb.close()
    
def level13(task_id,no_of_task):
    
    status = []
    
    mydb = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
    
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM ml_task_model where complexity_level = 'Entry' and duration >= 12 and duration <= 15 ORDER BY id ASC");
    
    for i1 in mycursor.fetchall():
        
        if i1[9] == 1:
            status.append(1)
        else:
            status.append(0)
    
    positive = status.count(1)
    negative = status.count(0)
    
    if positive > negative:
        
        pers_name = ''
        
        mydb3 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor3 = mydb3.cursor()
        query_string = "SELECT * FROM task_assigned WHERE task_id = '%s' and status = 'Pending' "
        cursor3.execute(query_string, (task_id,))
        
        remaining_task = []
        personid = 0
        
        for i2 in cursor3:
            personid = i2[1]
            remaining_task.append(i2[0])
        
        remaining_task_sum = sum(remaining_task)
        
        mydb3.commit()
        mydb3.close()
        
        mydb4 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor4 = mydb4.cursor()
        query_string = "SELECT * FROM employee WHERE pers_no = '%s' "
        cursor4.execute(query_string, (personid,))
        
        for i3 in cursor4:
            pers_name = i3[1]+' '+i3[2]
        
        mydb4.commit()
        mydb4.close()
        
        remaining_task_sum = str(remaining_task_sum)
        personid = str(personid)
        task_id = str(task_id)
        pers_name = str(pers_name)
        
        mydb5 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor5 = mydb5.cursor()
        
        cursor5.execute('INSERT INTO task_suggetions (pers_no,task_id,pers_name,remaining_task,reason,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s)' , (personid,task_id,pers_name,remaining_task_sum,'The probability task done in time is high','1','0') );
        
        mydb5.commit()
        mydb5.close()
        
    else:
        
        pers_name = ''
        
        mydb3 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor3 = mydb3.cursor()
        query_string = "SELECT * FROM task_assigned WHERE task_id = '%s' and status = 'Pending' "
        cursor3.execute(query_string, (task_id,))
        
        remaining_task = []
        personid = 0
        
        for i2 in cursor3:
            personid = i2[1]
            remaining_task.append(i2[0])
        
        remaining_task_sum = sum(remaining_task)
        
        mydb3.commit()
        mydb3.close()
        
        mydb4 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor4 = mydb4.cursor()
        query_string = "SELECT * FROM employee WHERE pers_no = '%s' "
        cursor4.execute(query_string, (personid,))
        
        for i3 in cursor4:
            pers_name = i3[1]+' '+i3[2]
        
        mydb4.commit()
        mydb4.close()
        
        remaining_task_sum = str(remaining_task_sum)
        personid = str(personid)
        task_id = str(task_id)
        pers_name = str(pers_name)
        
        mydb5 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor5 = mydb5.cursor()
        
        cursor5.execute('INSERT INTO task_suggetions (pers_no,task_id,pers_name,remaining_task,reason,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s)' , (personid,task_id,pers_name,remaining_task_sum,'The probability task done in time is high','0','0') );
        
        mydb5.commit()
        mydb5.close()
    
    mydb.commit()
    mydb.close()
    
def level14(task_id,no_of_task):
    
    status = []
    
    mydb = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
    
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM ml_task_model where complexity_level = 'Entry' and complexity_level = 'Intermediate' and duration >= 12 and duration <= 15 ORDER BY id ASC");
    
    for i1 in mycursor.fetchall():
        
        if i1[9] == 1:
            status.append(1)
        else:
            status.append(0)
    
    positive = status.count(1)
    negative = status.count(0)
    
    if positive > negative:
        
        pers_name = ''
        
        mydb3 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor3 = mydb3.cursor()
        query_string = "SELECT * FROM task_assigned WHERE task_id = '%s' and status = 'Pending' "
        cursor3.execute(query_string, (task_id,))
        
        remaining_task = []
        personid = 0
        
        for i2 in cursor3:
            personid = i2[1]
            remaining_task.append(i2[0])
        
        remaining_task_sum = sum(remaining_task)
        
        mydb3.commit()
        mydb3.close()
        
        mydb4 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor4 = mydb4.cursor()
        query_string = "SELECT * FROM employee WHERE pers_no = '%s' "
        cursor4.execute(query_string, (personid,))
        
        for i3 in cursor4:
            pers_name = i3[1]+' '+i3[2]
        
        mydb4.commit()
        mydb4.close()
        
        remaining_task_sum = str(remaining_task_sum)
        personid = str(personid)
        task_id = str(task_id)
        pers_name = str(pers_name)
        
        mydb5 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor5 = mydb5.cursor()
        
        cursor5.execute('INSERT INTO task_suggetions (pers_no,task_id,pers_name,remaining_task,reason,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s)' , (personid,task_id,pers_name,remaining_task_sum,'The probability task done in time is high','1','0') );
        
        mydb5.commit()
        mydb5.close()
        
    else:
        
        pers_name = ''
        
        mydb3 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor3 = mydb3.cursor()
        query_string = "SELECT * FROM task_assigned WHERE task_id = '%s' and status = 'Pending' "
        cursor3.execute(query_string, (task_id,))
        
        remaining_task = []
        personid = 0
        
        for i2 in cursor3:
            personid = i2[1]
            remaining_task.append(i2[0])
        
        remaining_task_sum = sum(remaining_task)
        
        mydb3.commit()
        mydb3.close()
        
        mydb4 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor4 = mydb4.cursor()
        query_string = "SELECT * FROM employee WHERE pers_no = '%s' "
        cursor4.execute(query_string, (personid,))
        
        for i3 in cursor4:
            pers_name = i3[1]+' '+i3[2]
        
        mydb4.commit()
        mydb4.close()
        
        remaining_task_sum = str(remaining_task_sum)
        personid = str(personid)
        task_id = str(task_id)
        pers_name = str(pers_name)
        
        mydb5 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor5 = mydb5.cursor()
        
        cursor5.execute('INSERT INTO task_suggetions (pers_no,task_id,pers_name,remaining_task,reason,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s)' , (personid,task_id,pers_name,remaining_task_sum,'The probability task done in time is high','0','0') );
        
        mydb5.commit()
        mydb5.close()
    
    mydb.commit()
    mydb.close()
    
def level15(task_id,no_of_task):
    
    status = []
    
    mydb = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
    
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM ml_task_model where complexity_level = 'Entry' and complexity_level = 'Intermediate' and complexity_level = 'Expert' and duration >= 12 and duration <= 15 ORDER BY id ASC");
    
    for i1 in mycursor.fetchall():
        
        if i1[9] == 1:
            status.append(1)
        else:
            status.append(0)
    
    positive = status.count(1)
    negative = status.count(0)
    
    if positive > negative:
        
        pers_name = ''
        
        mydb3 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor3 = mydb3.cursor()
        query_string = "SELECT * FROM task_assigned WHERE task_id = '%s' and status = 'Pending' "
        cursor3.execute(query_string, (task_id,))
        
        remaining_task = []
        personid = 0
        
        for i2 in cursor3:
            personid = i2[1]
            remaining_task.append(i2[0])
        
        remaining_task_sum = sum(remaining_task)
        
        mydb3.commit()
        mydb3.close()
        
        mydb4 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor4 = mydb4.cursor()
        query_string = "SELECT * FROM employee WHERE pers_no = '%s' "
        cursor4.execute(query_string, (personid,))
        
        for i3 in cursor4:
            pers_name = i3[1]+' '+i3[2]
        
        mydb4.commit()
        mydb4.close()
        
        remaining_task_sum = str(remaining_task_sum)
        personid = str(personid)
        task_id = str(task_id)
        pers_name = str(pers_name)
        
        mydb5 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor5 = mydb5.cursor()
        
        cursor5.execute('INSERT INTO task_suggetions (pers_no,task_id,pers_name,remaining_task,reason,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s)' , (personid,task_id,pers_name,remaining_task_sum,'The probability task done in time is high','1','0') );
        
        mydb5.commit()
        mydb5.close()
        
    else:
        
        pers_name = ''
        
        mydb3 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor3 = mydb3.cursor()
        query_string = "SELECT * FROM task_assigned WHERE task_id = '%s' and status = 'Pending' "
        cursor3.execute(query_string, (task_id,))
        
        remaining_task = []
        personid = 0
        
        for i2 in cursor3:
            personid = i2[1]
            remaining_task.append(i2[0])
        
        remaining_task_sum = sum(remaining_task)
        
        mydb3.commit()
        mydb3.close()
        
        mydb4 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor4 = mydb4.cursor()
        query_string = "SELECT * FROM employee WHERE pers_no = '%s' "
        cursor4.execute(query_string, (personid,))
        
        for i3 in cursor4:
            pers_name = i3[1]+' '+i3[2]
        
        mydb4.commit()
        mydb4.close()
        
        remaining_task_sum = str(remaining_task_sum)
        personid = str(personid)
        task_id = str(task_id)
        pers_name = str(pers_name)
        
        mydb5 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor5 = mydb5.cursor()
        
        cursor5.execute('INSERT INTO task_suggetions (pers_no,task_id,pers_name,remaining_task,reason,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s)' , (personid,task_id,pers_name,remaining_task_sum,'The probability task done in time is high','0','0') );
        
        mydb5.commit()
        mydb5.close()
    
    mydb.commit()
    mydb.close()
    
def level16(task_id,no_of_task):
    
    status = []
    
    mydb = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
    
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM ml_task_model where complexity_level = 'Entry' and duration >= 15 ORDER BY id ASC");
    
    for i1 in mycursor.fetchall():
        
        if i1[9] == 1:
            status.append(1)
        else:
            status.append(0)
    
    positive = status.count(1)
    negative = status.count(0)
    
    if positive > negative:
        
        pers_name = ''
        
        mydb3 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor3 = mydb3.cursor()
        query_string = "SELECT * FROM task_assigned WHERE task_id = '%s' and status = 'Pending' "
        cursor3.execute(query_string, (task_id,))
        
        remaining_task = []
        personid = 0
        
        for i2 in cursor3:
            personid = i2[1]
            remaining_task.append(i2[0])
        
        remaining_task_sum = sum(remaining_task)
        
        mydb3.commit()
        mydb3.close()
        
        mydb4 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor4 = mydb4.cursor()
        query_string = "SELECT * FROM employee WHERE pers_no = '%s' "
        cursor4.execute(query_string, (personid,))
        
        for i3 in cursor4:
            pers_name = i3[1]+' '+i3[2]
        
        mydb4.commit()
        mydb4.close()
        
        remaining_task_sum = str(remaining_task_sum)
        personid = str(personid)
        task_id = str(task_id)
        pers_name = str(pers_name)
        
        mydb5 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor5 = mydb5.cursor()
        
        cursor5.execute('INSERT INTO task_suggetions (pers_no,task_id,pers_name,remaining_task,reason,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s)' , (personid,task_id,pers_name,remaining_task_sum,'The probability task done in time is high','1','0') );
        
        mydb5.commit()
        mydb5.close()
        
    else:
        
        pers_name = ''
        
        mydb3 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor3 = mydb3.cursor()
        query_string = "SELECT * FROM task_assigned WHERE task_id = '%s' and status = 'Pending' "
        cursor3.execute(query_string, (task_id,))
        
        remaining_task = []
        personid = 0
        
        for i2 in cursor3:
            personid = i2[1]
            remaining_task.append(i2[0])
        
        remaining_task_sum = sum(remaining_task)
        
        mydb3.commit()
        mydb3.close()
        
        mydb4 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor4 = mydb4.cursor()
        query_string = "SELECT * FROM employee WHERE pers_no = '%s' "
        cursor4.execute(query_string, (personid,))
        
        for i3 in cursor4:
            pers_name = i3[1]+' '+i3[2]
        
        mydb4.commit()
        mydb4.close()
        
        remaining_task_sum = str(remaining_task_sum)
        personid = str(personid)
        task_id = str(task_id)
        pers_name = str(pers_name)
        
        mydb5 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor5 = mydb5.cursor()
        
        cursor5.execute('INSERT INTO task_suggetions (pers_no,task_id,pers_name,remaining_task,reason,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s)' , (personid,task_id,pers_name,remaining_task_sum,'The probability task done in time is high','0','0') );
        
        mydb5.commit()
        mydb5.close()
    
    mydb.commit()
    mydb.close()
    
def level17(task_id,no_of_task):
    
    status = []
    
    mydb = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
    
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM ml_task_model where complexity_level = 'Entry' and complexity_level = 'Intermediate' and duration >= 15 ORDER BY id ASC");
    
    for i1 in mycursor.fetchall():
        
        if i1[9] == 1:
            status.append(1)
        else:
            status.append(0)
    
    positive = status.count(1)
    negative = status.count(0)
    
    if positive > negative:
        
        pers_name = ''
        
        mydb3 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor3 = mydb3.cursor()
        query_string = "SELECT * FROM task_assigned WHERE task_id = '%s' and status = 'Pending' "
        cursor3.execute(query_string, (task_id,))
        
        remaining_task = []
        personid = 0
        
        for i2 in cursor3:
            personid = i2[1]
            remaining_task.append(i2[0])
        
        remaining_task_sum = sum(remaining_task)
        
        mydb3.commit()
        mydb3.close()
        
        mydb4 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor4 = mydb4.cursor()
        query_string = "SELECT * FROM employee WHERE pers_no = '%s' "
        cursor4.execute(query_string, (personid,))
        
        for i3 in cursor4:
            pers_name = i3[1]+' '+i3[2]
        
        mydb4.commit()
        mydb4.close()
        
        remaining_task_sum = str(remaining_task_sum)
        personid = str(personid)
        task_id = str(task_id)
        pers_name = str(pers_name)
        
        mydb5 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor5 = mydb5.cursor()
        
        cursor5.execute('INSERT INTO task_suggetions (pers_no,task_id,pers_name,remaining_task,reason,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s)' , (personid,task_id,pers_name,remaining_task_sum,'The probability task done in time is high','1','0') );
        
        mydb5.commit()
        mydb5.close()
        
    else:
        
        pers_name = ''
        
        mydb3 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor3 = mydb3.cursor()
        query_string = "SELECT * FROM task_assigned WHERE task_id = '%s' and status = 'Pending' "
        cursor3.execute(query_string, (task_id,))
        
        remaining_task = []
        personid = 0
        
        for i2 in cursor3:
            personid = i2[1]
            remaining_task.append(i2[0])
        
        remaining_task_sum = sum(remaining_task)
        
        mydb3.commit()
        mydb3.close()
        
        mydb4 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor4 = mydb4.cursor()
        query_string = "SELECT * FROM employee WHERE pers_no = '%s' "
        cursor4.execute(query_string, (personid,))
        
        for i3 in cursor4:
            pers_name = i3[1]+' '+i3[2]
        
        mydb4.commit()
        mydb4.close()
        
        remaining_task_sum = str(remaining_task_sum)
        personid = str(personid)
        task_id = str(task_id)
        pers_name = str(pers_name)
        
        mydb5 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor5 = mydb5.cursor()
        
        cursor5.execute('INSERT INTO task_suggetions (pers_no,task_id,pers_name,remaining_task,reason,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s)' , (personid,task_id,pers_name,remaining_task_sum,'The probability task done in time is high','0','0') );
        
        mydb5.commit()
        mydb5.close()
    
    mydb.commit()
    mydb.close()
    
def level18(task_id,no_of_task):
    
    status = []
    
    mydb = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
    
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM ml_task_model where complexity_level = 'Entry' and complexity_level = 'Intermediate' and complexity_level = 'Expert' and duration >= 15 ORDER BY id ASC");
    
    for i1 in mycursor.fetchall():
        
        if i1[9] == 1:
            status.append(1)
        else:
            status.append(0)
    
    positive = status.count(1)
    negative = status.count(0)
    
    if positive > negative:
        
        pers_name = ''
        
        mydb3 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor3 = mydb3.cursor()
        query_string = "SELECT * FROM task_assigned WHERE task_id = '%s' and status = 'Pending' "
        cursor3.execute(query_string, (task_id,))
        
        remaining_task = []
        personid = 0
        
        for i2 in cursor3:
            personid = i2[1]
            remaining_task.append(i2[0])
        
        remaining_task_sum = sum(remaining_task)
        
        mydb3.commit()
        mydb3.close()
        
        mydb4 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor4 = mydb4.cursor()
        query_string = "SELECT * FROM employee WHERE pers_no = '%s' "
        cursor4.execute(query_string, (personid,))
        
        for i3 in cursor4:
            pers_name = i3[1]+' '+i3[2]
        
        mydb4.commit()
        mydb4.close()
        
        remaining_task_sum = str(remaining_task_sum)
        personid = str(personid)
        task_id = str(task_id)
        pers_name = str(pers_name)
        
        mydb5 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor5 = mydb5.cursor()
        
        cursor5.execute('INSERT INTO task_suggetions (pers_no,task_id,pers_name,remaining_task,reason,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s)' , (personid,task_id,pers_name,remaining_task_sum,'The probability task done in time is high','1','0') );
        
        mydb5.commit()
        mydb5.close()
        
    else:
        
        pers_name = ''
        
        mydb3 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor3 = mydb3.cursor()
        query_string = "SELECT * FROM task_assigned WHERE task_id = '%s' and status = 'Pending' "
        cursor3.execute(query_string, (task_id,))
        
        remaining_task = []
        personid = 0
        
        for i2 in cursor3:
            personid = i2[1]
            remaining_task.append(i2[0])
        
        remaining_task_sum = sum(remaining_task)
        
        mydb3.commit()
        mydb3.close()
        
        mydb4 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor4 = mydb4.cursor()
        query_string = "SELECT * FROM employee WHERE pers_no = '%s' "
        cursor4.execute(query_string, (personid,))
        
        for i3 in cursor4:
            pers_name = i3[1]+' '+i3[2]
        
        mydb4.commit()
        mydb4.close()
        
        remaining_task_sum = str(remaining_task_sum)
        personid = str(personid)
        task_id = str(task_id)
        pers_name = str(pers_name)
        
        mydb5 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor5 = mydb5.cursor()
        
        cursor5.execute('INSERT INTO task_suggetions (pers_no,task_id,pers_name,remaining_task,reason,allow,seen) VALUES (%s,%s,%s,%s,%s,%s,%s)' , (personid,task_id,pers_name,remaining_task_sum,'The probability task done in time is high','0','0') );
        
        mydb5.commit()
        mydb5.close()
    
    mydb.commit()
    mydb.close()
        
def main():
    
    duration = []
    complexity = []
    task_id = []
    
    mydb = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
    
    maincursor = mydb.cursor()
    maincursor.execute("SELECT * FROM task_assigned where status = 'Pending' ORDER BY id ASC LIMIT 1");
    
    for i in maincursor:
        
        mydb2 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
        cursor2 = mydb2.cursor()
        query_string = "SELECT * FROM task WHERE task_id = '%s' "
        cursor2.execute(query_string, (i[2],))
        ##data = cursor2.fetchall()
        
        for i3 in cursor2:
            task_id.append(i3[1])
            duration.append(i3[3])
            complexity.append(i3[7])

        mydb2.commit()
        mydb2.close()
    
    duration_length = len(duration)
    complexity_length = len(complexity)
    duration_sum = sum(duration)
    
    if(duration_sum > 0):
        duration_final = duration_sum / duration_length
    else:
        duration_final = 0
    
    match1 = ["Entry"]
    match2 = ["Entry","Intermediate"]
    match3 = ["Entry","Intermediate","Expert"]
    
    match1.sort()
    match2.sort()
    match3.sort()
    
    task_id = list(dict.fromkeys(task_id))
    task_id = sum(task_id)
    
    refined_complexity = list(dict.fromkeys(complexity))
    refined_complexity.sort()
    
    no_of_task = duration_length
    
    if duration_final >= 1 and duration_final <= 3:
        if refined_complexity == match1:
            level1(task_id,no_of_task)
        elif refined_complexity == match2:
            level2(task_id,no_of_task)
        elif refined_complexity == match3:
            level3(task_id,no_of_task)
    elif duration_final >= 3 and duration_final <= 6:
        if refined_complexity == match1:
            level4(task_id,no_of_task)
        elif refined_complexity == match2:
            level5(task_id,no_of_task)
        elif refined_complexity == match3:
            level6(task_id,no_of_task)
    elif duration_final >= 6 and duration_final <= 9:
        if refined_complexity == match1:
            level7(task_id,no_of_task)
        elif refined_complexity == match2:
            level8(task_id,no_of_task)
        elif refined_complexity == match3:
            level9(task_id,no_of_task)
    elif duration_final >= 9 and duration_final <= 12:
        if refined_complexity == match1:
            level10(task_id,no_of_task)
        elif refined_complexity == match2:
            level11(task_id,no_of_task)
        elif refined_complexity == match3:
            level12(task_id,no_of_task)
    elif duration_final >= 12 and duration_final <= 15:
        if refined_complexity == match1:
            level13(task_id,no_of_task)
        elif refined_complexity == match2:
            level14(task_id,no_of_task)
        elif refined_complexity == match3:
            level15(task_id,no_of_task)
    elif duration_final >= 15:
        if refined_complexity == match1:
            level16(task_id,no_of_task)
        elif refined_complexity == match2:
            level17(task_id,no_of_task)
        elif refined_complexity == match3:
            level18(task_id,no_of_task)
    
    maincursor.close()
    
host_name = "localhost"
user_name = "root"
user_password = ""
db_name = "mi_model"

main()

print('\n','Done','\n')


# In[ ]:




