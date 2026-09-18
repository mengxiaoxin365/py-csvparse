# RFC-4180 CSV row parser

```
csvline.py
```
When you parse raw protocol payloads for delivery logs, a single unescaped quote can break the whole pipeline. Check the Python Csvparse test suite next to the implementation to see how it handles these boundary conditions.

It parses a single CSV line while correctly honoring nested quotes and escape characters. You get this strictly dependency-free.

The Python Csvparse module relies entirely on the standard library. You will not need to install any external services or third-party packages.