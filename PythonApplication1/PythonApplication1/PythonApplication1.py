import numpy as np
import pandas as pd
import matplotlib as plt
import Quandl

class security:

    def __init__(self, name, ticker):
        self.name = name
        self.ticker = ticker
        print("New security has been created.")

spx = security("S&P 500","SPX Index")