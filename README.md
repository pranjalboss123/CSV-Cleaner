# CSV Data Cleanup Tool 🧹

Hello this is the csv file cleaner as per the assignment . with three agents and their log files . a input and its cleand output csv file . 
## How project works ?? 📦

Let me walk you through what we've got here:

### The Web Interface 🌐
- `app.py`: This is where the magic starts! It's a simple web server that lets you upload your messy CSV files
- `templates/`: Got some good-looking pages in here:
  - `index.html`: The upload page with a nice drag-and-drop area
  - `result.html`: Shows you a "all done!" message when your file is cleaned
- `static/`: Just some CSS to make things pretty

### The Cleanup Agents 🧐
I have created three smart agents in the `agents/` folder:

1. **Detection Agent** (`detection_agent.py`)
   - Like a detective, it spots all the problems
   - Finds missing data, wrong email formats, misspelled countries
   - Keeps notes in `logs/detection_log.txt`

2. **Correction Agent** (`correction_agent.py`)
   - The fixer-upper of the bunch
   - Fixes email formats, corrects country names
   - Gets rid of duplicate entries
   - Writes what it fixed in `logs/correction_log.txt`

3. **Enrichment Agent** (`enrichment_agent.py`)
   - The finishing touches guy
   - Fills in missing names with realistic ones
   - Makes sure every row has a valid country
   - Keeps track of changes in `logs/enrichment_log.txt`

### The Control Center 🎮
`main.py` is the file that keeps track of all agents works correctly :
1. First calls the detective (Detection)
2. Then the fixer (Correction)
3. Finally, the finishing touches (Enrichment)

### File Organization 📁
- `input/`: Drop your messy CSV here (like `messy_customers.csv`)
- `output/`: Find your cleaned-up file here as `final_cleaned_output.csv`
- `logs/`: See what each agent did in their own log files

## How to Use It? 🚀

1. Fire up the web server (run `app.py`)
2. Open your browser and head to the upload page
3. Drop your messy CSV file
4. Click "Upload & Clean"
5. Wait a few seconds while our agents do their thing
6. Download your clean CSV!

## What Gets Fixed? 🛠️

- Standardizes email addresses (lowercase, proper format)
- Fixes country name typos ("Indiia" → "India")
- Fills in missing names with realistic ones
- Removes duplicate entries
- Makes sure phone numbers and other data are consistent

Thats the working of our agents . 

Thank you 
Rishikesh gupta 