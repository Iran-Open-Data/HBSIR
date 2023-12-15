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
