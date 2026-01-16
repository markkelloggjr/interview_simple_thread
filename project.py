from datetime import datetime, timedelta

class HistoryDateAndValue():
    def __init__(self, date):
        self.date
        self.reimbursement = None

class CityHistory():
    DATE_FORMAT = "%m/%d/%y"

    class CostOfLiving():
        LOW = 1
        HIGH = 2

    class Status():
        START = 0
        NOT_REIMBURSED = 1
        TRAVELING = 2
        WORKING = 3

    def __init__(self, cost_of_living, start_date, end_date):
        self.cost_of_living = cost_of_living

        self.start_date = datetime.strptime(start_date, CityHistory.DATE_FORMAT)
        self.end_date = datetime.strptime(end_date, CityHistory.DATE_FORMAT)

    def _is_date_within_city_history(self, date):
        if date >= self.start_date and date <= self.end_date:
            return True
        return False

    def _get_reimbursement_value(self, status):
        value = 0

        if self.cost_of_living == CityHistory.CostOfLiving.HIGH:
            if status == CityHistory.Status.TRAVELING:
                value = 55
            if status == CityHistory.Status.WORKING:
                value = 85
        elif self.cost_of_living == CityHistory.CostOfLiving.LOW:
            if status == CityHistory.Status.TRAVELING:
                value = 45
            if status == CityHistory.Status.WORKING:
                value = 75

        return value



class SetOfProjects():
    def __init__(self, history_data):
        self.histories = history_data
    
    def _generate_dates_from_date_range(self, start_date, end_date):
        days = int((end_date - start_date).days) + 1
        for day in range(days):
            yield start_date + timedelta(day)

    def _build_reimbursement_value(self, start_date, end_date):
        active_status = CityHistory.Status.START
        total = 0

        for date in self._generate_dates_from_date_range(start_date, end_date):           
            # track the status so it can be used to calculate the reimbursement value
            histories_to_pick_from_to_reimburse = []
            for history in self.histories:
                if history._is_date_within_city_history(date):
                    histories_to_pick_from_to_reimburse.append(history)

            ##### Do the look ahead. increment the date and see if it is also tracked
            ##### if not, this is traveling

            if len(histories_to_pick_from_to_reimburse) > 0:
                # find out what happened the next day.
                
                look_ahead_histories = []
                for history in self.histories:
                    if history._is_date_within_city_history(date+timedelta(days=1)):
                        look_ahead_histories.append(history)
                
                # assuming at least one history today
                if active_status == CityHistory.Status.START:
                    # start of project set
                    active_status = CityHistory.Status.TRAVELING
                elif active_status == CityHistory.Status.NOT_REIMBURSED:
                    # yesterday was mid set skip day, so we are traveling back
                    active_status = CityHistory.Status.TRAVELING
                elif active_status == CityHistory.Status.TRAVELING:
                    # yesterday we were traveling so we may be working or traveling today
                    active_status = CityHistory.Status.TRAVELING
                    if len(look_ahead_histories) > 0:
                        active_status = CityHistory.Status.WORKING
                elif active_status == CityHistory.Status.WORKING:
                    # yesterday we were working so we may be working or traveling today
                    active_status = CityHistory.Status.TRAVELING
                    if len(look_ahead_histories) > 0:
                        active_status = CityHistory.Status.WORKING
            else:
                # assuming no histories today
                active_status = CityHistory.Status.NOT_REIMBURSED
                
            ##### Finished the look ahead, now use the result of the state machine.
            #####
                        

            value_to_add = 0
            for history in histories_to_pick_from_to_reimburse:
                # Could optimize here and throw out the lists if no longer in bounds, but the lists are so small its not worth it
                value_to_add = 0
                new_value = history._get_reimbursement_value(active_status)
                if new_value >= value_to_add: # this is a shortcut to pick the HIGH city if on the same as a LOW city
                    value_to_add = new_value

            total += value_to_add

        return total

    def _get_date_range(self):
        # find the earliest date and the latest date in our histories
        begining_date = datetime.now()
        end_date = datetime.min

        for history in self.histories:
            if history.start_date < begining_date:
                begining_date = history.start_date

            if history.end_date > end_date:
                end_date = history.end_date

        return (begining_date, end_date)

    def calculate_reimbursement(self):
        date_range = self._get_date_range()
        return self._build_reimbursement_value(date_range[0], date_range[1])
