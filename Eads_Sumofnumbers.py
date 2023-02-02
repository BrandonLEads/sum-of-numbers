#Programming exercise 6-5

def main():
  # Declare variables
  line = ''
  total = 0.0
  number = 0.0

  

  #opening file to read the series of intergers
  infile = open('c:/Users/Bose2/Documents/CIS 115/U6/numbers.txt', 'r')
  #reading a string from the file
  for line in infile:
    number = float(line)
    #total equals total which is 0. Then we are adding the number to it.
    total=total+number

  #close file
  infile.close()

  #Display the total of the numbers in the file
  print('Total: ', total)

#Call the main function
main()