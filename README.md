# InstaCompare
A Python script that compares your Instagram followers and following lists to identify non-mutual follows.

##How It Works
Instagram allows you to export your account data as JSON files. This script parses both files, extracts usernames, and compares them to produce two lists:

- Not following back — accounts you follow that don't follow you
- Not following me back — accounts that follow you that you don't follow

It also includes a manually configured filter list for accounts you want to exclude from results, such as deactivated accounts, deleted accounts, or public figures you don't expect a follow back from.

##Usage
1. Request your data export from Instagram and download the JSON files
2. Add the file paths to your exported JSON files in the script
3. Manually update the filter list in the script with any accounts you want to exclude
4. Run the script: python instagram_comparison.py followers.json following.json

##Requirements
Python 3
