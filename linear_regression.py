import numpy as np
import matplotlib.pyplot as plt

#Regression function
def estimation_b0_b1(x, y):
  n = np.size(x)

  # x and y acerage values
  mean_x, mean_y = np.mean(x), np.mean(y)

  #summation of xy and xx
  sumatoria_xy = np.sum((x - mean_x)*(y - mean_y))
  sumatoria_xx = np.sum(x*(x - mean_x))

  #Regression coeficients
  b_1 = sumatoria_xy / sumatoria_xx
  b_0 = mean_y - b_1*mean_x

  return b_0, b_1

#Graph function
def plot_regression(x, y, b):

  plt.scatter(x, y, color = "b", marker = "o", s = 30)

  y_pred = b[0] + b[1]*x
  plt.plot(x, y_pred, color = "g")
  plt.xlabel("x")
  plt.ylabel("y")
  
  plt.show()

#Main code
def main():
  #Dataset
  x = np.array([1, 2, 3, 4, 5])
  y = np.array([2, 3, 5, 6, 5])

  #b_0 and b_1
  b = estimation_b0_b1(x, y)
  print(f"Los valores de b_0 = {b[0]} y b_1 = {b[1]}")

  #Regression plot
  plot_regression(x, y, b)

if __name__ == "__main__":
  main()
  
