
#publik
#private
#protactive

#task: for all the concept that we have discussed in our classa
#point by point u have to write atleast 10 examples

#u have to make sure that use ineuron student ,class, class type,
# number of courses. affiliate ,blog ,internship ,job as a reference example

import logging as lg
lg.basicConfig(filename="oops.log",level=lg.DEBUG,format='%(asctime)s %(levelname)s %(name)s %(message)s')

class company:
    def __init__(self,CEO,CFO,CTO,CBO,CMO,count_dev,count_analyst,count_support,count_mle,count_devops):
        lg.info("Classification of class variables: private, public and protected")

        self.CEO = CEO
        self.CFO = CFO
        self.CTO = CTO
        self.__CBO = CBO
        self.__CMO = CMO
        self.__dev_count = count_dev
        self._analyst_count = count_analyst
        self._support_count = count_support
        self._mle_count = count_mle
        self._devops_count = count_devops

try:
    lg.info("Creating an object of the class company")
    ineuron = company('Sudhanshu Kumar', 'Krish Naik', 'Hitesh Choudhary', 'Manoj Kumar', 'Darius', 15, 20, 10, 18, 12)

    lg.info("CEO of ineuron is: %s", ineuron.CEO)

    lg.info("CFO of ineuron is: %s", ineuron.CFO)

    lg.info("CTO of ineuron is: %s", ineuron.CTO)

    lg.info("CBO of ineuron is: %s", ineuron._company__CBO)

    lg.info("CMO of ineuron is: %s", ineuron._company__CMO)

    lg.info("Total developers in ineuron is: %s", ineuron._company__dev_count)

    lg.info("Total analyst in ineuron is: %s", ineuron._count_analyst)

    lg.info("Total support team in ineuron is: %s", ineuron._count_support)

    lg.info("Total mle in ineuron is: %s", ineuron._count_mle)

    lg.info("Total devops in ineuron is: %s", ineuron._count_devops)


except Exception as e:
    lg.exception(e)