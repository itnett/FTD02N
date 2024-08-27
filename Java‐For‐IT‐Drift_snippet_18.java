try {
    int resultat = 10 / 0; // Dette vil kaste et ArithmeticException
} catch (ArithmeticException e) {
    System.out.println("Feil: Du kan ikke dele på null.");
} finally {
    System.out.println("Denne koden kjøres alltid.");
}