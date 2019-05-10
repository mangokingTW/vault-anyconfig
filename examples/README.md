vault-anyconfig Usage Examples
==============================

This example shows three different authentication configurations of vault-anyconfig by providing three different `vault_creds.yaml` files using a single
`vault.yaml` (Vault configuration) file, a single `example.py` Python script and finally a single `config.yaml` file to be processed with secrets
from Vault.

1. Pass-through mode, which does not use Vault at all. This uses `vault_creds_passthrough.yaml`, which is simply an empty file
2. Approle authentication, which uses the Approle authentication with Vault. This uses `vault_creds_approle.yaml`.
3. Kubernetes authetnication, which uses the Kubernetes authentication method with Vault. This uses `vault_creds_k8s.yaml`.