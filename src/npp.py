import xarray as xr


class Miami:
    """Miami model for Net Primary Productivity (NPP)."""
    
    def __init__(self, a=3000, b=1.315, c=0.119, d=3000, e=-0.00064):
        """Return a parameterized Miami model for NPP."""
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        
    def precipitation(self, mean_annual_precipitation):
        """Return the NPP based on mean annual precipitation"""
        return self.d * (1 - xr.ufuncs.exp(self.e * mean_annual_precipitation))
    
    def temperature(self, mean_annual_temperature):
        """Return the NPP based on mean annual temperature"""
        return self.a / (1 + xr.ufuncs.exp(self.b - self.c * mean_annual_temperature))
    
    def __call__(self, mean_annual_temperature, mean_annual_precipitation):
        """Return the NPP"""
        return xr.ufuncs.minimum(
            self.temperature(mean_annual_temperature),
            self.precipitation(mean_annual_precipitation)
        )
