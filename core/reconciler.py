def reconcile_wealth(opening_wealth: float, net_income: float, expenses: float, closing_assets: float) -> dict:
    """Formula: Closing Wealth = Opening Wealth + Inflows - Outflows"""
    expected_closing = opening_wealth + net_income - expenses
    difference = closing_assets - expected_closing
    
    return {
        "expected_closing": expected_closing,
        "actual_closing": closing_assets,
        "difference": difference,
        "is_balanced": abs(difference) < 1.0
    }
