import mysql.connector
def DataUpdate(First_name,last_name,email,mob_number):
    mydb= mysql.connector.connect(
        host= "localhost",
        user="root",
        passwd="bhaturae3",
        database="Rasa_chat_forms",
        auth_plugin='mysql_native_password'
    )
    mycursor=mydb.cursor()
    #sql= "CREATE TABLE form_entries_2(First__name VARCHAR(255), last_name VARCHAR(255),email VARCHAR(255), mob_number VARCHAR(255));"
    sql= 'INSERT INTO form_entries_2(First__name,last_name,email,mob_number) VALUES ("{0}","{1}","{2}","{3}");'.format(First_name,last_name,email,mob_number)
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "entry successfully stored")
if __name__=='__main__':
    DataUpdate("karam","Arora","arorakaram41@gmail.com","8368055676")