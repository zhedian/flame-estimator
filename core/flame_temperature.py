import cantera as ct

def estimate_flame_temperature(fuel, oxidizer, phi):
    gas = ct.Solution("gri30.yaml")
    gas.set_equivalence_ratio(phi, fuel=fuel, oxidizer=oxidizer)
    gas.TP = 300, ct.one_atm

    gas.set_equivalence_ratio(phi, fuel=fuel, oxidizer="O2:1, N2:3.76")
    gas.equilibrate("HP")  # 等焓等压平衡燃烧
    flame_temp = gas.T

    return flame_temp
