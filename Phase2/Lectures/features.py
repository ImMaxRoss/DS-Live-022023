import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.preprocessing import PolynomialFeatures, StandardScaler
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm
from scipy import stats

wine = pd.read_csv('data/wine.csv')

wine.head(10)


# Use the .corr() DataFrame method to find out about the
# correlation values between all pairs of variables!