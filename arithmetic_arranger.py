def arithmetic_arranger(problems, show_total=False):

  arranged_line1 = ''
  arranged_line2 = ''
  arranged_line3 = ''
  arranged_line4 = ''
  space1 = " "
  space4 = "    "
  dash = "-"
  
  if len(problems) > 5:
    return "Error: Too many problems."
  
  else:
    for problem in problems:

      operands = problem.split()
      problem_total = 0
      
      problem_digits1, problem_op, problem_digits2 = operands[0], operands[1], operands[2]
      
      if problem_op not in ['+', '-']:
        return "Error: Operator must be '+' or '-'."

      if not problem_digits1.isdigit() or not problem_digits2.isdigit():
        return "Error: Numbers must only contain digits."

      if len(problem_digits1) > 4 or len(problem_digits2) > 4:
        return "Error: Numbers cannot be more than four digits."

      if problem_op == "+":
        problem_total = str(int(problem_digits1) + int(problem_digits2))

      if problem_op == "-":
        problem_total = str(int(problem_digits1) - int(problem_digits2))
      
      if not arranged_line1 == '':
        arranged_line1 = arranged_line1 + space4
      if not arranged_line2 == '':
          arranged_line2 = arranged_line2 + space4
      if not arranged_line3 == '':
            arranged_line3 = arranged_line3 + space4
      if not arranged_line4 == '':
        arranged_line4 = arranged_line4 + space4
        
      digit_width = max(len(problem_digits1), len(problem_digits2))
        
      arranged_line1 = arranged_line1 + (space1 * (2 + (digit_width - len(problem_digits1)))) + problem_digits1

      arranged_line2 = arranged_line2 + problem_op + (space1 * (1 + (digit_width - len(problem_digits2)))) + problem_digits2

      arranged_line3 = arranged_line3 + dash * (digit_width + 2)
      
      arranged_line4 = arranged_line4 + space1 * ((digit_width + 2) - len(problem_total)) + problem_total

    
    arranged_problems = arranged_line1 + '\n' + arranged_line2 + '\n' + arranged_line3

    
    if show_total==True:
      arranged_problems = arranged_problems + '\n' + arranged_line4

    return arranged_problems
