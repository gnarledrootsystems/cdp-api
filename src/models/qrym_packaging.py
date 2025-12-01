class QRYM_Packaging:
    def __init__(
        self,
        drug_code,
        upc,
        package_size_unit,
        package_type,
        package_size,
        product_information,
        package_size_unit_f,
        package_type_f
    ):
        self.drug_code = drug_code
        self.upc = upc
        self.package_size_unit = package_size_unit
        self.package_type = package_type
        self.package_size = package_size
        self.product_information = product_information
        self.package_size_unit_f = package_size_unit_f
        self.package_type_f = package_type_f