# Lab 6 Tasks

## Task 1: Component Integration
- Bring in `SystemConfig` (Singleton).
- Bring in `RiskStrategy` (Strategy).
- Bring in `Subject/Observer` (Observer).
- Bring in `ReportFactory` (Factory).

## Task 2: Build the Orchestrator
- Class `MedGuardSystem`.
- Method `add_patient(self, name, age_category)`.
- Method `process_vitals(self, patient_name, heart_rate)`:
    - Get max threshold from `SystemConfig`.
    - Apply correct `RiskStrategy` based on age.
    - If Risk is "CRITICAL", call `notify()`.

## Task 3: Final Disposition
- Method `close_case(self, patient_name, format_type)`:
    - Use `ReportFactory` to generate a summary.

## Task 4: System Test
- Configure 1 patient.
- Trigger a critical HR.
- Observe the notification.
- Generate a final PDF report.
