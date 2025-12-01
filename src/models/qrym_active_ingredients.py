class QRYM_ActiveIngredients:
    def __init__(
        self,
        drug_code=0,
        active_ingredient_code=0,
        ingredient="",
        ingredient_supplied_ind="",
        strength="",
        strength_unit="",
        strength_type="",
        dosage_value="",
        base="",
        dosage_unit="",
        notes="",
        ingredients_f="",
        strength_unit_f="",
        strength_type_f="",
        dosage_unit_f=""
    ):
        self.drug_code = drug_code
        self.active_ingredient_code = active_ingredient_code
        self.ingredient = ingredient
        self.ingredient_supplied_ind = ingredient_supplied_ind
        self.strength = strength
        self.strength_unit = strength_unit
        self.strength_type = strength_type
        self.dosage_value = dosage_value
        self.base = base
        self.dosage_unit = dosage_unit
        self.notes = notes
        self.ingredients_f = ingredients_f
        self.strength_unit_f = strength_unit_f
        self.strength_type_f = strength_type_f
        self.dosage_unit_f = dosage_unit_f