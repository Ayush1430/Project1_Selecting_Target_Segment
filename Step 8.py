import numpy as np
# Assuming x and y are lists or numpy arrays
x = np.array(x)
y = np.array(y)
# Assuming wx and wy are weights
wx = np.array(wx)
wy = np.array(wy)

# Calculate the decision matrix
decision_matrix = np.dot(x, wx) + np.dot(y, wy)

# You can also create a DataFrame if needed
import pandas as pd

decision_matrix_df = pd.DataFrame({'Decision_Matrix': decision_matrix})

# Print the decision matrix
print(decision_matrix_df)
