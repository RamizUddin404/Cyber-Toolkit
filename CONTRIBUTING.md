# Contributing to Cyber-Toolkit

Thank you for your interest in contributing to **Cyber-Toolkit**! We welcome contributions from the community to help make this the ultimate security suite for Termux.

## 🤝 How to Contribute

1.  **Fork the Repository:** Click the "Fork" button on the top right of this page.
2.  **Clone Your Fork:**
    ```bash
    git clone https://github.com/YOUR_USERNAME/Cyber-Toolkit.git
    ```
3.  **Create a Branch:**
    ```bash
    git checkout -b feature/AmazingNewTool
    ```
4.  **Add Your Tool:**
    *   Create a new Python script (e.g., `my_tool.py`).
    *   Ensure it has a `def run():` function as the entry point.
    *   Use `import cyber_deps` if you need external packages.
5.  **Commit Your Changes:**
    ```bash
    git commit -m "Added AmazingNewTool for XYZ"
    ```
6.  **Push to GitHub:**
    ```bash
    git push origin feature/AmazingNewTool
    ```
7.  **Submit a Pull Request:** Go to the original repository and click "New Pull Request".

## 📜 Code Style
*   Keep it simple and readable.
*   Use the `tool_header(name)` function for consistency.
*   Handle errors gracefully (try/except).
*   **Do not** include malicious payloads that harm innocent users. This is for educational/security testing only.

## 🐛 Reporting Bugs
If you find a bug, please open an issue describing the problem and how to reproduce it.

---
**Happy Hacking!**
- **Ramiz Uddin**
