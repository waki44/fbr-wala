def calculate_salaried_tax(annual_income: float) -> float:
    """Pakistan Salaried Tax Slabs"""
    if annual_income <= 600000:
        return 0.0
    elif annual_income <= 1200000:
        return (annual_income - 600000) * 0.05
    elif annual_income <= 2200000:
        return 30000 + (annual_income - 1200000) * 0.15
    elif annual_income <= 3200000:
        return 180000 + (annual_income - 2200000) * 0.25
    elif annual_income <= 4100000:
        return 430000 + (annual_income - 3200000) * 0.30
    else:
        return 700000 + (annual_income - 4100000) * 0.35
