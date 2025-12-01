class QRYM_Status:
    def __init__(
        self,
        drug_code,
        current_status_flag,
        status,
        history_date,
        status_f,
        lot_number,
        expiration_date
    ):
        self.drug_code = drug_code
        self.current_status_flag = current_status_flag
        self.status = status
        self.history_date = history_date
        self.status_f = status_f
        self.lot_number = lot_number
        self.expiration_date = expiration_date