DIRECTION_INCREASE = "INC"
DIRECTION_DECRESAE = "DEC"
DIRECTION_INVALID = "INVALID"

def is_report_safe(nums, isToleranceCheck = False):
    numsLength = len(nums)
    isValid = True
    prevDirection = ""

    i=1
    while i < numsLength and isValid:
        levelDetails = get_level_details(nums[i-1], nums[i], prevDirection)
        isValid = levelDetails[0]

        if not isValid and not isToleranceCheck:
            removedElementCopy = nums.copy()
            removedElementCopy.pop(i)
            isSafeWithRemovedElement = is_report_safe(removedElementCopy, True)

            removedPreviousElementCopy = nums.copy()
            removedPreviousElementCopy.pop(i-1)
            isSafeWithRemovedPreviousElement = is_report_safe(removedPreviousElementCopy, True)

            removedTwoPreviousElementsCopy = nums.copy()
            twoPrevIndex = 0 if i - 2 < 0 else i - 2
            removedTwoPreviousElementsCopy.pop(twoPrevIndex)
            isSafeWithRemovedTwoPreviousElement = is_report_safe(removedTwoPreviousElementsCopy, True)
           

            return isSafeWithRemovedElement or isSafeWithRemovedPreviousElement or isSafeWithRemovedTwoPreviousElement

        prevDirection = levelDetails[1]
        i+=1

    return isValid
    
def get_level_details(x, y, prevDirection):
    direction = get_direction(x, y)
    isValid = (prevDirection == "") or (direction != DIRECTION_INVALID and direction == prevDirection)

    return (isValid, direction)
    
def get_direction(prev, curr):
    direction = ""
    diff = prev - curr

    if diff > 0 and diff <= 3 :
        direction = DIRECTION_DECRESAE
    elif diff < 0 and diff >= -3:
        direction = DIRECTION_INCREASE
    else:
        direction = DIRECTION_INVALID
    
    return direction

def get_safe_report_count(reports):
    safe_count = 0

    report_to_level_func = lambda report: [int(x) for x in report.split(" ") ]
    for i in reports:
        santized_report = i.replace("\n", "")
        nums = report_to_level_func(santized_report)

        if is_report_safe(nums):
            safe_count += 1

    return safe_count
