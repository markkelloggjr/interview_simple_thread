from datetime import datetime

class CityHistory():
    DATE_FORMAT = "%m/%d/%y"

    class CostOfLiving():
        LOW = 1
        HIGH = 2

    def __init__(self, cost_of_living, start_date, end_date):
        self.cost_of_living = cost_of_living

        self.start_date = datetime.strptime(start_date, CityHistory.DATE_FORMAT)
        self.end_date = datetime.strptime(end_date, CityHistory.DATE_FORMAT)


class SetOfProjects():
    def __init__(self, history_data):
        self.histories = [] # CityHistory

        for city_history in history_data:
            self.histories.append(city_history)

    def calculate_reimbursement(self):
        # Work on this after the chorus concert
        pass
























        '''
        
class Project():
    pass

class SequenceOfProjects(Project):
    pass
        '''