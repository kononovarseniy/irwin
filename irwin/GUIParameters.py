class GUIParameters:
    TemperatureCalcConstant = 100
    TemperatureSliderMin = 0.0
    TemperatureSliderMax = 500.0  # Kelvin
    TemperatureLineEditAccuracy = 2
    TemperatureSliderMin = TemperatureSliderMin * TemperatureCalcConstant  # These calculations for correct
    TemperatureSliderMax = TemperatureSliderMax * TemperatureCalcConstant

    DonorEnergyCalcConstant = 10000
    DonorEnergySliderMin = 0.0
    DonorEnergySliderMax = 2.0  # electron-Volt
    DonorEnergyLineEditAccuracy = 2
    DonorEnergySliderMin = DonorEnergySliderMin * DonorEnergyCalcConstant
    DonorEnergySliderMax = DonorEnergySliderMax * DonorEnergyCalcConstant



    AcceptorEnergyCalcConstant = 10000
    AcceptorEnergySliderMin = 0.0
    AcceptorEnergySliderMax = 1.0  # electron-Volt
    AcceptorEnergyLineEditAccuracy = 2
    AcceptorEnergySliderMin = AcceptorEnergySliderMin * AcceptorEnergyCalcConstant
    AcceptorEnergySliderMax = AcceptorEnergySliderMax * AcceptorEnergyCalcConstant


    AcceptorConcentrationCalcConstant = 100
    AcceptorConcentrationSliderMin = 1.0 * AcceptorConcentrationCalcConstant
    AcceptorConcentrationSliderMax = 9.0 * AcceptorConcentrationCalcConstant  # ХЗ зачем нужна такая константа (10)
    AcceptorConcentrationLineEditAccuracy = 2


    DonorConcentrationCalcConstant = 100
    DonorConcentrationSliderMin = 1.0 * DonorConcentrationCalcConstant
    DonorConcentrationSliderMax = 9.0 * DonorConcentrationCalcConstant  # ХЗ зачем нужна такая константа (10)
    DonorConcentrationLineEditAccuracy = 2


