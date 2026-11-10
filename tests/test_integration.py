from src.models import Apartment
from src.manager import Manager
from src.models import Parameters
import json

def test_load_data():
    parameters = Parameters()
    manager = Manager(parameters)
    assert isinstance(manager.apartments, dict)
    assert isinstance(manager.tenants, dict)
    assert isinstance(manager.transfers, list)
    assert isinstance(manager.bills, list)

    for apartment_key, apartment in manager.apartments.items():
        assert isinstance(apartment, Apartment)
        assert apartment.key == apartment_key

def test_all_tenants_from_json_are_in_manager():
    parameters = Parameters()
    manager = Manager(parameters)
    manager.load_data()

    with open("data/tenants.json", encoding="utf-8") as f:
        tenants_json = json.load(f)
    print(tenants_json)
    
    tenant_names = [tenant.name for tenant in manager.tenants.values()]

    for tenant_key, tenant_data in tenants_json.items():
        assert tenant_key in manager.tenants
        assert tenant_data["name"] in tenant_names