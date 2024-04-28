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

# All_names
all_names=["Alisher","Maxim","Nikita","Ivan","Denis"]
all_phone_numbers=["+7709876546","+7707654332","+7797654332","+80987363355","+98725363536"]




result_wrong_numbers=["2","3","4"]
index=0
cnt=0
#Input_list_names_and_numbers
for i in range(3):
    print("Enter the name : ")
    name_input=input()
    print("Enter the phone number: ")
    phone_number_input=input()
    for name in all_names:
        if name==name_input:
            for phone_number in all_phone_numbers:
                if phone_number_input!=phone_number:
                    cnt+=1
            if cnt==5:
                result_wrong_numbers[index]="Your numbers is wrong: "+str(name_input)
                index+=1
                cnt=0
 
for i in result_wrong_numbers:
    print(i)
    index-=1
    if index==0:
        break

            





conn.commit()