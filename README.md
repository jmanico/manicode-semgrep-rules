# Manicode Semgrep Rules

Custom Semgrep rules that go **deep** where stock Semgrep goes wide.

These rules target areas where default Semgrep coverage is shallow or missing entirely:

- **AI/LLM Security** — prompt injection, model poisoning, unsafe deserialization of model outputs
- **Modern Supply Chain** — dependency confusion, manifest manipulation, lockfile attacks
- **Secrets & Credential Hygiene** — API keys, tokens, and credentials in non-obvious locations
- **Journalism & Newsroom Security** — source protection, metadata leakage, secure communications
- **Server-Side Request Forgery (SSRF)** — deep SSRF patterns beyond basic URL validation
- **Mass Assignment / Object Injection** — framework-specific deep patterns
- **Cryptographic Misuse** — subtle misuse beyond "don't use MD5"
- **Deserialization** — language-specific gadget chains and unsafe unmarshaling

## Usage

```bash
semgrep --config ./rules/ /path/to/your/code
```

## Structure

```
rules/
├── ai-llm-security/       # AI/LLM application security
├── supply-chain/           # Dependency and build pipeline security
├── secrets-detection/      # Deep secrets and credential detection
├── newsroom-security/      # Journalism and source protection
├── ssrf-deep/              # Advanced SSRF detection
├── mass-assignment/        # Object binding and mass assignment
├── crypto-misuse/          # Cryptographic implementation flaws
└── deserialization/        # Unsafe deserialization patterns
```

## License

MIT
