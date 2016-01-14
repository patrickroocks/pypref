"""User interfaces of pypref"""

# -*- coding: utf-8 -*-


"""
  The pypref-module
  
  Sykline Computation and Database Preferences in Python
  
  Preference evaluation algorithm is implemented in Cython
  
"""


# Sample data
# ===========

import os
import pandas as pd

def get_mtcars():
  """
  Returns the mtcars data set from R
  """
  return(pd.read_csv(os.path.join(os.path.split(__file__)[0], "mtcars.csv"), index_col = 0))
    
    
# Module files
# ============

from . import prefclasses
from .prefclasses import *

from . import btg
from .btg import *




  