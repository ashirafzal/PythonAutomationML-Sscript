import mysql.connector
from mysql.connector import cursor
import datetime
        
def main():

    pers_no = 0
    slots = []
    tasks = []
    doc_id = 0

    mydb = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
    
    maincursor = mydb.cursor()
    maincursor.execute("SELECT * FROM specific_doc where type = 'task' ORDER BY id DESC LIMIT 1")

    for i in maincursor:
        pers_no = i[1]
        doc_id = i[0]

    now = datetime.datetime.now()
    day = now.strftime("%A")

    cursor2 = mydb.cursor()
    query_string = "SELECT * FROM time_table WHERE pers_no = '%s' and day = %s "
    cursor2.execute(query_string, (pers_no,day))

    for i2 in cursor2:
        slots.append(i2[0])

    slots = len(slots)

    status = 'Pending'

    cursor3 = mydb.cursor()
    query_string = "SELECT * FROM task_assigned WHERE pers_no = '%s' and status = %s "
    cursor3.execute(query_string, (pers_no,status))

    for i3 in cursor3:
        tasks.append(i3[0])
    
    tasks = len(tasks)
    doc_id = str(doc_id)
    pers_no = str(pers_no)

    decision(doc_id,tasks,slots,pers_no)

    mydb.commit()
    mydb.close()


def decision(doc_id,tasks,slots,pers_no):

    point1 = []
    point2 = []
    pers_name = ''

    mydb = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)

    cursor = mydb.cursor()
    query_string = "SELECT * FROM ml_doc_model WHERE no_of_slots = '%s' and no_of_tasks = %s "
    cursor.execute(query_string, (slots,tasks))

    mydb4 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
    cursor4 = mydb4.cursor()
    query_string = "SELECT * FROM employee WHERE pers_no = %s "
    cursor4.execute(query_string, (pers_no,))
    
    for i3 in cursor4:
        pers_name = i3[1]+' '+i3[2]
    
    mydb4.commit()
    mydb4.close()

    for i in cursor:
        if i[3] == 1:
            point1.append(1)
        else:
            point1.append(0)

        if i[4] == 1:
            point2.append(1)
        else:
            point2.append(0)

    Boolean1 = point1.count(1)
    Boolean2 = point1.count(0)

    Boolean3 = point2.count(1)
    Boolean4 = point2.count(0)

    mydb5 = mysql.connector.connect(host=host_name, user=user_name, password=user_password ,db=db_name)
    cursor5 = mydb5.cursor()


    if Boolean1 > Boolean2:
        if Boolean3 > Boolean4:
            cursor5.execute('INSERT INTO doc_suggestions (doc_id,pers_no,pers_name,pending_task,slots,reason,allow,completed_in_time,seen) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)' ,
                (doc_id,pers_no,pers_name,tasks,slots,'The probability of this task to be done is very high','1','1','0') )
        else:
            cursor5.execute('INSERT INTO doc_suggestions (doc_id,pers_no,pers_name,pending_task,slots,reason,allow,completed_in_time,seen) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)' ,
                (doc_id,pers_no,pers_name,tasks,slots,'The probability of this task to be done is good but lately','1','0','0') )
    else:
        cursor5.execute('INSERT INTO doc_suggestions (doc_id,pers_no,pers_name,pending_task,slots,reason,allow,completed_in_time,seen) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)' ,
                (doc_id,pers_no,pers_name,tasks,slots,'The probability of this task to be done is very low','0','0','0') )


    mydb5.commit()
    mydb5.close()

host_name = "localhost"
user_name = "root"
user_password = ""
db_name = "cis_office"

main()

print('\n','Done','\n')
