import red_nosed_reports

def test_is_report_safe():
    safeDecrease = [7, 6, 4, 2, 1]
    unsafeIncrease = [1, 2, 7, 8, 9]
    unsafeDecrease = [9, 7, 6, 2, 1]
    safeIncreaseSecondLevelRemoved = [1, 3, 2, 4, 5]
    safeDecreaseThirdLevelRemoved = [8, 6, 4, 4, 1]
    safeIncrease = [1, 3, 6, 7, 9]

    custom1 = [10, 12, 9, 8, 7]
    custom2 = [10, 8, 12, 14, 16]
    custom3 = [10, 12, 11, 9, 8]
    custom4 = [1, 2, 3, 4, 10]
    custom5 = [1, 2, 3, 4, 1]
    
    assert red_nosed_reports.is_report_safe(safeDecrease)
    assert not red_nosed_reports.is_report_safe(unsafeIncrease)
    assert not red_nosed_reports.is_report_safe(unsafeDecrease)
    assert red_nosed_reports.is_report_safe(safeIncreaseSecondLevelRemoved)
    assert red_nosed_reports.is_report_safe(safeDecreaseThirdLevelRemoved)
    assert red_nosed_reports.is_report_safe(safeIncrease)

    assert red_nosed_reports.is_report_safe(custom1)
    assert red_nosed_reports.is_report_safe(custom2)
    assert red_nosed_reports.is_report_safe(custom3)
    assert red_nosed_reports.is_report_safe(custom4)
    assert red_nosed_reports.is_report_safe(custom5)

def test_is_valid_level():
    validIncrease = red_nosed_reports.get_level_details(6, 9, red_nosed_reports.DIRECTION_INCREASE)
    invalidIncrease = red_nosed_reports.get_level_details(6, 10, red_nosed_reports.DIRECTION_INCREASE)
    validDecrease = red_nosed_reports.get_level_details(6, 3, red_nosed_reports.DIRECTION_DECRESAE)
    invalidDecrease = red_nosed_reports.get_level_details(6, 2, red_nosed_reports.DIRECTION_DECRESAE)
    invalidEquals = red_nosed_reports.get_level_details(4, 4, red_nosed_reports.DIRECTION_INVALID)

    assert validIncrease == (True, red_nosed_reports.DIRECTION_INCREASE)
    assert invalidIncrease == (False, red_nosed_reports.DIRECTION_INVALID)
    assert validDecrease == (True, red_nosed_reports.DIRECTION_DECRESAE)
    assert invalidDecrease == (False, red_nosed_reports.DIRECTION_INVALID)
    assert invalidEquals == (False, red_nosed_reports.DIRECTION_INVALID)


def test_get_direction():
    decreaseDirection = red_nosed_reports.get_direction(7, 4)
    increaseDirection = red_nosed_reports.get_direction(6, 9)
    invalidEqualDirection = red_nosed_reports.get_direction(7, 7)
    invalidDecreaseGretherThanThree = red_nosed_reports.get_direction(6, 2)
    invalidIncreaseGreaterThanThree = red_nosed_reports.get_direction(6, 10)

    assert decreaseDirection == red_nosed_reports.DIRECTION_DECRESAE
    assert increaseDirection == red_nosed_reports.DIRECTION_INCREASE
    assert invalidEqualDirection == red_nosed_reports.DIRECTION_INVALID
    assert invalidDecreaseGretherThanThree == red_nosed_reports.DIRECTION_INVALID
    assert invalidIncreaseGreaterThanThree == red_nosed_reports.DIRECTION_INVALID

def test_safe_report_total(): 
    reports = ["7 6 4 2 1\n",
               "1 2 7 8 9\n", 
               "9 7 6 2 1\n",
               "1 3 2 4 5\n",
               "8 6 4 4 1\n",
               "1 3 6 7 9\n"]

    total = red_nosed_reports.get_safe_report_count(reports)

    assert total == 4

def test_get_safe_report_total_from_input():
    f = open("inputs/red_nosed_reports.txt", "r")
    input = f.readlines()

    total = red_nosed_reports.get_safe_report_count(input)

    f.close

    assert total == 540
