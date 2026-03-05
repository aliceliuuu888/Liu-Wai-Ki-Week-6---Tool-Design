# Liu-Wai-Ki-Week-6---Tool-Design
# Key Points Extractor Tool

## Tool Description
Automatically extracts key points, action items, and stakeholder impact from long texts, helping users quickly understand the core content of documents.

## Features
- **Key Points Extraction**: Identifies the 3-5 most important sentences
- **Summary Generation**: Automatically creates a one-sentence summary
- **Action Items Recognition**: Identifies action plans mentioned in the text
- **Stakeholder Impact Analysis**: Analyzes impact on different groups
- **Text Statistics**: Provides basic statistical information

## Installation

```bash
pip install python-dotenv
```

##  API Key Configuration (Optional)
```bash
cp .env.example .env
```


## Edit the .env file and add your DeepSeek API key:
```
DEEPSEEK_API_KEY=sk-Your key
```

## **Run the demo program:**
```bash
python demo.py
```

## Usage Example
```python
from tool import KeyPointsExtractor

# Create extractor instance
extractor = KeyPointsExtractor()

# Extract key points
text = "This is a text that needs analysis..."
result = extractor.execute(text, max_points=5)

if result["success"]:
    print(result["key_points"])
else:
    print(f"Error: {result['error']}")
```
## Output Format Example
```json
{
    "success": true,
    "key_points": ["Q3 revenue reached $5 billion, up 20% year-over-year", "Will open 5 new factories in Asia"],
    "summary": "Company performance improves but with restructuring layoffs",
    "action_items": ["Open new factories", "Lay off 1000 employees"],
    "stakeholder_impact": {
        "investors": "positive impact",
        "employees": "negative impact"
    },
    "statistics": {
        "total_characters": 350,
        "total_sentences": 8
    }
}
```
## File Structure
```
.
├── tool.py          # Tool implementation
├── demo.py          # Demo script
├── README.md        # This document
├── .env.example     # Environment variables example
└── .gitignore       # Git ignore file
🧪 Demo Content
Running demo.py will showcase:

✅ Success Case: CEO speech text analysis

❌ Error Case: Empty text and invalid parameter handling
```

## Notes
API Key is optional - the tool runs in simulation mode without it

If using the real API, ensure your account has sufficient balance
