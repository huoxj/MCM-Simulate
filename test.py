import numpy as np
import mglearn
import matplotlib.pyplot as plt
import pandas as pd


db_bitcoin = pd.read_csv("database\BCHAIN-MKPRU.csv")
db_gold = pd.read_csv("database\LBMA-GOLD.csv")

date_bitcoin, value_bitcoin = db_bitcoin.values[:, 0], db_bitcoin.values[:, 1]
date_gold, value_gold = db_gold.values[:, 0], db_gold.values[:, 1]

