class IT_Cluster:
    
    numberOfITClusters = 3

    def __init__(self, city, numberOfMembers, chiefOfCluster, numberOfProjects, yearOfFounding, numberOfPartners):
        self.city = city
        self.numberOfMembers = numberOfMembers
        self.chiefOfCluster = chiefOfCluster
        self.numberOfProjects = numberOfProjects
        self.yearOfFounding = yearOfFounding
        self.numberOfPartners = numberOfPartners

    def printITCluster(self):
        print (self.city, self.numberOfMembers, self.chiefOfCluster,
               self.numberOfProjects, self.yearOfFounding, self.numberOfPartners)

    def getNumberOfITClusters(self):
        return self.getNumberOfITClusters ( )

    def __del__(self):
        del self.city
        del self.numberOfMembers
        del self.chiefOfCluster
        del self.numberOfProjects
        del self.yearOfFounding
        del self.numberOfPartners


def main():
    defaultITCluster = IT_Cluster ('ww', 22, '222', 22, 34, 55)
    LvivITCluster = IT_Cluster ('Lviv', 100, 'StepanVeselovskiy', 10, 2010, 50)
    KyivITCluster = IT_Cluster ('Kyiv', 92, 'NataliaVeremeeva', 5, 2012, 45)

    defaultITCluster.printITCluster ( )
    LvivITCluster.printITCluster ( )
    KyivITCluster.printITCluster ( )


if __name__ == "__main__": main ( )
