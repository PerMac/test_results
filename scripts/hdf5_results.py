from tables import *


class Particle(IsDescription):
    """
    This class describes the structure used to save results. Each field here
    will be a column in the results table and the type of object it will held
    is also defined.
    """
    name = StringCol(16)   # 16-character String
    idnumber  = Int64Col()      # Signed 64-bit integer
    ADCcount  = UInt16Col()     # Unsigned short integer
    TDCcount  = UInt8Col()      # unsigned byte
    grid_i    = Int32Col()      # 32-bit integer
    grid_j    = Int32Col()      # 32-bit integer
    pressure  = Float32Col()    # float  (single-precision)
    energy    = Float64Col()    # double (double-precision)