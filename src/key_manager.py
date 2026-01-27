from Crypto.PublicKey import RSA
from pathlib import Path

KEYS_DIR = Path(__file__).resolve().parent / "keys"
KEYS_DIR.mkdir(parents=True, exist_ok=True)


def generate_rsa_keys() -> None:
    """
    Unconditionally generate a new RSA keypair.

    Use this only when you explicitly want to rotate keys.
    """
    private_key = RSA.generate(2048)
    private_path = KEYS_DIR / "private.pem"
    public_path = KEYS_DIR / "public.pem"

    with open(private_path, "wb") as f:
        f.write(private_key.export_key("PEM"))

    with open(public_path, "wb") as f:
        f.write(private_key.publickey().export_key("PEM"))

    print(f"RSA Keys generated:\n- {private_path}\n- {public_path}")


def ensure_rsa_keys() -> None:
    """
    Ensure RSA keys exist in KEYS_DIR.

    Safe to call on every startup: it only creates keys if missing.
    """
    private_path = KEYS_DIR / "private.pem"
    public_path = KEYS_DIR / "public.pem"

    if private_path.exists() and public_path.exists():
        return

    generate_rsa_keys()


if __name__ == "__main__":
    ensure_rsa_keys()
