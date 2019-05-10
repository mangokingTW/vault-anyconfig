from vault_anyconfig.vault_anyconfig import VaultAnyConfig

# Passthrough mode

# Passthrough mode will also work if it is passed an empty configuration file, allowing administrators to use it without code changes.
config_client = VaultAnyConfig()

# vault_creds_passthrough.yaml is empty, but because passthrough has already be set in the previous step that doesn't actually matter
config_client.auth_from_file("vault_creds_passthrough.yaml")
config = config_client.load("config.yaml")


# Approle

# Kubernetes
