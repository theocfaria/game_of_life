from utils import nextTableState

def testingUnit(initial_table, expected_table):
    if nextTableState(initial_table) == expected_table:
        print('PASSED TEST')
    else:
        print('FAILED THE TEST')
        print("Expected:")
        print(expected_table)
        print("Actual:")
        print(nextTableState(initial_table))