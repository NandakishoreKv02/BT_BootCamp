# Lab 6: Complete EHR System - Expert Capstone

## Architecture
Build a menu-driven system with these modules:

### 1. Patient Module
- add_patient(), search_patient(), update_patient()

### 2. Appointment Module  
- schedule_appointment(), cancel_appointment(), view_schedule()

### 3. Medication Module
- prescribe_medication(), dispense_medication(), check_inventory()

### 4. Reporting Module
- generate_daily_report(), patient_history(), system_statistics()

### 5. Data Persistence
- save_all_data(), load_all_data()

### 6. Main Menu
- Display options, handle user input, call appropriate functions
- Loop until user exits
- Validate all inputs

## Integration Points
- Appointments link to patients (by MRN)
- Medications link to patients
- Reports aggregate data from all modules
- All data persists to JSON files
