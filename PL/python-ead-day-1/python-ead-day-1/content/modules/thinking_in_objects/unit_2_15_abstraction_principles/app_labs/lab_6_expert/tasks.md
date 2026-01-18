# Lab 6 Tasks

## Task 1: Abstract Scanner
- Define `Scanner(ABC)` with abstract methods `capture_image()` and `get_cost()`.
- Implement `MRIScanner` (cost: 1200), `CTScanner` (cost: 800), `UltrasoundScanner` (cost: 300).

## Task 2: SRP Components
- `ImagingOrder(order_id, patient_id, scanner_type)`: Data storage only.
- `CostEstimator`: Has a method `estimate(scanner)` that calls `scanner.get_cost()`.
- `ReportGenerator`: Has a method `generate(scanner_type, patient_id, image_data, cost)` that returns a formatted string.

## Task 3: Workflow Orchestration
- Create `DiagnosticWorkflow` class.
- Implement `execute_scan(order)`:
  - Map `order.scanner_type` to the correct scanner class.
  - Instantiate the scanner.
  - Call `capture_image()`.
  - Use `CostEstimator` to get the cost.
  - Use `ReportGenerator` to create the final report.
  - Return the report.

## Task 4: Integration
In `main()`:
1. Create an order for an MRI scan.
2. Create a `DiagnosticWorkflow` instance.
3. Execute the scan and print the report.
