---
title: Apache SSL certificate issues
kind: faq
---

If you're having issues with your Apache integration, it may be because the upgraded version of Python in agent version 5.2 has bug fixes concerning SSL certificates.

A "faulty" SSL certificate that the agent previously accepted may now be rejected resulting in errors.

To resolve the issue, patch the apache.py file in /checks.d with [these changes](https://gist.github.com/philliphaines/06e7cef908f921de94b5):