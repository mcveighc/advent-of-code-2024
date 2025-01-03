import re

def get_enabled_mul_instances(input):
    splitInput = input.split("don't()")
    sanitizedInput = splitInput[0]

    for i in range(1, len(splitInput)):
        disabledText = splitInput[i]
        nestedEnabled = disabledText.split("do()")

        for e in range(1, len(nestedEnabled)):
            sanitizedInput += nestedEnabled[e]
    
    regex = "mul[\(]\d+[,]\d+[\)]"
    instances = re.findall(regex, sanitizedInput)
    return instances
 

def parse_mul(input):
    splitInput = input.split(",")
    leftSide = splitInput[0]
    rightSide = splitInput[1]

    leftNum = int(leftSide[4:])
    rightNum = int(rightSide[:-1])

    return (leftNum, rightNum)

def calc_mul_total(input):
    result = 0
    instances = get_enabled_mul_instances(input)
    for i in instances:
        mul = parse_mul(i)
        result += mul[0] * mul[1]
    
    return result