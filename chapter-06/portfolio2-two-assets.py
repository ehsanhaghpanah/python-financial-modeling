# %%

#
# Two Assets Portfolio
#
class Asset(object):
     mu: float = 0                 # expected return (reward)
     sigma: float = 0              # risk (standard deviation)
     weight: float = 0

     def __init__(self, m: float, s: float, w: float) -> None:
          self.mu = m
          self.sigma = s
          self.weight = w
          pass

     # expected return of the asset in the portfolio = (mu * weight)
     def reward(self) -> float:
          return self.mu * self.weight

# = Asset =====================================================

class Portfolio(object):

     asset_a: Asset
     asset_b: Asset
     correlation: float            # rho (correlation(AB) = covariance(AB) / (sigma(A) * sigma(B))

     def __init__(self, aa: Asset, ab: Asset, cr: float) -> None:
          if ((aa.weight + ab.weight) != 1):
               raise Exception("portfolio's assets' weights summation is not one")
          self.asset_a = aa
          self.asset_b = ab
          self.correlation = cr
          pass
     
     # Portfolio Return (Rp)
     # Rate of Return (RoR) of Portfolio
     def reward(self) -> float:
          mu_p = (self.asset_a.mu * self.asset_a.weight) + (self.asset_b.mu * self.asset_b.weight)
          return round(mu_p, 4)
     
     def risk(self) -> float:
          sigma_p = (self.asset_a.sigma * self.asset_a.weight) ** 2 + (self.asset_b.sigma * self.asset_b.weight) ** 2
          sigma_p = sigma_p + (2 * self.asset_a.sigma * self.asset_a.weight * self.asset_b.sigma * self.asset_b.weight * self.correlation)
          sigma_p = sigma_p ** 0.5      # sqrt(sigma_p)
          return round(sigma_p, 4)

# = Portfolio =================================================

pr = Portfolio(Asset(0.174, 0.05, 0.5), Asset(0.017, 0.08, 0.5), 0.3)
print(f'portfolio expected return = {pr.reward()}')
print(f'portfolio risk = {pr.risk()}')
