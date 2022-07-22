#encapsulation
import logging as lg
lg.basicConfig(filename="oops.log",level=lg.DEBUG,format='%(asctime)s, %(levelname)s, %(name)s, %(message)s')
lg.info("Encapsulation")

class employee:
    def __init__(self):
        self.__name="Bhavani Hegde"
        self.__role="Data analyst"
        self.__yob=1984
        self.__salary=50000
        self.__hours_per_week=40
        self.__benefits = ['HRA','TA']
        self.city="Bangalore"
        self.week_off=['Saturday','sunday']

    def mod_role(self):
        try:
            self.__role='senior developer'
            lg.info("new role: %s",self.__role)
            return "Role changed"
        except Exception as e:
            lg.exception(e)

    def mod_salary(self):
        try:
            self.__salary = 70000
            lg.info("new salary is %s",self.__salary)
            return "Salary updated"
        except Exception as e:
            lg.exception(e)

    def mod_workhours(self):
        try:
            self.__hours_per_week = 45
            lg.info("New hours of work per week:  %s",self.__hours_per_week)
            return "No of working hours per week has been changed"
        except Exception as e:
            lg.exception(e)

    def mod_benefits(self):
        try:
            self.__benefits=['HRA','TA','LTA']
            lg.info("New befefits are: %s",self.__benefits)
            return "Benefits has been changed"
        except Exception as e:
            lg.exception(e)


    try:
        emp1=employee()
        lg.info("Current working city is : %s",emp1.city)
        emp1.city="bangalore"
        lg.info("The current working city has been changed to %s:",emp1.city)

        lg.info("current role is  %s",emp1._employee__role)
        lg.info(emp1.mod_role())
        lg.info("the role has been modified to %s",emp1._employee__role)

        lg.info("current salary is %s",emp1._employee__salary)
        lg.info(emp1.mod_salary())
        lg.info("the salary has been modifeid to %s",emp1._employee__salary)

        lg.info("Current working hours per week:  %s",emp1._employee__hours_per_week)
        lg.info(emp1.mod_workhours())
        lg.info("The working hours modified to %s", emp1._employee__hours_per_week)

        lg.info("current benifits are: %s",emp1._employee__benefits)
        lg.info(mod_benefits())
        lg.info("the benefits has been changed to %s",emp1._employee__benefits)

        lg.info("Current week offs are :  %s",emp1.week_off)
        emp1.week_off = ['Sunday','Monday']
        lg.info("Week off has been updated: ", emp1.week_off)

    except Exception as e:
        lg.exception(e)
