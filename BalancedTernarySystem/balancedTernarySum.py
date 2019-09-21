input = "+--+0+-++(+)-++++---+"

firstNumber = ""
operator = ""
secondNumber = ""

def processInput():
  global firstNumber, operator, secondNumber

  firstNumber = input.split("(")[0]
  operator = input.split("(")[1].split(")")[0]
  secondNumber = input.split("(")[1].split(")")[1]
  lenDiff = len(firstNumber) - len(secondNumber)

  if lenDiff > 0:
    for i in range(lenDiff):
      secondNumber = "0" + secondNumber
  else:
    for i in range(lenDiff):
      firstNumber = "0" + firstNumber

  print(firstNumber.rjust(20))
  print(operator.rjust(20))
  print(secondNumber.rjust(20))
  print()

  firstNumber = firstNumber[::-1]
  secondNumber = secondNumber[::-1]

def sum():
  global firstNumber, operator, secondNumber
  currentSum, carryOver = "", "0"

  while (not isZero(secondNumber)):
    for (first, second) in zip(firstNumber, secondNumber):
      result, carry = digitSum(first, second)
      currentSum += result
      carryOver += carry

    firstNumber = currentSum
    secondNumber = carryOver
    currentSum = ""
    carryOver = "0"

  return firstNumber[::-1]

def digitSum(first, second):
  if (first == "0"):
    return second, "0"
  if (second == "0"):
    return first, "0"
  if (first != second):
    return "0", "0"
  if (first == "-"):
    return "+", "-"
  if (first == "+"):
    return "-", "+"

def negate(number):
  negativeNumber = ""
  for digit in number:
    if digit == "+":
      negativeNumber += "-"
    elif digit == "-":
      negativeNumber += "+"
    else:
      negativeNumber += "0"
  return negativeNumber

def isZero(number):
  return number == (len(number) * "0")

processInput()

if (operator == "-"):
  secondNumber = negate(secondNumber)

print("Result:".ljust(10) + sum().lstrip("0").rjust(10))
