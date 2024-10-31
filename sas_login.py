import kolabpy

def sas_login(id, password, server):
    """
    Log in to SAS using kolabpy and return the session object.
    
    Parameters:
    - id (str): User ID
    - password (str): User password
    - server (str): Server name
    
    Returns:
    - SAS session object if successful, else raises an exception.
    """
    try:
        sas = kolabpy.SASLogin(id, password, 'oda', server)
        kolabpy.SASMagic(sas, 'oda')
        return sas
    except Exception as e:
        raise RuntimeError(f"Login failed: {e}")
