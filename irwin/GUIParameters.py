class GUIParameters:
    TemperatureSliderMin = 0.0
    TemperatureSliderMax = 500.0  # Kelvin
    TemperatureLineEditAccuracy = 2
    TemperatureSliderMin = TemperatureSliderMin ** TemperatureLineEditAccuracy  # These calculations for correct
    TemperatureSliderMax = TemperatureSliderMax ** TemperatureLineEditAccuracy

    DonorEnergySliderMin = 0.0
    DonorEnergySliderMax = 5.0  # electron-Volt
    DonorEnergyLineEditAccuracy = 2
    DonorEnergySliderMin = DonorEnergySliderMin ** DonorEnergyLineEditAccuracy  # These calculations for correct
    DonorEnergySliderMax = DonorEnergySliderMax ** DonorEnergyLineEditAccuracy

    AcceptorEnergySliderMin = 0.0
    AcceptorEnergySliderMax = 5.0  # electron-Volt
    AcceptorEnergyLineEditAccuracy = 2
    AcceptorEnergySliderMin = AcceptorEnergySliderMin ** AcceptorEnergyLineEditAccuracy  # These calculations for correct
    AcceptorEnergySliderMax = AcceptorEnergySliderMax ** AcceptorEnergyLineEditAccuracy
