import click
import csv
import os
from pathlib import Path
from typing import Union
from contextlib import suppress
from src.models import QRYM_ActiveIngredients, QRYM_VeterinarySpecies, QRYM_Biosimilars, QRYM_Companies, QRYM_DrugProduct, QRYM_Form, QRYM_InactiveProducts, QRYM_Packaging, QRYM_PharmaceuticalSTD, QRYM_Route, QRYM_Schedule, QRYM_Status, QRYM_TherapeuticClass
import src.utilities.memsnap as memsnap
import src.utilities.colors as colors

"""
Importer Command
[poetry run quart importer]
"""
def importer(app):
    @click.option("--import-date", 'import_date')
    @app.cli.command("importer")
    def importer(import_date):
        if import_date:
            print("Running importer for Date {import_date}")
            process_marketed_drug_files(import_date)
            process_approved_drug_files(import_date)
            process_cancelled_drug_files(import_date)
            process_dormant_drug_files(import_date)
        else:
            print("No Import Date was passed.")
            
    return app

"""
Grab the project root based on the location of "pyproject.toml"

Returns: Project root Path object
"""
def get_project_root():
    current = os.path.abspath(os.path.dirname(__file__))
    while True:
        if os.path.exists(os.path.join(current, 'pyproject.toml')):
            return Path(current)
        
        parent = os.path.dirname(current)
        if parent == current:
            raise Exception("Error finding project root and pyproject.toml")
        
        current = parent
            
"""
Return all files as a list within the given directory

date_dir: The Directory of the Export, i.e: "2025-11-03"
product_dir: The child folders, i.e: "allfiles|allfiles_*"

Returns: List of Path objects
"""
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
    
# allfiles
"""

"""    
def process_marketed_drug_files(import_date):
    files = get_file_names(import_date, "allfiles")
    for file in files:
        qrym_model = map_file_to_qrym_model(str(file))
        
        qrym_model_list = []
        if qrym_model:
            qrym_model_list = build_qrym_model_list(file, qrym_model)
            
        if qrym_model_list:
            # Now we have a list of all the QRYM Model objects.
            # We need to start converting them to MongoDB-Compatible
            # JSON and inserting them.
            # The insertions should be done in batches to save on requests
            # to the MongoDB instance, especially since some of the files
            # are 15k lines.
            # Batching of maybe 250 Rows would be sufficient.
            # TODO:
            # 1. Setup MongoDB Config and Functions for Insert|Batch Insert
            # 2. Create function for chunking the lists and batch inserting
            print('todo')
            
"""
TODO: All the separate functions below for processing can be reduced into one
where I pass in the "allfiles|allfiles_*" as a parameter.
"""
# allfiles_ia
def process_cancelled_drug_files(import_date):
    files = get_file_names(import_date, "allfiles_ia")
    for file in files:
        map_file_to_qrym_model(str(file))

# allfiles_ap
def process_approved_drug_files(import_date):
    files = get_file_names(import_date, "allfiles_ap")
    for file in files:
        map_file_to_qrym_model(str(file))

# allfiles_dr
def process_dormant_drug_files(import_date):
    files = get_file_names(import_date, "allfiles_dr")
    for file in files:
        map_file_to_qrym_model(str(file))

"""
Maps the given file to the correct model and runs the model list builder
with the file and correct model to use.

Returns: QRYM Model
"""
def map_file_to_qrym_model(file):
    qrym_model = None
    
    if "biosimilar" in file:
        qrym_model = QRYM_Biosimilars()
    elif "comp" in file:
        qrym_model = QRYM_Companies()
    elif "drug" in file:
        qrym_model = QRYM_DrugProduct()
    elif "form" in file:
        qrym_model = QRYM_Form()
    elif "ingred" in file:
        qrym_model = QRYM_ActiveIngredients()
    elif "package" in file:
        qrym_model = QRYM_Packaging()
    elif "pharm" in file:
        qrym_model = QRYM_PharmaceuticalSTD()
    elif "route" in file:
        qrym_model = QRYM_Route()
    elif "schedule" in file:
        qrym_model = QRYM_Schedule()
    elif "status" in file:
        qrym_model = QRYM_Status()
    elif "ther" in file:
        qrym_model = QRYM_TherapeuticClass()
    elif "vet" in file:
        qrym_model = QRYM_VeterinarySpecies()
    
    return qrym_model
    
