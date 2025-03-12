- Deserialization vulnerabilities have long been a hacker's playground.
- LLM powered apps dynamically processing user input, the attack surface has just gotten larger when LLm powered apps process and deserialize structured data, especially when integrating tools, agents, or external function call.

- When an LLM interact with serialized data - be it JSON, pickle protobufs, you should look fo improper de-serialization mecahnismsthat allow them to inject arbitrary objects, execute remote code or tamper with application logic.