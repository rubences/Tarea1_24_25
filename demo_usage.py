#!/usr/bin/env python3
"""
Example usage of the Google Trends chart module
"""

from google_trends_chart import python_user_visible, generate_synthetic_trends_data

def main():
    """Demonstrate usage of the Google Trends chart functionality"""
    
    print("=== Google Trends Chart Demo ===")
    print("This demo shows how to use the python_user_visible function")
    print("to generate and display a line chart of AI tools popularity trends.")
    print("-" * 50)
    
    # Option 1: Use the main function directly
    print("1. Generating chart using python_user_visible():")
    data, chart = python_user_visible()
    
    print("\n" + "-" * 50)
    
    # Option 2: Generate data separately and inspect it
    print("2. Data summary:")
    data_summary = generate_synthetic_trends_data()
    
    print(f"Number of data points: {len(data_summary)}")
    print(f"Date range: {data_summary['Date'].min().strftime('%Y-%m-%d')} to {data_summary['Date'].max().strftime('%Y-%m-%d')}")
    print("\nAverage popularity by tool:")
    
    for tool in ['ChatGPT', 'Claude', 'Gemini', 'Copilot', 'Deepseek']:
        avg_popularity = data_summary[tool].mean()
        max_popularity = data_summary[tool].max()
        print(f"  {tool}: {avg_popularity:.1f} (max: {max_popularity:.1f})")
    
    print("\n✅ Demo completed successfully!")

if __name__ == "__main__":
    main()