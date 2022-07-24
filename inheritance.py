import logging as lg
lg.basicConfig(filename='oops.log',level=lg.DEBUG,format='%(asctime)s %(levelname)s %(name)s %(message)s')
lg.info("INHERITANCE")

class ineuron:
    lg.info("Parent class")
    def __init__(self,student_name,user_id,password):
        self.student_name=student_name
        self.user_id=user_id
        self.passwprd=password

    def courses(self):
        lg.info("Courses availability")
        try:
            lg.info("Multiple courses are available in all the domains:")
            return "GO TO COURSES"
        except Exception as e:
            lg.exception(e)

    def internship(self):
        lg.info("Internship options")
        try:
            lg.info("Student can take free internship:  ")
            return "FREE INTERNSHIP"
        except Exception as e:
            lg.exception(e)

    def one_neuron(self):
        lg.info("for education:  ")
        try:
            lg.info("OTT platfomr for a range of demanding courses:  ")
            return "OTT FOR EDUCATION"
        except Exception as e:
            lg.exception(e)



class ineuron_intelligence(ineuron):
    lg.info("inheritaed class:  ")
    def reseach(self):
        lg.info("reseach center: ")
        try:
            lg.info("reseach team for product developments")
            return "R&D CENTER FOR PRODUCT DEVELOPMENT"
        except Exception as e:
            lg.exception(e)

class ineuron_solutions(ineuron_intelligence):
    lg.info("inheritaed sub class:  ")
    def solutions(self):
        lg.info("solution center:  ")
        try:
            lg.info("Dev team for app developments  ")
            return "Business sol to ineuron: "
        except Exception as e:
            lg.exception(e)

try:
    i = ineuron_solutions("Bhavani Hegde", 1234, "password")
    lg.info("Name of Student is: %s", i.student_name)
    lg.info("Courses: %s", i.courses())
    lg.info("Internship: %s", i.internship())
    lg.info("OTT: %s", i.one_neuron())
    lg.info("OTT: %s", i.Research())
    lg.info("OTT: %s", i.Solutions())

except Exception as e:
    lg.exception(e)