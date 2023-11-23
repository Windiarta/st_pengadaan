from components.custom import *
from data.const import *

def get_data_index(data, index):
    if data is not None:
        id_val = data["ID"][index]
        date_val = data["PR Month"][index]
        material_val = data["Material/Services"][index]
        tender_val = data["Status Tender"][index]
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
        deliv_val = data["Delivery Time"][index]
        penalty_val = data["Penalty/N"][index]
        oe_val = data["OE"][index]
        pook_val = data["PO/OK"][index]
        realization_val = data["Realization"][index]
        saving_val = data["Saving"][index]
        other_val = data["Other"][index]
        other2_val = data["Other 2"][index]
        file_loc_val = data["File Location"][index]
        forecast_val = data["Forecast Realization"][index]
        cumulative_val = data["Cumulative FR"][index]
        ir_val = data["IR Realization"][index]
        a_val = data["A"][index]
        return (id_val, date_val, material_val, tender_val, item_val, ka_val, rkap_val,
                tpn_val, coa_val, discipline_val, eproc_val, dur_val, sap_val, user_val,
                vendor_val, status_val, deliv_val, penalty_val, oe_val, pook_val,
                realization_val, saving_val, other_val, other2_val, file_loc_val,
                forecast_val, cumulative_val, ir_val, a_val)
    else:
        st.warning("Tidak ada data, Isi untuk menginput data baru")
        return (None, today, material_options["M"][0], metode_tender_option["M"][0], "",
                ka_option["M"][0], current_year, tpn_option["M"][0], coa_option["M"][0],
                discipline_option["M"][0], eproc_option["M"][0], "", sap_option["M"][0],
                user_option["M"][0], 'NONE', "", "", "", 0, 0, 0, 0, "", "", "", "", "", "", "")
