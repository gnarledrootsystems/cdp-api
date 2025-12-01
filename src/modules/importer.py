import click
import csv
import os
from pathlib import Path
from typing import Union
from src.models import QRYM_ActiveIngredients, QRYM_VeterinarySpecies, QRYM_Biosimilars, QRYM_Companies, QRYM_DrugProduct, QRYM_Form, QRYM_InactiveProducts, QRYM_Packaging, QRYM_PharmaceuticalSTD, QRYM_Route, QRYM_Schedule, QRYM_Status, QRYM_TherapeuticClass

def importer(app):
    # @click.option("--my-option")
    @app.cli.command("importer")
    def importer():
        print("Running importer...")
        process_marketed_drug_files()
    return app

def get_project_root():
    current = os.path.abspath(os.path.dirname(__file__))
    while True:
        if os.path.exists(os.path.join(current, 'pyproject.toml')):
            return Path(current)
        
        parent = os.path.dirname(current)
        if parent == current:
            raise Exception("Error finding project root and pyproject.toml")
        
        current = parent
            

def get_file_names(date_dir, product_dir):
    drug_file_directory = Path(get_project_root() / "import_files")
    
    files = []
    
    try:
        path = Path(drug_file_directory / date_dir / product_dir)
            
        for entry in path.iterdir():
            if entry.is_file():
                files.append(entry)
        
    except Exception as e:
        print(f"Error getting file names: {e}")
        
    return files
    
    
    
    for file in files:
        with open(file, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print(row)
                
        break
    
# allfiles    
def process_marketed_drug_files():
    files = get_file_names("2025-11-03", "allfiles")
    
    for file in files:
        process_file_by_name(str(file))
        
    return True

# allfiles_ia
def process_cancelled_drug_files():
    files = get_file_names("2025-11-03", "allfiles_ia")
    return True

# allfiles_ap
def process_approved_drug_files():
    files = get_file_names("2025-11-03", "allfiles_ap")
    return True

# allfiles_dr
def process_dormant_drug_files():
    files = get_file_names("2025-11-03", "allfiles_dr")
    return True

def process_file_by_name(file):
    print(file)
    if "biosimilar" in file:
        print("Test")
    elif "comp" in file:
        print("Test")
    elif "drug" in file:
        print("Test")
    elif "form" in file:
        print("Test")
    elif "ingred" in file:
        print("Building Model List for Ingred")
        test = QRYM_ActiveIngredients()
        build_model_list(file, test)
        print("Test")
    elif "package" in file:
        print("Test")
    elif "pharm" in file:
        print("Test")
    elif "route" in file:
        print("Test")
    elif "schedule" in file:
        print("Test")
    elif "ther" in file:
        print("Test")
    elif "vet" in file:
        print("Test")
    
def build_model_list(file, model: Union[
    QRYM_ActiveIngredients,
    QRYM_VeterinarySpecies,
    QRYM_Biosimilars,
    QRYM_Companies,
    QRYM_DrugProduct,
    QRYM_Form,
    QRYM_InactiveProducts,
    QRYM_Packaging,
    QRYM_PharmaceuticalSTD,
    QRYM_Route,
    QRYM_Schedule,
    QRYM_Status,
    QRYM_TherapeuticClass
]):
    print(f"File: {file}")
    print(f"Model: {model}")
    if isinstance(model, QRYM_ActiveIngredients):
        print("Found case")
        with open(file, 'r', newline='') as csvfile:
            print("File opened..")
            reader = csv.reader(csvfile)
            for row in reader:
                print(row)
                model = QRYM_ActiveIngredients(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6],
                    row[7],
                    row[8],
                    row[9],
                    row[10],
                    row[11],
                    row[12],
                    row[13],
                    row[14],
                )
                for key, value in vars(model).items():
                    print(f"{key}: {value}")
                
                break
                    
            
            
        
        
        


def load_files(date):
    return True