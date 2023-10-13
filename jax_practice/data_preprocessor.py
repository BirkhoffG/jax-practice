# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/00_data_preprocessor.ipynb.

# %% ../nbs/00_data_preprocessor.ipynb 2
from __future__ import annotations
import jax
import jax.numpy as jnp
import numpy as np

# %% auto 0
__all__ = ['DataPreprocessor', 'MinMaxScaler', 'OneHotEncoder', 'Feature', 'FeaturesList']

# %% ../nbs/00_data_preprocessor.ipynb 4
class DataPreprocessor:
    
    def fit(self, xs, y=None):
        """Fit the preprocessor with `xs` and `y`."""
        raise NotImplementedError
    
    def transform(self, xs):
        """Transform `xs`."""
        raise NotImplementedError
    
    def fit_transform(self, xs, y=None):
        """Fit the preprocessor with `xs` and `y`, then transform `xs`."""
        self.fit(xs, y)
        return self.transform(xs)
    
    def inverse_transform(self, xs):
        """Inverse transform `xs`."""
        raise NotImplementedError


# %% ../nbs/00_data_preprocessor.ipynb 5
def _check_xs(xs: np.ndarray, name: str):
    """Check if `xs` is a 1D array with shape (n_samples,) or a 2D array with shape (n_samples, 1)."""
    if xs.ndim > 2 or (xs.ndim == 2 and xs.shape[1] != 1):
        raise ValueError(f"`{name}` only supports array with a single feature, but got shape={xs.shape}.")

# %% ../nbs/00_data_preprocessor.ipynb 6
class MinMaxScaler(DataPreprocessor):         
    def fit(self, xs, y=None):
        _check_xs(xs, name="MinMaxScaler")
        self.min_ = xs.min(axis=0)
        self.max_ = xs.max(axis=0)
        return self
    
    def transform(self, xs):
        return (xs - self.min_) / (self.max_ - self.min_)
    
    def inverse_transform(self, xs):
        return xs * (self.max_ - self.min_) + self.min_

# %% ../nbs/00_data_preprocessor.ipynb 8
class OneHotEncoder(DataPreprocessor):
    """One-hot encoder for a single categorical feature."""
    
    def fit(self, xs, y=None):
        """Fit the OneHotEncoder with `xs`."""
        ...

    def transform(self, xs):
        """Transform `xs`."""
        ...

    def inverse_transform(self, xs):
        """Inverse transform `xs`."""
        ...

# %% ../nbs/00_data_preprocessor.ipynb 10
class Feature:
    def __init__(
        self,
        name: str,
        data: np.ndarray,
        preprocessor: DataPreprocessor = None,
    ):
        self.name = name
        self.data = data
        self.preprocessor = preprocessor

    def transform(self, xs):
        ...

    def inverse_transform(self, xs):
        ...

# %% ../nbs/00_data_preprocessor.ipynb 11
class FeaturesList:
    def __init__(self, features: list[Feature]):
        ...

    def transform(self, xs):
        ...

    def inverse_transform(self, xs):
        ...
