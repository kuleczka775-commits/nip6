from src.manager import Manager
from src.models import Parameters

def test_total_due_pln():
    manager = Manager(Parameters())

    apartment_settlement = manager.get_settlement('apart-polanka', 2025, 1)
    tenants_settlements = manager.create_tenants_settlements(apartment_settlement)
    tenant_settlement_total = 0
    for tenant_settlement in tenants_settlements:
        tenant_settlement_total += tenant_settlement.total_due_pln 
    
    assert apartment_settlement.total_due_pln == tenant_settlement_total
