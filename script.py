import json
import os

def create_rule(website_id, website_url):
    return {
        "id": website_id,
        "priority": 1,
        "action": {"type": "block"},
        "condition": {"urlFilter": f"//*{website_url}/*"}
    }

def load_existing_rules():
    """Load existing rules from the JSON file, if it exists."""
    if os.path.exists('rules.json'):
        with open('rules.json', 'r') as json_file:
            return json.load(json_file)
    return []  # Return an empty list if the file doesn't exist

def main():
    # Load existing rules
    rules = load_existing_rules()
    website_id = len(rules) + 1  # Start with the next available ID

    while True:
        website_url = input("Write 'exit' and ENTER to exit from the script. Enter website URL to block (or type 'exit' to stop): ")

        if website_url.lower() == 'exit':
            break

        # Create rule for the website
        rule = create_rule(website_id, website_url)
        rules.append(rule)

        # Increment the website_id for the next rule
        website_id += 1

    # Save the updated list of rules to the JSON file
    with open('rules.json', 'w') as json_file:
        json.dump(rules, json_file, indent=4)

    print("Blocked websites have been saved to 'rules.json'.")

if __name__ == "__main__":
    main()
