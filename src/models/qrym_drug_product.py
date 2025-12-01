class QRYM_DrugProduct:
    def __init__(
        self,
        drug_code=0,
        product_categorization="",
        drug_class="",
        drug_identification_number="",
        brand_name="",
        descriptor="",
        pediatric_flag="",
        accession_number="",
        number_of_ais="",
        last_update_date="",
        ai_group_no="",
        class_f="",
        brand_name_f="",
        descriptor_f=""
    ):
        self.drug_code = drug_code
        self.product_categorization = product_categorization
        self.drug_class = drug_class
        self.drug_identification_number = drug_identification_number
        self.brand_name = brand_name
        self.descriptor = descriptor
        self.pediatric_flag = pediatric_flag
        self.accession_number = accession_number
        self.number_of_ais = number_of_ais
        self.last_update_date = last_update_date
        self.ai_group_no = ai_group_no
        self.class_f = class_f
        self.brand_name_f = brand_name_f
        self.descriptor_f = descriptor_f
        