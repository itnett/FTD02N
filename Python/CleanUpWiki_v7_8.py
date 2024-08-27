python
import os

github_pat = os.environ.get('GITHUB_PAT')
if not github_pat:
    raise EnvironmentError("GITHUB_PAT miljøvariabelen er ikke satt.")