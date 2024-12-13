# AdBlocker
A simple ad blocker project to experiment since a lot of ad blockers get taken down or don't work properly. 

Sure! Here's a detailed README description that you can use for your project.

---

# Website Blocker Rule Generator

This Python script allows you to create a list of website blocking rules in JSON format. It appends new blocking rules to an existing `blocked_websites.json` file, making it ideal for managing and expanding a list of websites you want to block without overwriting or deleting previous entries.

### Features
- **Append to Existing Data**: It loads the existing blocking rules from `blocked_websites.json` (if the file exists) and appends new rules without overwriting the existing data.
- **Automatic ID Generation**: Each new rule gets a unique ID based on the number of existing rules, ensuring no duplication.
- **Simple User Input**: Users can input website URLs to block, and the script will automatically generate and append the corresponding blocking rules.
- **Customizable Rule Format**: The rules are formatted as JSON objects with an `id`, `priority`, `action` (block), and a `condition` that matches the specified URL pattern.

### Prerequisites
- Python 3.x installed on your system.

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
3. **Appending to File**: The script then appends the generated rule to the `blocked_websites.json` file. If the file doesn't exist, it is created.

4. **Exit**: Type 'exit' to stop the process and save the changes.

### Installation
1. Clone the repository or download the script file.

2. Install Python 3.x if you haven't already. You can download Python from [here](https://www.python.org/downloads/).

3. Ensure you have permissions to read and write to the directory where the `blocked_websites.json` file will be saved.

### Usage
1. Open a terminal or command prompt.

2. Navigate to the directory where the script is saved:
   ```bash
   cd /path/to/script/
   ```

3. Run the script:
   ```bash
   python generate_block_rules.py
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
- If the `blocked_websites.json` file already exists, the new rules will be appended to it, preserving any previously saved rules.
- If no file exists, the script will create a new `blocked_websites.json` file.
- The script automatically assigns a unique ID to each new rule based on the number of existing rules.

### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to adjust or expand any sections based on your specific needs or features!
