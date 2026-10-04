import numpy as np
from scipy.stats import norm


def generate_gbm_paths(S0, r, sigma, T, num_simulations, num_steps):
    dt = T / num_steps
    Z = np.random.standard_normal((num_simulations, num_steps))
    drift = (r - 0.5 *sigma**2) * dt
    diffusion = sigma * np.sqrt(dt) * Z
    log_returns = drift + diffusion
    cumulative_returns = np.cumsum(log_returns, axis=1)
    price_paths = S0 *np.exp(cumulative_returns)
    return price_paths



def price_european_call_mc(paths, K, r, T):
    ST = paths[:, -1]
    payoffs = np.maximum(ST - K, 0)
    call_price = np.exp(-r * T) * np.mean(payoffs)
    std_error = (np.exp(-r * T) * np.std(payoffs)) / np.sqrt(len(ST))
    return call_price, std_error



def price_antithetic_call_mc(paths, K, r, T):
    ST = paths[:, -1]
    payoffs = np.maximum(ST - K, 0)
    
    # 1. Split into the original half and the mirrored (-Z) half
    half_sims = len(ST) // 2
    payoffs_orig = payoffs[:half_sims]
    payoffs_anti = payoffs[half_sims:]
    
    # 2. Average each mirrored pair together FIRST
    paired_payoffs = (payoffs_orig + payoffs_anti) / 2.0
    
    # 3. Calculate price and correct standard error across pairs
    call_price = np.exp(-r * T) * np.mean(paired_payoffs)
    std_error = (np.exp(-r * T) * np.std(paired_payoffs)) / np.sqrt(half_sims)
    
    return call_price, std_error



def black_scholes_call(S0, K, r, sigma, T):
    d1 = (np.log(S0 / K) + T * (r + 0.5 * sigma**2)) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    call_price = S0 * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    return call_price



def generate_antithetic_gbm_paths(S0, r, sigma, T, num_simulations, num_steps):
    dt = T / num_steps
    half_sims = num_simulations // 2
    Z = np.random.standard_normal((half_sims, num_steps))
    Z_antithetic = np.vstack((Z, -Z))
    drift = (r - 0.5 * sigma**2) * dt
    diffusion = sigma * np.sqrt(dt) * Z_antithetic
    log_returns = drift + diffusion
    cumulative_returns = np.cumsum(log_returns, axis=1)
    price_paths = S0 * np.exp(cumulative_returns)
    return price_paths


if __name__ == "__main__":
    S0 = 100.0 # Starting stcok price
    K = 100.0  # Strike price
    r = 0.05 # Risk-Free rate
    sigma = 0.2 # Annual Volatility
    T = 1.0 # Time Horizon
    num_steps = 252 # Number of trading days in a year
    num_simulations = 100000 # Number of hypithetical future paths to generate



    paths_standard = generate_gbm_paths(
        S0, r, sigma, T, num_simulations, num_steps
    )
    mc_price, mc_stderr = price_european_call_mc(paths_standard, K, r, T)


    paths_antithetic = generate_antithetic_gbm_paths(
        S0, r, sigma, T, num_simulations, num_steps
    )
    anti_price, anti_stderr = price_antithetic_call_mc(paths_antithetic, K, r, T)


    bs_price = black_scholes_call(S0, K, r, sigma, T)


    print("==================================================")
    print(" MONTE CARLO OPTION PRICING & BENCHMARK ENGINE")
    print("==================================================")
    print(f"Black-Scholes Price (Absolute Truth) : {bs_price:.4f}\n")

    print(f"Standard Monte Carlo Price        : {mc_price:.4f}")
    print(f"Standard Monte Carlo Std Error    : {mc_stderr:.5f}\n")
    
    print(f"Antithetic Monte Carlo Price      : {anti_price:.4f}")
    print(f"Antithetic Monte Carlo Std Error  : {anti_stderr:.5f}\n")
    
    stderr_reduction = ((mc_stderr - anti_stderr) / mc_stderr) * 100
    print(f"Variance Reduction Achieved      : {stderr_reduction:.2f}%")
    print("==================================================")