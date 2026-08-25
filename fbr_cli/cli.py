import typer
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from core.slabs import calculate_salaried_tax
from core.reconciler import reconcile_wealth

app = typer.Typer(help="FBR Pakistan Tax Filing CLI Assistant")
console = Console()

@app.command()
def start():
    console.print(Panel.fit("[bold green]ðŸ‡µðŸ‡° FBR-WALA: Tax & Wealth Filing Assistant[/bold green]"))

    # Inputs
    annual_income = typer.prompt("Annual Salary Income (PKR)", type=float)
    tax_deducted_salary = typer.prompt("Tax already deducted by Employer (PKR)", default=0.0, type=float)
    mobile_tax = typer.prompt("Advance Tax on Mobile Bills (Section 236)", default=0.0, type=float)
    vehicle_tax = typer.prompt("Vehicle Token/Purchase Advance Tax", default=0.0, type=float)
    
    console.print("\n[bold yellow]--- Wealth Statement Details ---[/bold yellow]")
    opening_wealth = typer.prompt("Opening Wealth (Previous Year Closing)", default=0.0, type=float)
    annual_expenses = typer.prompt("Total Personal/Household Expenses for the Year", default=0.0, type=float)
    closing_assets = typer.prompt("Total Current Assets (Bank balance, Property, Gold, etc.)", type=float)

    # Calculation
    gross_tax = calculate_salaried_tax(annual_income)
    total_wht = tax_deducted_salary + mobile_tax + vehicle_tax
    net_tax_payable = gross_tax - total_wht
    
    reconciliation = reconcile_wealth(
        opening_wealth=opening_wealth,
        net_income=annual_income,
        expenses=annual_expenses,
        closing_assets=closing_assets
    )

    # Output Table
    table = Table(title="Tax Calculation Summary", show_header=True, header_style="bold magenta")
    table.add_column("Particulars", style="dim")
    table.add_column("Amount (PKR)", justify="right")
    table.add_column("IRIS Code", justify="center")

    table.add_row("Total Income (Salary)", f"{annual_income:,.2f}", "Code 1000")
    table.add_row("Computed Tax Liability", f"{gross_tax:,.2f}", "Code 9200")
    table.add_row("Adjustable Taxes (WHT Paid)", f"{total_wht:,.2f}", "Code 92100")
    
    if net_tax_payable >= 0:
        table.add_row("[bold red]Net Tax Payable[/bold red]", f"[bold red]{net_tax_payable:,.2f}[/bold red]", "Admitted Tax")
    else:
        table.add_row("[bold green]Refundable Tax[/bold green]", f"[bold green]{abs(net_tax_payable):,.2f}[/bold green]", "Refund")

    console.print("\n", table)

    # Wealth Result
    if reconciliation["is_balanced"]:
        console.print("\n[bold green]âœ” Wealth Statement Reconciled Successfully (Difference = 0 PKR)[/bold green]")
    else:
        diff = reconciliation['difference']
        console.print(f"\n[bold red]âœ– Unreconciled Difference: {diff:,.2f} PKR[/bold red]")
        console.print("[dim]Note: IRIS portal par submit karne ke liye difference 0 hona zaroori hai.[/dim]")
