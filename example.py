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

print("Data:", convert_data(1024, UnitData.KB, UnitData.MB))
print("Distance:", convert_distance(1, UnitDistance.MI, UnitDistance.KM))
print("Mass:", convert_mass(10, UnitMass.K, UnitMass.P))
print("Temperature:", convert_temperature(32, UnitTemperature.F, UnitTemperature.C))