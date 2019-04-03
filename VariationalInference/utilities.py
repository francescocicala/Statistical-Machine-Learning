import numpy as np

def extract(probabilities, N=1):
  extractions = []
  for i in range(N):

    u = np.random.uniform()

    sum = probabilities[0]
    for i in range(len(probabilities)):
      if u < sum:
        extractions.append(i)
        break
      sum += probabilities[i+1]
  print(np.asarray(extractions))
  return np.asarray(extractions)


def gaussian_mixture(N, mu, S, pi):
  extractions = []
  indices = extract(pi, N)
  for i in range(N):
    index = indices[i]
    print("{}) Indice: {}".format(i, index))
    print("Mu: {}\nS: {}".format(mu[index], S[index]))
    extractions.append(np.random.multivariate_normal(mu[index], S[index]))
  return np.asarray(extractions)
    

if __name__ == '__main__':
