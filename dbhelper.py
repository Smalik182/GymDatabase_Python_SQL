import mysql.connector as connector



class DBHelper:
    def __init__(self):
        self.con = connector.connect(host = 'localhost',
                                      port ='3306',
                                        user = 'root',
                                          password = 'Noodle987!',
                                            database = 'GymManagement')
        cur = self.con.cursor()
        query = 'create table if not exists member(memberID int primary key, memberName varchar(200), phone varchar(12))'
        cur.execute(query)
        query = 'create table if not exists employee(employeeID int primary key, employeeName varchar(200), phone varchar(12))'
        cur.execute(query)
        query = 'create table if not exists trainer(trainerID int primary key, trainerName varchar(200), phone varchar(12))'        
        cur.execute(query)
        print("Created")


    # *****************************************Insert into tables*******************************************************************

    # Insert member
    def insert_member(self, memberID, memberName, phone):
        query = "insert into member(memberID, memberName, phone) values({},'{}', '{}')".format(memberID, memberName, phone)
        #print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Member saved to database")


    #Insert employee
    def insert_employee(self, employeeID, employeeName, phone):
        query = "insert into employee(employeeID, employeeName, phone) values({},'{}', '{}')".format(employeeID, employeeName, phone)
        #print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Employee saved to database")

    # Insert trainer
    def insert_trainer(self, trainerID, trainerName, phone):
        query = "insert into trainer(trainerID, trainerName, phone) values({},'{}', '{}')".format(trainerID, trainerName, phone)
        #print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("Trainer saved to database")


    # *****************************************Fetch tables*******************************************************************


    # Fetch member table
    def fetch_member(self):
        query = "select * from member"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("Member ID: ", row[0])
            print("Member Name: ", row[1])
            print("Member Phone: ", row[2])
            print()
            print()


    # Fetch employee table
    def fetch_employee(self):
        query = "select * from employee"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("Employee ID: ", row[0])
            print("Employee Name: ", row[1])
            print("Employee Phone: ", row[2])
            print()
            print()

    # Fetch trainer
    def fetch_trainer(self):
        query = "select * from trainer"
        cur = self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("Trainer ID: ", row[0])
            print("Trainer Name: ", row[1])
            print("Trainer Phone: ", row[2])
            print()
            print()


    # *****************************************Delete tables*******************************************************************

    
    # Delete member
    def delete_member(self,memberID):
        query = "delete from member where memberID = {}".format(memberID)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        print("Deleted")


    # Delete employee
    def delete_employee(self,employeeID):
        query = "delete from employee where employeeID = {}".format(employeeID)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        print("Deleted")

    # Delete trainer
    def delete_trainer(self,trainerID):
        query = "delete from trainer where trainerID = {}".format(trainerID)
        print(query)
        cur = self.con.cursor()
        cur.execute(query)
        print("Deleted")



    # *****************************************Update tables*******************************************************************


    # Update member
    def update_member(self, memberID, newName, newPhone):
        query = "update member set memberName = '{}', phone = '{}' where memberId = {}".format(newName,newPhone, memberID)
        #print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("updated")

    # Update employee
    def update_employee(self, employeeID, newName, newPhone):
        query = "update employee set employeeName = '{}', phone = '{}' where employeeId = {}".format(newName,newPhone, employeeID)
        #print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("updated")

    # Update trainer
    def update_trainer(self, trainerID, newName, newPhone):
        query = "update trainer set trainerName = '{}', phone = '{}' where trainerId = {}".format(newName,newPhone, trainerID)
        #print(query)
        cur = self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("updated")
