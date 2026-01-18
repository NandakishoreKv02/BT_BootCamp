"""
Starter Code - Reset
"""
'\nLab 1: Patient Vital Signs Monitor - Basic Properties\nSolution Code\n'

class VitalSigns:
    """
    Stores and provides read-only access to patient vital signs.
    
    Attributes:
        patient_id (str): Unique patient identifier
        temperature (float): Body temperature in Celsius
        heart_rate (int): Heart rate in beats per minute
        bp_systolic (int): Systolic blood pressure
        bp_diastolic (int): Diastolic blood pressure
    """

    def __init__(self, patient_id: str, temperature: float, heart_rate: int, bp_systolic: int, bp_diastolic: int):
        """
        Initialize vital signs for a patient.
        
        Args:
            patient_id: Unique patient identifier
            temperature: Body temperature in Celsius
            heart_rate: Heart rate in BPM
            bp_systolic: Systolic blood pressure
            bp_diastolic: Diastolic blood pressure
        """
        # TODO: Implement logic
        pass

    @property
    def patient_id(self) -> str:
        """Get patient ID (read-only)."""
        # TODO: Implement logic
        pass

    @property
    def temperature(self) -> float:
        """Get temperature in Celsius."""
        # TODO: Implement logic
        pass

    @property
    def heart_rate(self) -> int:
        """Get heart rate in BPM."""
        # TODO: Implement logic
        pass

    @property
    def blood_pressure(self) -> str:
        """Get formatted blood pressure string."""
        # TODO: Implement logic
        pass

    def __str__(self) -> str:
        """String representation of vital signs."""
        # TODO: Implement logic
        pass
if __name__ == '__main__':
    vitals = VitalSigns('P12345', 37.2, 72, 120, 80)
    print(f'Patient ID: {vitals.patient_id}')
    print(f'Temperature: {vitals.temperature}C')
    print(f'Heart Rate: {vitals.heart_rate} bpm')
    print(f'Blood Pressure: {vitals.blood_pressure}')
    print(vitals)