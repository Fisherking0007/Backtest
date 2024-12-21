
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Liste des actifs à inclure dans le portefeuille
tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN']

# Téléchargement des données historiques sur 1 an
data = yf.download(tickers, start="2023-01-01", end="2023-12-31")['Adj Close']

# Calcul des rendements quotidiens
returns = data.pct_change().dropna()

# Allocation initiale du portefeuille (égale pour chaque actif)
weights = np.array([0.25, 0.25, 0.25, 0.25])  # 25% pour chaque actif

# Calcul de l’évolution du portefeuille
portfolio_returns = (returns @ weights).cumsum()
portfolio_value = (1 + portfolio_returns) * 100  # Portefeuille initial = 100$

# Visualisation de l’évolution du portefeuille
plt.figure(figsize=(10, 6))
plt.plot(portfolio_value, label="Portfolio")
plt.title("Évolution du portefeuille sur 1 an")
plt.xlabel("Date")
plt.ylabel("Valeur du portefeuille ($)")
plt.legend()
plt.show()

# Analyse des performances
total_return = portfolio_value[-1] - 100  # Gain total
annualized_return = (1 + portfolio_returns[-1]) ** (1 / 1) - 1  # Rendement annualisé
volatility = returns @ weights
sharpe_ratio = annualized_return / volatility.std()

print(f"Rendement total : {total_return:.2f}%")
print(f"Rendement annualisé : {annualized_return:.2f}%")
print(f"Ratio de Sharpe : {sharpe_ratio:.2f}")