"""
| Action                 | Works Automatically | Needs `global` | Best Practice            |
| ---------------------- | ------------------- | -------------- | ------------------------ |
| Read global variable   | ✅ Yes               | ❌ No           | Fine                     |
| Modify global variable | ❌ No                | ✅ Yes          | Avoid — pass as argument |
"""