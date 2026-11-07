"""Project-wide constants and paths. Edit here, not inside notebooks.

Project: pretrial detention decisions in New York (SE_POL 408, Fall 2026).
Data: NY State Office of Court Administration, Pretrial Release Data (public CSV,
one file per arraignment year). https://www.nycourts.gov/division-technology-court-research/pretrial-release-data
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA_RAW = ROOT / "data" / "raw"            # NYS for Web <year>.csv (not tracked)
DATA_PROCESSED = ROOT / "data" / "processed"
DATA_EXTERNAL = ROOT / "data" / "external"
REPORTS = ROOT / "reports"                  # aggregate tables only (tracked)
FIGURES = REPORTS / "figures"
MODELS_DIR = ROOT / "models"                # not tracked
DOCS = ROOT / "docs"

RAW_FILE_PATTERN = "NYS for Web {year}.csv"

# ---- Years and split (plan v1, section 4.1; to confirm at team meeting) ----
YEARS = [2021, 2022, 2023]
TRAIN_YEARS = [2021, 2022]
VALID_YEAR = 2023
TEST_YEAR = None            # 2024 if downloaded, else a hold-out slice of 2023 [to decide]
SPLIT_COL = "split"

# ---- Sample (plan v1, section 2.2) ----
NYC_COUNTIES = ["New York", "Kings", "Bronx", "Queens", "Richmond"]
MAIN_SCOPE = "nyc"          # "nyc" (main analysis) or "state"
RELEASE_COL = "Release Decision at Arraign"
RELEASE_DISPOSED = "Disposed at arraign"    # no detention decision -> dropped
RELEASE_UNKNOWN = "Unknown"                 # dropped
RELEASE_DETAIN = ["Remanded", "Bail-set"]   # Q1 outcome = 1
RELEASE_FREE = ["ROR", "Nonmonetary release"]

# ---- Outcomes ----
ID_COL = "Internal_Case_ID"
TARGET_Q1 = "y_detain"      # bail set or remanded at arraignment
TARGET_Q3 = "y_warrant"     # bench warrant ordered between arraignment and disposition (released only)
TARGET_Q3_ALT = "y_rearrest"  # any pretrial rearrest (supplementary; not a legal criterion in NY)
RELEASED_COL = "released"   # ROR / NMR / bail posted at arraignment

# ---- Feature groups (plan v1, section 3.1) ----
FEATURES_CASE = [
    "Top_Severity_at_Arraign", "Top_Charge_Weight_at_Arraign",
    "Top_Charge_at_Arraign_Violent_Felony_Ind", "Top_Arraign_Attempt_Indicator",
    "Arraign Charge Category", "Hate_Crime_Ind", "Arrest_Type",
    "prior_vfo_cnt", "prior_nonvfo_cnt", "prior_misd_cnt",
    "pend_vfo", "pend_nonvfo", "pend_misd", "supervision",
    "Age_at_Arrest", "Gender",
]
FEATURES_PLACE = ["County_Name", "Court_Type", "Representation_Type"]
FEATURES_JUDGE = ["judge_id"]               # anonymised in src/sample.py
FEATURE_SETS = {
    "CASE": FEATURES_CASE,
    "CASE_PLACE": FEATURES_CASE + FEATURES_PLACE,
    "CASE_PLACE_JUDGE": FEATURES_CASE + FEATURES_PLACE + FEATURES_JUDGE,
}
CATEGORICAL = ["Top_Severity_at_Arraign", "Top_Charge_Weight_at_Arraign",
               "Top_Charge_at_Arraign_Violent_Felony_Ind", "Top_Arraign_Attempt_Indicator",
               "Arraign Charge Category", "Hate_Crime_Ind", "Arrest_Type", "Gender",
               "County_Name", "Court_Type", "Representation_Type", "judge_id"]
FAIRNESS_GROUPS = ["Race", "Ethnicity", "age_group"]   # never features

# Columns determined after the arraignment decision: never features (plan v1, 3.2)
LEAKAGE_BLOCKLIST = [
    "Release Decision at Arraign", "Remanded_to_Jail_at_Arraign", "ROR_at_Arraign",
    "Bail_Set_and_Posted_at_Arraign", "Bail_Set_and_Not_Posted_at_Arraign", "NMR_at_Arraign",
    "Pretrial_Supervision_at_Arraign", "Contact_Pretrial_Service_Agency", "Electronic_Monitoring",
    "Travel_Restrictions", "Passport_Surrender", "No_Firearms_or_Weapons", "Maintain_Employment",
    "Maintain_Housing", "Maintain_School", "Placement_in_Mandatory_Program", "Removal_to_Hospital",
    "Obey_Order_of_Protection", "Obey_Court_Conditions-Family_Offense", "Other_NMR", "Order_of_Protection",
    "First_Bail_Set_Cash", "First_Bail_Set_Credit", "First_Insurance_Company_Bail_Bond",
    "First_Secured_Surety_Bond", "First_Secured_App_Bond", "First_Unsecured_Surety_Bond",
    "First_Unsecured_App_Bond", "First_Partially_Secured_Surety_Bond", "Partially_Secured_Surety_Bond_Perc",
    "First_Partially_Secured_App_Bond", "Partially_Secured_App_Bond_Perc", "Bail_Made_Indicator",
    "Warrant_Ordered_btw_Arraign_and_Dispo", "First_Bench_Warrant_Month", "First_Bench_Warrant_Year",
    "Non_Stayed_WO", "Num_of_Stayed_WO", "Num_of_ROW", "Docket_Status", "Disposition_Type",
    "Disposition_Detail", "Dismissal_Reason", "Disposition_Date", "Most_Severe_Sentence",
    "Top_Conviction_Law", "Top_Conviction_Article_Section", "Top_Conviction_Attempt_Indicator",
    "Top_Charge_at_Conviction", "Top_Charge_Severity_at_Conviction", "Top_Charge_Weight_at_Conviction",
    "Top_Charge_at_Conviction_Violent_Felony_Ind", "Days_Arraign_Remand_First_Released",
    "Known_Days_in_Custody", "Days_Arraign_Bail_Set_to_First_Posted", "Days_Arraign_Bail_Set_to_First_Release",
    "Days_Arraign_to_Dispo", "MinImpTopConvDays", "MaxImpTopConvDays",
    "App_Count_Arraign_to_Dispo_Released", "App_Count_Arraign_to_Dispo_Detained",
    "App_Count_Arraign_to_Dispo_Total", "Def_Attended_Sched_Pretrials",
    "rearrest", "rearrest_180", "rearrest_date", "rearrest_firearm", "rearrest_date_firearm",
    "Race", "Ethnicity", "Judge_Name",       # race/ethnicity: fairness only; judge: use judge_id
    "y_detain", "y_warrant", "y_rearrest", "released",
]

# ---- Modeling / evaluation ----
RANDOM_STATE = 408
MIN_JUDGE_CASES = 100       # judges with fewer cases pooled into "other" [to decide]
MIN_GROUP_N = 100           # fairness cells below this are not reported
