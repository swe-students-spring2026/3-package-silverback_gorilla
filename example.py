# Option 1:
# from unit_convert import *

# Option 2: explicit import
from unit_convert import (
    convert_data,
    convert_distance,
    convert_mass,
    convert_temperature,
    UnitData,
    UnitDistance,
    UnitMass,
    UnitTemperature,
)

print(convert_data(1024, UnitData.KB, UnitData.MB))
print(convert_distance(1, UnitDistance.MI, UnitDistance.KM))
print(convert_mass(10, UnitMass.K, UnitMass.P))
print(convert_temperature(32, UnitTemperature.F, UnitTemperature.C))