# ruleid: manicode.ssrf.cloud-metadata-hardcoded-python
requests.get("http://169.254.169.254/latest/meta-data/")

# ruleid: manicode.ssrf.cloud-metadata-url-construction-python
metadata_url = "http://metadata.google.internal/computeMetadata/v1/"
requests.get(metadata_url)

# ruleid: manicode.ssrf.dangerous-protocol-scheme-python
requests.get("file:///etc/passwd")

# ruleid: manicode.ssrf.dangerous-protocol-variable-python
dangerous_url = "gopher://127.0.0.1:11211/_stats"
httpx.get(dangerous_url)

# ok: manicode.ssrf.cloud-metadata-hardcoded-python
requests.get("https://api.example.com/profile")

