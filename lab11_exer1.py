import psycopg2


# Connect to the database by creating connection variable or object
conn = psycopg2.connect(
    host="localhost",
    database="students_data",
    user="postgres",
    password="Alisher_18"
)

# Creating cursor to get access to database
cur=conn.cursor()


# Delete previous table
cur.execute("DROP TABLE students_data")

# Creating table
cur.execute("""CREATE TABLE students_data(
            name VARCHAR (255),
            phone_number VARCHAR (255) PRIMARY KEY

);""")
conn.commit()

# Inserting the information
cur.execute("""INSERT INTO students_data(name,phone_number) VALUES
            ('Maxim','+7708765432'),
            ('Alisher','+08876765'),
            ('Ivan','+77072345678'),
            ('Nikita','+770798756547'),
            ('Denis','46746474647');
""")
#Input values
print("Enter your name: ")
input_name=input()
print("Enter your phone number: ")
input_phone_number=input()

# All_names
all_names=["Alisher","Maxim","Nikita","Ivan","Denis"]
all_phone_numbers=["+7709876546","+7707654332","+7797654332","+80987363355","+98725363536"]


cnt=0
for name in all_names:
    if input_name==name:
        cur.execute("""UPDATE students_data
                    Set phone_number='0000'
                    WHERE name=(%s)""",(input_name,)
                    )
        cnt=0
        break
    else:
        cnt+=1
    
if cnt==len(all_names):  
  cur.execute("""INSERT INTO students_data(name,phone_number) VALUES(%s,%s)""",(input_name,input_phone_number))


conn.commit()