"""
Given the QRYM Model, this function loads the passed csv file and builds a
list of the appropriate QRYM Model.

Returns: List<QRYM Model>
"""
def build_qrym_model_list(file, model: Union[
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
    memsnap.start()
    
    print(f"File: {file}")
    print(f"Model: {model}")
    
    qrym_model_list = []
    with open(file, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        if isinstance(model, QRYM_ActiveIngredients):
            for row in reader:
                qrym_model = QRYM_ActiveIngredients(
                    int(row[0]), int(row[1]), row[2], row[3], row[4], row[5], row[6], row[7],
                    row[8], row[9], row[10], row[11], row[12], row[13], row[14]
                )
                qrym_model_list.append(qrym_model)
        elif isinstance(model, QRYM_Biosimilars):
            for row in reader:
                qrym_model = QRYM_Biosimilars(
                    int(row[0]), row[1], row[2], int(row[3])
                )
                qrym_model_list.append(qrym_model)
        elif isinstance(model, QRYM_Companies):
            for row in reader:
                qrym_model = QRYM_Companies(
                    int(row[0]), row[1], int(row[2]), row[3], row[4], row[5], row[6], row[7],
                    row[8], row[9], row[10], row[11], row[12], row[13], row[14],
                    row[15], row[16], row[17]
                )
                qrym_model_list.append(qrym_model)
        elif isinstance(model, QRYM_DrugProduct):
            for row in reader:
                qrym_model = QRYM_DrugProduct(
                    int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6], row[7],
                    row[8], row[9], row[10], row[11], row[12], row[13]
                )
                qrym_model_list.append(qrym_model)
        elif isinstance(model, QRYM_Form):
            for row in reader:
                qrym_model = QRYM_Form(
                    int(row[0]), int(row[1]), row[2], row[3]
                )
                qrym_model_list.append(qrym_model)
        elif isinstance(model, QRYM_InactiveProducts):
            for row in reader:
                qrym_model = QRYM_InactiveProducts(
                    int(row[0]), row[1], row[2], row[3], row[4]
                )
                qrym_model_list.append(qrym_model)
        elif isinstance(model, QRYM_Packaging):
            for row in reader:
                qrym_model = QRYM_Packaging(
                    int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6], row[7]
                )
                qrym_model_list.append(qrym_model)
        elif isinstance(model, QRYM_PharmaceuticalSTD):
            for row in reader:
                qrym_model = QRYM_PharmaceuticalSTD(
                    int(row[0]), row[1]
                )
                qrym_model_list.append(qrym_model)
        elif isinstance(model, QRYM_Route):
            for row in reader:
                qrym_model = QRYM_Route(
                    int(row[0]), int(row[1]), row[2], row[3]
                )
                qrym_model_list.append(qrym_model)
        elif isinstance(model, QRYM_Schedule):
            for row in reader:
                qrym_model = QRYM_Schedule(
                    int(row[0]), row[1], row[2]
                )
                qrym_model_list.append(qrym_model)
        elif isinstance(model, QRYM_Status):
            for row in reader:
                qrym_model = QRYM_Status(
                    int(row[0]), row[1], row[2], row[3], row[4], row[5], row[6]
                )
                qrym_model_list.append(qrym_model)
        elif isinstance(model, QRYM_TherapeuticClass):
            for row in reader:
                qrym_model = QRYM_TherapeuticClass(
                    int(row[0]), row[1], row[2]
                )
                qrym_model_list.append(qrym_model)
        elif isinstance(model, QRYM_VeterinarySpecies):
            for row in reader:
                qrym_model = QRYM_VeterinarySpecies(
                    int(row[0]), row[1], row[2], row[3]
                )
                qrym_model_list.append(qrym_model)
    
    memsnap.stop(build_qrym_model_list.__name__)
    
    return qrym_model_list                
            
            
        
        
        


def load_files(date):
    return True