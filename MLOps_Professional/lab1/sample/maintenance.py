# maitnenace test business logic
# Lab-1: Add pressure parameter
def test_maintenance(temperature:int, pressure:int) -> str:
    """_summary_

    Parameters
    ----------
    temperature : int
        test parameter for temperature sensor readings

    pressure : int
        test parameter for pressure sensor readings

    Returns
    -------
    str
        'Approved' or 'Denied' based on temperature/pressure readings
    """
    maintenance_status = 'Needs Maintenance' if temperature > 50 or pressure > 2000 else 'No Maintenance Required'
    
    return maintenance_status
