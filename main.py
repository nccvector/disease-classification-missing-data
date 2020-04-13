import numpy as np
from pomegranate import *

# Loading and Preparing training data
X = np.genfromtxt("data/traindata.txt", delimiter=" ")
X[X == -1.0] = None
X = X.tolist()

# Loading test data
Y = np.genfromtxt("data/testdata.txt", delimiter=" ")
total = Y.shape[0]

# Defining bayesian network
dunnets = DiscreteDistribution({0: 0.5, 1: 0.25, 2: 0.25}) # 0->None, 1->Mild, 2->Severe
trimono = DiscreteDistribution({1: 0.1, 0: 0.9}) # 0->False, 1->True

# Creating cpt arrays

# Conditional table of sloep has the following columns [trimono, dunnets, sloep, p(sloep)]
sloep_cpt = np.array([[1, 0, 1, 0.03],
                      [1, 0, 0, 0.97],
                      [1, 2, 1, 0.9],
                      [1, 2, 0, 0.1],
                      [1, 1, 1, 0.9],
                      [1, 1, 0, 0.1],
                      [0, 0, 1, 0.03],
                      [0, 0, 0, 0.97],
                      [0, 2, 1, 1.0],
                      [0, 2, 0, 0.0],
                      [0, 1, 1, 1.0],
                      [0, 1, 0, 0.1]])

# Conditional table of forien has the following columns [dunnets, forien, p(forien)]
forien_cpt = np.array([[0, 1, 0.03],
                       [0, 0, 0.97],
                       [2, 1, 0.2],
                       [2, 0, 0.8],
                       [1, 1, 0.8],
                       [1, 0, 0.2]])

# Conditional table of degar has the following columns [dunnets, degar, p(degar)]
degar_cpt = np.array([[0, 1, 0.03],
                      [0, 0, 0.97],
                      [2, 1, 0.8],
                      [2, 0, 0.2],
                      [1, 1, 0.2],
                      [1, 0, 0.8]])

# Creating cpt objects from arrays
sloep = ConditionalProbabilityTable(sloep_cpt, [trimono, dunnets])
forien = ConditionalProbabilityTable(forien_cpt, [dunnets])
degar = ConditionalProbabilityTable(degar_cpt, [dunnets])

# Defining nodes
T = Node(trimono, name="trimono")
D = Node(dunnets, name="dunnet")
S = Node(sloep, name="sloep")
F = Node(forien, name="forien")
De = Node(degar, name="degar")

# Creating model
model = None
model = BayesianNetwork("Dunnets syndrome problem")

# Joint probability is going to be of the following form [sloep, forien, degar, trimono, dunnets]
model.add_states(S, F, De, T, D)

# Connecting edges
model.add_edge(T, S)
model.add_edge(D, S)
model.add_edge(D, F)
model.add_edge(D, De)
model.bake()

# Fitting network using EM
model.fit(X)

# Evaluating model performance on test data
correct = 0
for i in range(0, total):
    # Chances of not dunnets, mild dunnets and severe dunnets
    result = [model.probability([[Y[i][0], Y[i][1], Y[i][2], Y[i][3], 0]]), # Query for not-dunnets syndrome
        model.probability([[Y[i][0], Y[i][1], Y[i][2], Y[i][3], 1]]), # Query for mild-dunnets syndrome
        model.probability([[Y[i][0], Y[i][1], Y[i][2], Y[i][3], 2]])] # Query for severe-dunnets syndrome

    # Maximum likelihood index
    result = result.index(max(result))

    # Mark if correct
    if result == Y[i][-1]:
        correct += 1

accuracy = correct/total * 100
print("Accuracy", accuracy)