python
        # Funksjon for å beregne BMI
        def beregn_bmi(vekt, høyde):
            bmi = vekt / (høyde ** 2)
            return bmi

        vekt = 75
        høyde = 1.75
        bmi = beregn_bmi(vekt, høyde)
        print("Din BMI er:", bmi)