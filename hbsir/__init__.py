"""HBSIR - Tools for working with Household Budget Survey of Iran

This package provides a set of tools to facilitate working with the 
Household Budget Survey of Iran (HBSIR) data.
  
It allows easy access to standardized survey tables across multiple 
years. It also enables data enrichment, aggregation, analysis and 
visualization.

"""

from .api import (
    load_table,
    load_knowledge,
    add_attribute,
    add_classification,
    add_weight,
    setup,
    setup_config,
)

from . import calculate

__all__ = [
    "load_table",
    "load_knowledge",
    "add_attribute",
    "add_classification",
    "add_weight",
    "setup",
    "setup_config",
    "calculate",
]
