from components.custom import *
from data.const import *

def set_default():
    return (None, today, material_options["M"][0], metode_tender_option["M"][0], "",
            ka_option["M"][0], current_year, tpn_option["M"][0], coa_option["M"][0],
            discipline_option["M"][0], eproc_option["M"][0], "", sap_option["M"][0],
            None, None, "", None, None, None, "", "", 0, 0, 0, 0, "", "")

# TODO: LENGKAPI BAGIAN INI
def get_data_index(data, datasimona, index, indexsimona):
    id_val, date_val, material_val, tender_val, item_val, ka_val, rkap_val, tpn_val, coa_val, discipline_val, eproc_val, dur_val, sap_val, user_val, vendor_val, status_val, poreleased_val, eta_val, bast_val, deliv_val, penalty_val, oe_val, pook_val, realization_val, saving_val, other_val, void_val = set_default()
    if datasimona is not None and data is not None:
        # Gunakan data dari data
        id_val = data["ID"][index]
        date_val = data["PR Month"][index]
        material_val = data["Material/Services"][index]
        tender_val = data["Jenis Tender"][index]
        item_val = data["Item"][index]
        ka_val = data["K/A"][index]
        rkap_val = data["RKAP"][index]
        tpn_val = data["TA/Punchlist/Normal"][index]
        coa_val = data["COA"][index]
        discipline_val = data["Discipline"][index]
        eproc_val = data["E-Proc/PaDi/Normal"][index]
        dur_val = data["No. DUR"][index]
        sap_val = data["SAP/Non"][index]
        user_val = data["User Name"][index]
        vendor_val = data["Vendor Name"][index]
        status_val = data["Status"][index]
        poreleased_val = data["PO Released"][index]
        eta_val = data["ETA"][index]
        bast_val = data["BAST"][index]
        deliv_val = data["Delivery Time"][index]
        penalty_val = data["Penalty/N"][index]
        oe_val = data["OE"][index]
        pook_val = data["PO/OK"][index]
        realization_val = data["Realization"][index]
        saving_val = data["Saving"][index]
        other_val = data["Other"][index]
        void_val = data["Status Void"][index]
        return (id_val, date_val, material_val, tender_val, item_val, ka_val, rkap_val,
                tpn_val, coa_val, discipline_val, eproc_val, dur_val, sap_val, user_val,
                vendor_val, status_val, poreleased_val, eta_val, bast_val, deliv_val, 
                penalty_val, oe_val, pook_val, realization_val, saving_val, other_val, void_val)
    elif datasimona is not None and data is None:
        # Gunakan data Simona
        date_val = datasimona["PR Month"][indexsimona]
        material_val = datasimona["Material/Services"][indexsimona]
        # tender_val = datasimona["Status Tender"][indexsimona]
        item_val = datasimona["Item"][indexsimona]
        # ka_val = datasimona["K/A"][indexsimona]
        # rkap_val = datasimona["RKAP"][indexsimona]
        # tpn_val = datasimona["TA/Punchlist/Normal"][indexsimona]
        # coa_val = datasimona["COA"][indexsimona]
        # discipline_val = datasimona["Discipline"][indexsimona]
        # eproc_val = datasimona["E-Proc/PaDi/Normal"][indexsimona]
        # dur_val = datasimona["No. DUR"][indexsimona]
        # sap_val = datasimona["SAP/Non"][indexsimona]
        # user_val = datasimona["User Name"][indexsimona]
        # vendor_val = datasimona["Vendor Name"][indexsimona]
        # status_val = datasimona["Status"][indexsimona]
        # deliv_val = datasimona["Delivery Time"][indexsimona]
        # penalty_val = datasimona["Penalty/N"][indexsimona]
        # oe_val = datasimona["OE"][indexsimona]
        # pook_val = datasimona["PO/OK"][indexsimona]
        # realization_val = datasimona["Realization"][indexsimona]
        # saving_val = datasimona["Saving"][indexsimona]
        # other_val = datasimona["Other"][indexsimona]
        # other2_val = datasimona["Other 2"][indexsimona]
        # file_loc_val = datasimona["File Location"][indexsimona]
        # forecast_val = datasimona["Forecast Realization"][indexsimona]
        # cumulative_val = datasimona["Cumulative FR"][indexsimona]
        # ir_val = datasimona["IR Realization"][indexsimona]
        # a_val = datasimona["A"][indexsimona]
        return (id_val, date_val, material_val, tender_val, item_val, ka_val, rkap_val,
                tpn_val, coa_val, discipline_val, eproc_val, dur_val, sap_val, user_val,
                vendor_val, status_val, poreleased_val, eta_val, bast_val, deliv_val, 
                penalty_val, oe_val, pook_val, realization_val, saving_val, other_val, void_val)
    elif datasimona is None and data is not None:
        # Gunakan data data
        id_val = data["ID"][index]
        date_val = data["PR Month"][index]
        material_val = data["Material/Services"][index]
        tender_val = data["Jenis Tender"][index]
        item_val = data["Item"][index]
        ka_val = data["K/A"][index]
        rkap_val = data["RKAP"][index]
        tpn_val = data["TA/Punchlist/Normal"][index]
        coa_val = data["COA"][index]
        discipline_val = data["Discipline"][index]
        eproc_val = data["E-Proc/PaDi/Normal"][index]
        dur_val = data["No. DUR"][index]
        sap_val = data["SAP/Non"][index]
        user_val = data["User Name"][index]
        vendor_val = data["Vendor Name"][index]
        status_val = data["Status"][index]
        poreleased_val = data["PO Released"][index]
        eta_val = data["ETA"][index]
        bast_val = data["BAST"][index]
        deliv_val = data["Delivery Time"][index]
        penalty_val = data["Penalty/N"][index]
        oe_val = data["OE"][index]
        pook_val = data["PO/OK"][index]
        realization_val = data["Realization"][index]
        saving_val = data["Saving"][index]
        other_val = data["Other"][index]
        void_val = data["Status Void"][index]
        return (id_val, date_val, material_val, tender_val, item_val, ka_val, rkap_val,
                tpn_val, coa_val, discipline_val, eproc_val, dur_val, sap_val, user_val,
                vendor_val, status_val, poreleased_val, eta_val, bast_val, deliv_val, 
                penalty_val, oe_val, pook_val, realization_val, saving_val, other_val, void_val)
    else:
        st.header("INPUT DATA BARU")
        return set_default()
