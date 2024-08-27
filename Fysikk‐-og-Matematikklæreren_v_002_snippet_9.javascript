function genererKodeForTrinket(emne, input) {
    let kode = "";

    switch (emne) {
        case "regneregler":
            const tall1 = input.tall1;
            const operator = input.operator;
            const tall2 = input.tall2;
            kode = `
# Python kode for regneregler
tall1 = ${tall1}
operator =