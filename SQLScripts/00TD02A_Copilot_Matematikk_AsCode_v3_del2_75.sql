sql
SELECT decimal_value, 
       BIN(decimal_value) AS binary_value, 
       HEX(decimal_value) AS hexadecimal_value 
FROM DecimalValues;