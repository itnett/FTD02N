python
import tpm2_pytss
from tpm2_pytss import *

def create_primary_key(tpm, hierarchy=TPM2_RH_OWNER):
    in_public = TPM2B_PUBLIC(
        publicArea=TPMT_PUBLIC(
            type=TPM2_ALG_RSA,
            nameAlg=TPM2_ALG_SHA256,
            objectAttributes=(TPMA_OBJECT_RESTRICTED | TPMA_OBJECT_DECRYPT | TPMA_OBJECT_FIXEDTPM |
                              TPMA_OBJECT_FIXEDPARENT | TPMA_OBJECT_SENSITIVEDATAORIGIN | TPMA_OBJECT_USERWITHAUTH),
            parameters=TPMU_PUBLIC_PARMS(rsaDetail=TPMS_RSA_PARMS(scheme=TPMT_RSA_SCHEME(scheme=TPM2_ALG_NULL))),
            unique=TPMU_PUBLIC_ID(rsa=TPM2B_PUBLIC_KEY_RSA())
        )
    )
    return tpm.CreatePrimary(hierarchy, in_public, "", "", [TPMS_PCR_SELECTION()])

tpm = TSS2_SysContext()
primary_handle = create_primary_key(tpm)
print("Primary key created with handle:", primary_handle)