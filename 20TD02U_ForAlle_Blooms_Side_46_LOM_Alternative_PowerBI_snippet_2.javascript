function calculateBudgetVariance() {
     var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheetByName("Økonomistyring");
     var lastRow = sheet.getLastRow();

     for (var i = 2; i <= lastRow; i++) {
       var inntekter = sheet.getRange(i, 2).getValue();
       var utgifter = sheet.getRange(i, 3).getValue();
       var budsjett = sheet.getRange(i, 4).getValue();
       var avvik = inntekter - utgifter - budsjett;
       sheet.getRange(i, 5).setValue(avvik);
     }
   }