# Google Trends Chart Generator

This module provides functionality to generate and display a line chart showing Google Trends popularity indices for AI tools in Spain.

## Overview

The `google_trends_chart.py` module generates synthetic Google Trends data for five popular AI tools:
- **ChatGPT**: OpenAI's conversational AI
- **Claude**: Anthropic's AI assistant  
- **Gemini**: Google's AI model
- **Copilot**: GitHub/Microsoft's AI coding assistant
- **Deepseek**: AI research company's models

## Time Period

The chart covers the period from **September 2022 to February 2025**, showing the evolution of search interest over time.

## Usage

### Basic Usage

```python
from google_trends_chart import python_user_visible

# Generate and display the chart inline
data, chart = python_user_visible()
```

### Advanced Usage

```python
from google_trends_chart import python_user_visible, generate_synthetic_trends_data

# Generate and save the chart
data, chart = python_user_visible(save_chart=True, output_path="my_chart.png")

# Or generate data separately
trends_data = generate_synthetic_trends_data()
print(f"Generated {len(trends_data)} data points")
```

### Command Line Usage

```bash
# Install dependencies
pip install -r requirements.txt

# Generate and display chart
python3 google_trends_chart.py

# Run tests
python3 test_google_trends.py

# See demo
python3 demo_usage.py
```

## Data Characteristics

The synthetic data reflects realistic adoption patterns:

- **ChatGPT**: Shows explosive growth starting in late 2022, peaking in early 2023, then stabilizing at high levels
- **Claude**: Gradual adoption starting in 2023 with steady growth  
- **Gemini**: Strong launch presence starting in late 2023
- **Copilot**: Consistent growth from developer community adoption
- **Deepseek**: Later market entry with increasing presence in 2024-2025

## Chart Features

- **Interactive Display**: Charts display inline using matplotlib's `show()` function
- **High Quality**: 150 DPI resolution when saved
- **Professional Styling**: Custom colors, proper labeling, grid lines
- **Date Formatting**: Quarterly date labels for readability
- **Legend**: Clear identification of each AI tool
- **Spanish Context**: Designed for Spain-specific Google Trends data

## Dependencies

- `matplotlib >= 3.5.0`: Chart generation and display
- `numpy >= 1.20.0`: Numerical computations
- `pandas >= 1.3.0`: Data manipulation and time series

## Files

- `google_trends_chart.py`: Main implementation
- `test_google_trends.py`: Comprehensive test suite
- `demo_usage.py`: Usage examples
- `requirements.txt`: Python dependencies
- `google_trends_spain.png`: Sample generated chart

## Note on Data

All data is synthetic and generated for demonstration purposes. It does not represent actual Google Trends data, but follows realistic patterns based on the public timeline of these AI tools' releases and adoption.