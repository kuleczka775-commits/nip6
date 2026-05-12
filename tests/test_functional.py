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


def test_get_debtors():
    manager = Manager(Parameters())
    
    debtors = manager.get_debtors('apart-polanka', 2025, 1)

    assert debtors == []
    assert len(debtors) == 0
    

def test_check_deposits():
    manager = Manager(Parameters())
    
    deposit_status = manager.check_deposits()
    
    assert deposit_status is False