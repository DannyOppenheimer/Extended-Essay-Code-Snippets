import math

def RSA_data():
  # arrays that save data from RSA_Data.csv to calculate average time
  rsa_frequency = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  rsa_sum = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
  rsa_ave = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

  # Open file
  with open("RSA/RSA_Data.csv", "r") as f:
    text = f.readlines()

  # For each line, split it into csv columns, and save them to sum and ave arrays
  for line in text:
    column = line.split(",")
    index = int(math.log(int(column[0]), 2))
    rsa_frequency[index] += 1
    rsa_sum[index] += float(column[1].strip("\n"))

  # Divide the two previous arrays to get average
  for i in range(len(rsa_ave)):
    if rsa_frequency[i] != 0:
      rsa_ave[i] = "{:f}".format(rsa_sum[i] / rsa_frequency[i])

  print(rsa_ave)
