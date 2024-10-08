python
# Power Query script for å laste inn og formatere data i Power BI
let
    Kilde = Excel.Workbook(File.Contents("C:\Data\regnskap.xlsx"), null, true),
    Data = Kilde{[Name="ØkonomiskeData"]}[Data],
    EndretType = Table.TransformColumnTypes(Data,{{"Måned", type text}, {"Inntekter", Int64.Type}, {"Utgifter", Int64.Type}})
in
    EndretType