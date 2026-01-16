import project



def test_example_one():
    example_data = [project.CityHistory(project.CityHistory.CostOfLiving.LOW, "10/1/24", "10/4/24")]

    example_one = project.SetOfProjects(example_data)
    print(f"Example One Reimburse:   ${example_one.calculate_reimbursement()}")
    
    

def test_example_two():
    example_data = [project.CityHistory(project.CityHistory.CostOfLiving.LOW, "10/1/24", "10/1/24"),
                    project.CityHistory(project.CityHistory.CostOfLiving.HIGH, "10/2/24", "10/6/24"),
                    project.CityHistory(project.CityHistory.CostOfLiving.LOW, "10/6/24", "10/9/24"),]

    example_two = project.SetOfProjects(example_data)
    print(f"Example Two Reimburse:   ${example_two.calculate_reimbursement()}")
    
def test_example_three():
    example_data = [project.CityHistory(project.CityHistory.CostOfLiving.LOW, "9/30/24", "10/3/24"),
                    project.CityHistory(project.CityHistory.CostOfLiving.HIGH, "10/5/24", "10/7/24"),
                    project.CityHistory(project.CityHistory.CostOfLiving.HIGH, "10/8/24", "10/8/24"),]

    example_three = project.SetOfProjects(example_data)
    print(f"Example Three Reimburse: ${example_three.calculate_reimbursement()}")

def test_example_four():
    example_data = [project.CityHistory(project.CityHistory.CostOfLiving.LOW, "10/1/24", "10/1/24"),
                    project.CityHistory(project.CityHistory.CostOfLiving.LOW, "10/1/24", "10/1/24"),
                    project.CityHistory(project.CityHistory.CostOfLiving.HIGH, "10/2/24", "10/3/24"),
                    project.CityHistory(project.CityHistory.CostOfLiving.HIGH, "10/2/24", "10/6/24"),]

    example_four = project.SetOfProjects(example_data)
    print(f"Example Four Reimburse:  ${example_four.calculate_reimbursement()}")




if __name__ == "__main__":
    test_example_one()
    test_example_two()
    test_example_three()
    test_example_four()