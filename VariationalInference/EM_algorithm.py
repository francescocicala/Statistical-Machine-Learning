import numpy as np
from utilities import extract




if __name__ == '__main__':

  mu = np.asarray([[1], [100], [300]])
  S = np.asarray([[[1]], [[1]], [[1]]])
  print(gaussian_mixture(20, mu, S, [0.3, 0.3, 0.4]))
