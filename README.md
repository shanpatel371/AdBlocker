# AdBlocker
This is a simple ad blocker script designed for experimentation and personal use. Many ad blockers either get taken down or don't work as expected, so this script offers a flexible solution for blocking ads from specific websites. It allows you to add the domains of websites that frequently serve ads, and it automatically generates blocking rules for those sites. Once added, the script ensures that ads from those websites will be blocked and won't appear during your browsing sessions.

### How It Works
1. **User Input**: The script prompts the user to input the website URLs they want to block (e.g., `doubleclick.net`, `googleadservices.com`, etc.).
2. **Generate Blocking Rule**: For each website, the script generates a blocking rule in the following format:
   ```json
   {
       "id": <unique_id>,
       "priority": 1,
       "action": {"type": "block"},
       "condition": {"urlFilter": "*://<website_url>/*"}
   }
   ```
3. **Appending to File**: The script then appends the generated rule to the `rules.json` file. If the file doesn't exist, it is created.

4. **Exit**: Type 'exit' to stop the process and save the changes.

### Installation
1. Clone the repository 

2. Install Python 3.x if you haven't already. You can download Python from [here](https://www.python.org/downloads/).

3. Ensure you have permissions to read and write to the directory where the `rules.json` file is saved.

### Usage
1. Open a terminal or command prompt.

2. Navigate to the directory where the script is saved:
   ```bash
   cd /path/to/script/
   ```

3. Run the script:
   ```bash
   python script.py
   ```

4. Follow the on-screen prompts to enter website URLs that you want to block. When you're done, type `exit` to finish and save the data.

   Example:
   ```
   Enter website URL to block (or type 'exit' to stop): doubleclick.net
   Enter website URL to block (or type 'exit' to stop): googleadservices.com
   Enter website URL to block (or type 'exit' to stop): exit
   ```

5. The `blocked_websites.json` file will be created or updated with the new blocking rules.

### Example of `blocked_websites.json`
After running the script and adding a few websites, your `blocked_websites.json` might look like this:

```json
[
    {
        "id": 1,
        "priority": 1,
        "action": {"type": "block"},
        "condition": {"urlFilter": "://*doubleclick.net/*"}
    },
    {
        "id": 2,
        "priority": 1,
        "action": {"type": "block"},
        "condition": {"urlFilter": "*://googleadservices.com/*"}
    }
]
```

### Notes
- If the `rules.json` file already exists, the new rules will be appended to it, preserving any previously saved rules.
- The script automatically assigns a unique ID to each new rule based on the number of existing rules.

### Add to Chrome Extension
- On Chrome, navigate to `chrome://extensions/`
- Click `Load Unpacked`
- Select the `AdBlocker` Folder 


Feel free to adjust or expand any sections based on your specific needs or features!
