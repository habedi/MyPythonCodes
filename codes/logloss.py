import numpy

def logloss(y: numpy.array, y_hat: numpy.array) -> float:
    return -y*numpy.log2(y_hat) - (1-y)*numpy.log2(1-y_hat)

if __name__ == "__main__":
    
  import matplotlib.pyplot as plt
  
  fig = plt.figure()
  
  # if y is all zeros
  y = numpy.zeros(100)
  y_hat = numpy.arange(0, 1, 1/len(y))

  lloss = logloss(y, y_hat)

  ax1 = fig.add_subplot(211)
  ax1.plot(y_hat, lloss)

  # if y is all ones
  y.fill(1)
  lloss = logloss(y, y_hat)

  ax2 = fig.add_subplot(212)
  ax2.plot(y_hat, lloss)

  fig.show()
