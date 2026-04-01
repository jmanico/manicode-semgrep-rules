# Manicode Semgrep Rules

**298 custom Semgrep rules** across 18 security categories that go **deep** where stock Semgrep goes wide.

## Usage

```bash
semgrep --config ./rules/ /path/to/your/code
```

Run a specific category:
```bash
semgrep --config ./rules/ai-llm-security/ /path/to/your/code
```

## Categories

| Category | Rules | Key Patterns |
|----------|-------|-------------|
| **AI/LLM Security** | 28 | Prompt injection, unsafe LLM output to eval/exec/SQL/shell, RAG security, API key hardcoding |
| **JWT Security** | 12 | Algorithm confusion, `none` algorithm, missing verification, hardcoded secrets, `kid` injection |
| **GraphQL Security** | 8 | Introspection enabled, no depth/complexity limits, resolver injection, batching abuse |
| **SSTI** | 10 | Jinja2, Mako, Tornado, FreeMarker, Velocity, Pebble, Thymeleaf, EJS template injection |
| **WebSocket Security** | 8 | Cross-Site WebSocket Hijacking (CSWSH), missing origin validation, message eval/innerHTML |
| **OAuth/OIDC** | 9 | Implicit grant, missing PKCE/state, lax redirect_uri, tokens in localStorage |
| **Deep SSRF** | 31 | Cloud metadata, file:// protocol, partial URL construction, redirect following |
| **Unsafe File Operations** | 10 | Zip Slip (Java/Python/Go/Node), path traversal, unsafe uploads |
| **Supply Chain** | 20 | Dependency confusion, post-install curl\|sh, CI pipeline injection, unpinned actions |
| **Secrets Detection** | 20 | Connection strings, IaC secrets, Stripe/Twilio/Slack/GitHub API key patterns |
| **Sensitive Data Logging** | 11 | Passwords/tokens/credit cards in logs, request body logging, auth header logging |
| **Header Injection** | 10 | CRLF injection, Host header injection, open redirects (Python/Java/JS/Go) |
| **ReDoS** | 8 | User-controlled regex, nested quantifiers, regex on untrusted input without timeout |
| **Broken Access Control** | 10 | Missing auth decorators/middleware, IDOR patterns (Flask/Django/Express/Spring/FastAPI) |
| **Newsroom Security** | 28 | Source protection, EXIF/metadata leakage, SecureDrop logging, embargo date exposure |
| **Mass Assignment** | 16 | Spring BeanUtils, Django `**request.data`, Express `{...req.body}`, prototype pollution |
| **Cryptographic Misuse** | 33 | ECB mode, static IVs, weak KDF, Math.random(), timing attacks, TLS verify bypass |
| **Deserialization** | 25 | pickle, PyYAML, Jackson, XStream, SnakeYAML, node-serialize, Go gob |

## Languages Covered

Python, Java, JavaScript/TypeScript, Go, HCL (Terraform), YAML, JSON, Generic

## Structure

```
rules/
├── ai-llm-security/       # AI/LLM application security (28 rules)
├── jwt-security/           # JWT misconfigurations (12 rules)
├── graphql-security/       # GraphQL API security (8 rules)
├── ssti/                   # Server-side template injection (10 rules)
├── websocket-security/     # WebSocket security (8 rules)
├── oauth-security/         # OAuth 2.0 / OIDC flaws (9 rules)
├── ssrf-deep/              # Advanced SSRF detection (31 rules)
├── unsafe-file-ops/        # Zip Slip, path traversal, uploads (10 rules)
├── supply-chain/           # Dependency and build pipeline security (20 rules)
├── secrets-detection/      # Deep secrets and credential detection (20 rules)
├── sensitive-logging/      # Sensitive data in logs (11 rules)
├── header-injection/       # CRLF, Host header, open redirect (10 rules)
├── redos/                  # Regular expression DoS (8 rules)
├── broken-access-control/  # Missing auth, IDOR patterns (10 rules)
├── newsroom-security/      # Journalism and source protection (28 rules)
├── mass-assignment/        # Object binding and mass assignment (16 rules)
├── crypto-misuse/          # Cryptographic implementation flaws (33 rules)
└── deserialization/        # Unsafe deserialization patterns (25 rules)
```

## License

MIT
