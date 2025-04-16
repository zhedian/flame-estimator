import cantera as ct

def estimate_flame_temperature(fuel, oxidizer, phi):
    gas = ct.Solution("gri30.yaml")
    gas.set_equivalence_ratio(phi, fuel=fuel, oxidizer=oxidizer)
    gas.TP = 300, ct.one_atm

    flame = ct.IdealGasConstPressureReactor(gas)
    sim = ct.ReactorNet([flame])
    sim.advance(1.0)
    return flame.thermo.T
