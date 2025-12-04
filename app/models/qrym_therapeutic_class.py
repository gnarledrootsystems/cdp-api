"""

AHFS Data is external to the Canadian Drug Product Database extracts, therefore
it is not included and will not be shown.

https://health-products.canada.ca/dpd-bdpp/info?lang=eng&code=3132#fn3
"""
class QRYM_TherapeuticClass:
    def __init__(
        self,
        drug_code=0,
        tc_atc_number="",
        tc_atc="",
        #tc_ahfs_number="",
        #tc_ahfs="",
        #tc_atc_f="",
        #tc_ahfs_f=""
    ):
        self.drug_code = drug_code
        self.tc_atc_number = tc_atc_number
        self.tc_atc = tc_atc
        #self.tc_ahfs_number = tc_ahfs_number
        #self.tc_ahfs = tc_ahfs
        #self.tc_atc_f = tc_atc_f
        #self.tc_ahfs_f = tc_ahfs_f