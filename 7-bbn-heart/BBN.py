from bayespy.nodes import Categorical, Mixture
from bayespy.inference import VB
import numpy as np

TRUE, FALSE = 1, 0

def _or(p_false, p_true):
    return np.take([p_false, p_true], [[FALSE, TRUE], [TRUE, TRUE]], axis = 0)

A = Categorical([0.5, 0.5])

T = Mixture(A, Categorical, [[0.99, 0.01], [0.8, 0.2]])

S = Categorical([0.5, 0.5])

L = Mixture(S, Categorical, [[0.98, 0.02], [0.75, 0.25]])

B = Mixture(S, Categorical, [[0.97, 0.03], [0.70, 0.30]])

X = Mixture(T, Mixture, L, Categorical, _or([0.96, 0.04], [0.115, 0.885]))

D = Mixture(B, Mixture, X, Categorical, _or([0.115, 0.885], [0.04, 0.96]))

T.observe(TRUE)
S.observe(FALSE)

B.observe(TRUE)

Q = VB(A, T, S, L, B, X, D)
Q.update(repeat=100)

print("P(asia): ", A.get_moments()[0][TRUE])
print("P(tuberculosis): ", T.get_moments()[0][TRUE])
print("P(smoking): ", S.get_moments()[0][TRUE])
print("P(lung): ", L.get_moments()[0][TRUE])
print("P(bronchitis): ", B.get_moments()[0][TRUE])
print("P(xray): ", X.get_moments()[0][TRUE])
print("P(dyspnea): ", D.get_moments()[0][TRUE])