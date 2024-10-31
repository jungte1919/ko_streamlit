import sys
import requests
import os
import warnings
import saspy

warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=ResourceWarning)
warnings.filterwarnings("ignore", category=ImportWarning)

def download_file(url, dst):
    """Helper function to download a file if it does not already exist."""
    if not os.path.exists(dst):
        st.info(f"Downloading file to {dst}...")
        response = requests.get(url)
        response.raise_for_status()  # Check for request errors
        with open(dst, "wb") as file:
            file.write(response.content)
        st.success(f"Downloaded {os.path.basename(dst)} successfully!")
    else:
        st.info(f"File {os.path.basename(dst)} already exists. Skipping download.")

# Set the file paths based on Python version
version = f"{sys.version_info.major}.{sys.version_info.minor}"
base_path = f"/usr/local/lib/python{version}/dist-packages/saspy/java/iomclient/"
os.makedirs(base_path, exist_ok=True)

# Define URLs and destinations
files = {
    "sas.rutil.jar": "https://www.googleapis.com/drive/v3/files/1wQkHbgrcF03hN8CrIFLK4zsqU-ckVRyK?alt=media&key=AIzaSyBfJIzuu9x7AZjgtr0UhbrxNTz0vqbYWv0",
    "sas.rutil.nls.jar": "https://www.googleapis.com/drive/v3/files/1wUiEDOu2UMsW6394MrC0s4D-FHPAlt8o?alt=media&key=AIzaSyBfJIzuu9x7AZjgtr0UhbrxNTz0vqbYWv0",
    "sastpj.rutil.jar": "https://www.googleapis.com/drive/v3/files/1wTOLejKU5UKw61KGu4oT_WM4ZdWOAdqu?alt=media&key=AIzaSyBfJIzuu9x7AZjgtr0UhbrxNTz0vqbYWv0"
}

# Attempt to download each file
for filename, url in files.items():
    dst_path = os.path.join(base_path, filename)
    download_file(url, dst_path)

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
