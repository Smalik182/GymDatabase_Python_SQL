from dbhelper import DBHelper







# Main

def main():


    # Calling DB object
    db = DBHelper()

    while True:
        print("********************************Gym Database System****************************************")
        print("Press 1 to eneter member menu")
        print("Press 2 to eneter employee menu")
        print("Press 3 to eneter trainer menu")
        print("Press 4 to exit program")
        print()

        try:
            choice = int(input())
            if (choice == 1):
                while True:
                    print("********************************Member Database System****************************************")
                    print("Press 1 to insert a new member")
                    print("Press 2 to update a existing member")
                    print("Press 3 to delete a member")
                    print("Press 4 to view member database")
                    print("Press 5 to exit program")
                    print()
                    

                    try:
                        choice = int(input())
                        if (choice == 1):

                            #insert member

                            mID = int(input("Enter Member ID: "))
                            memberName = input("Enter Member Name: ")
                            memberPhone = input("Enter Member Phone: ")
                            db.insert_member(mID, memberName, memberPhone)
                            

                        elif choice == 2:

                            # update member
                            mID = int(input("Enter the member ID of the member you want to update: "))
                            memberName = input("Enter the new Name: ")
                            memberPhone = input("Enter the new Phone Number: ")
                            db.update_member(mID, memberName, memberPhone)
                            pass

                        elif choice == 3:

                            # delete member
                            mID = int(input("Enter the member ID of the member you want to delete: "))
                            db.delete_member(mID)
                            pass

                        elif choice == 4:

                            # display members
                            db.fetch_member()
                            pass
                        elif choice == 5:
                            break
                        else:
                            print("Invalid input, try again")
                    except Exception as e:
                        print(e)
                        print("Invalid input, try again.")
                        
                    pass
            elif choice == 2:
                while True:
                    print("********************************Employee Database System****************************************")
                    print("Press 1 to insert a new employee")
                    print("Press 2 to update a existing employee")
                    print("Press 3 to delete a employee")
                    print("Press 4 to view employee database")
                    print("Press 5 to exit program")
                    print()

                    try:
                        choice = int(input())
                        if (choice == 1):

                            #insert employee

                            eID = int(input("Enter employee ID: "))
                            employeeName = input("Enter Employee Name: ")
                            employeePhone = input("Enter Employee Phone: ")
                            db.insert_employee(eID, employeeName, employeePhone)
                            

                        elif choice == 2:

                            # update employee
                            eID = int(input("Enter the employee ID of the member you want to update: "))
                            employeeName = input("Enter the new Name: ")
                            employeePhone = input("Enter the new Phone Number: ")
                            db.update_employee(eID, employeeName, employeePhone)
                            pass

                        elif choice == 3:

                            # delete employee
                            eID = int(input("Enter the Employee ID of the member you want to delete: "))
                            db.delete_employee(eID)
                            pass

                        elif choice == 4:

                            # display members
                            db.fetch_employee()
                            pass
                        elif choice == 5:
                            break
                        else:
                            print("Invalid input, try again")
                    except Exception as e:
                        print(e)
                        print("Invalid input, try again.")
                        
                    pass


                    pass

            elif choice == 3:
                while True:
                    print("********************************Trainer Database System****************************************")
                    print("Press 1 to insert a new trainer")
                    print("Press 2 to update a existing trainer")
                    print("Press 3 to delete a trainer")
                    print("Press 4 to view trainer database")
                    print("Press 5 to exit program")
                    print()

                    try:
                        choice = int(input())
                        if (choice == 1):

                            #insert trainer

                            tID = int(input("Enter Trainer ID: "))
                            trainerName = input("Enter Trainer Name: ")
                            trainerPhone = input("Enter Trainer Phone: ")
                            db.insert_trainer(tID, trainerName, trainerPhone)
                            

                        elif choice == 2:

                            # update trainer
                            tID = int(input("Enter the trainer ID of the trainer you want to update: "))
                            trainerName = input("Enter the new Name: ")
                            trainerPhone = input("Enter the new Phone Number: ")
                            db.update_trainer(tID, trainerName, trainerPhone)
                            pass

                        elif choice == 3:

                            # delete trainer
                            tID = int(input("Enter the trainer ID of the member you want to delete: "))
                            db.delete_trainer(tID)
                            pass

                        elif choice == 4:

                            # display trainer
                            db.fetch_trainer()
                            pass
                        elif choice == 5:
                            break
                        else:
                            print("Invalid input, try again")
                    except Exception as e:
                        print(e)
                        print("Invalid input, try again.")

                    pass

            elif choice == 4:
                break
            else:
                print("Invalid input, try again.")
        
        except Exception as e:
            print(e)
            print("Invalid input, try again.")




if __name__ == "__main__":
    main()