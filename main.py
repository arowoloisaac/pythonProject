import mysql.connector
import display

from datetime import datetime

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="3001",
    database="company"
)

mycursor = mydb.cursor()


def add_branch():  # 1 marked
    sql = "insert into company.branch(branch_name, mgr_id, mgr_start_date) values(%s,%s, %s)"
    # id = int(input("Enter the branch id: "))
    name = input("Enter Branch Name: ")
    start_date = str(datetime.today()).split()[0]
    manager_id = int(input("Enter your manager Id: "))
    val = (name, manager_id, start_date)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted")
    for x in mycursor:
        print(x)
    print("completed")
    pass


def set_parent():  # 2 marked
    sql = """
     update branch
     set Hierarchy_id = %s
     where branch_id = %s;
     """
    rank_id = int(input("Enter the rank Id: "))
    branch_id = int(input("Enter the branch Id: "))
    val = (rank_id, branch_id)
    mycursor.execute(sql, val)
    mydb.commit()
    print("record insert")
    for x in mycursor:
        print(x)
    print("completed")
    pass


def list_branches():  # 3 marked
    sql = "select * from branch;"
    mycursor.execute(sql)
    my_result = mycursor.fetchall()
    for x in my_result:
        print(x)
    print("completed")
    pass


def list_suppliers():  # 4 marked
    sql = "select * from company.branch_supplier where ref_branch_id = %s;"
    branch_id = int(input("Enter The Branch Id: "))
    val = (branch_id,)
    mycursor.execute(sql, val)
    my_result = mycursor.fetchall()
    for x in my_result:
        print(x)
    print("completed")
    pass


def foreign_manager():  # 5
    sql = """
     SELECT *, COUNT(*)
    FROM (SELECT *, COUNT(*) AS CNT
    from company.branch
    GROUP BY Hierarchy_id) AS T
    WHERE CNT > 0
    """
    mycursor.execute(sql)
    my_result = mycursor.fetchall()
    for x in my_result:
        print(x)
    print("completed")
    pass


def empty_branches():  # 6
    sql = "select * from company.employee where branch_id is NULL"
    mycursor.execute(sql)
    my_result = mycursor.fetchall()
    for x in my_result:
        print(x)
    print("completed")
    pass


def vip_clients():  # 7 marked
    sql = """
        select emp_id, client_id, count(client_id) from company.works_with 
        group by emp_id
        having count(client_id) =1;
    """
    mycursor.execute(sql)
    my_result = mycursor.fetchall()
    for x in my_result:
        print(x)
    print("completed")
    pass


def hard_workers():  # 8 marked
    sql = """
     select emp_id, count(client_id)
     from company.works_with
     group by emp_id
     order by count(client_id)
     desc limit 10;
     """
    mycursor.execute(sql)
    my_result = mycursor.fetchall()
    for x in my_result:
        print(x)
    print("completed")
    pass


def effectiveness():  # 9 marked
    sql = """
    select 
    (select count(client_id) from company.client where ref_branch_id = 1)/(select count(branch_id) from company.employee where branch_id = %s)
    as divide;
    """
    branch_id = int(input("Enter The Branch Id: "))
    val = (branch_id,)
    mycursor.execute(sql, val)
    my_result = mycursor.fetchall()
    for x in my_result:
        print(x)
    print("completed")
    pass


def popular_names():  # 10 marked
    sql = """
           select * from 
            (
                (Select first_name as fname, count(emp_id) 
                FROM company.employee  group by fname)
                UNION all 
                (SELECT last_name as lname, count(emp_id) 
                FROM company.employee group by lname)
                union all
                (select client_name as cname, count(client_id)
                from company.client group by cname)
            ) as t
            order by 2 desc;
           """
    mycursor.execute(sql)
    my_result = mycursor.fetchall()
    for x in my_result:
        print(x)
    print("completed")
    pass


if __name__ == "__main__":

    print("QUERY HERE 😂")
    check = input("Do you want to add query to the database (Yes/ N0): ")
    if check.upper() == "YES":
        display.dis()
        x = int(input("perform query (1/0): "))
        while x == 1:
            print("If you want to break out of the loop input 0 😂😂😂")
            my_case = int(input("Enter A Number To Perform The Query(1 - 10): "))
            if my_case == 1:
                add_branch()
                pass

            elif my_case == 2:
                set_parent()
                pass

            elif my_case == 3:
                list_branches()
                pass

            elif my_case == 4:
                list_suppliers()
                pass

            elif my_case == 5:
                foreign_manager()
                pass

            elif my_case == 6:
                empty_branches()
                pass

            elif my_case == 7:
                vip_clients()
                pass

            elif my_case == 8:
                hard_workers()
                pass

            elif my_case == 9:
                effectiveness()
                pass

            elif my_case == 10:
                popular_names()
                pass

            elif my_case == 0:
                print("Query Completed or you breakout of the loop")
                break

            else:
                print("Not Valid. Choose from 1 - 10 \n")

            pass
        else:
            print("Query Completed")
    pass
