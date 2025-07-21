#!/usr/bin/env python3
"""
Test script for Google Trends chart generation
"""

import sys
import os

# Add the current directory to the path to import our module
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from google_trends_chart import python_user_visible, generate_synthetic_trends_data
import matplotlib.pyplot as plt

def test_data_generation():
    """Test that synthetic data is generated correctly"""
    print("Testing data generation...")
    
    data = generate_synthetic_trends_data()
    
    # Check that we have the expected columns
    expected_columns = ['Date', 'ChatGPT', 'Claude', 'Gemini', 'Copilot', 'Deepseek']
    assert all(col in data.columns for col in expected_columns), "Missing expected columns"
    
    # Check that we have data points
    assert len(data) > 0, "No data generated"
    
    # Check that all values are between 0 and 100
    for tool in ['ChatGPT', 'Claude', 'Gemini', 'Copilot', 'Deepseek']:
        assert data[tool].min() >= 0, f"{tool} has values below 0"
        assert data[tool].max() <= 100, f"{tool} has values above 100"
    
    # Check date range
    start_date = data['Date'].min()
    end_date = data['Date'].max()
    
    assert start_date.year == 2022, "Start date not in 2022"
    assert start_date.month >= 9, "Start date not in September or later"
    assert end_date.year >= 2025, "End date not reaching 2025"
    
    print("✓ Data generation tests passed")
    return data

def test_chart_creation():
    """Test that chart can be created and saved"""
    print("Testing chart creation...")
    
    # Generate test data
    data = generate_synthetic_trends_data()
    
    # Create chart but don't show it (for testing)
    plt.figure(figsize=(14, 8))
    
    colors = {
        'ChatGPT': '#FF6B6B',
        'Claude': '#4ECDC4', 
        'Gemini': '#45B7D1',
        'Copilot': '#96CEB4',
        'Deepseek': '#FFEAA7'
    }
    
    for tool in ['ChatGPT', 'Claude', 'Gemini', 'Copilot', 'Deepseek']:
        plt.plot(data['Date'], data[tool], 
                label=tool, 
                color=colors[tool], 
                linewidth=2.5,
                marker='o',
                markersize=3,
                alpha=0.8)
    
    plt.title('Google Trends: AI Tools Popularity in Spain\n(September 2022 - February 2025)', 
              fontsize=16, fontweight='bold', pad=20)
    plt.xlabel('Date', fontsize=12, fontweight='bold')
    plt.ylabel('Search Interest (0-100)', fontsize=12, fontweight='bold')
    
    # Save chart for verification
    plt.savefig('/tmp/google_trends_test_chart.png', dpi=150, bbox_inches='tight')
    plt.close()  # Close without showing
    
    # Check that file was created
    assert os.path.exists('/tmp/google_trends_test_chart.png'), "Chart image not saved"
    
    print("✓ Chart creation tests passed")
    print("✓ Test chart saved to /tmp/google_trends_test_chart.png")

def test_python_user_visible():
    """Test the main python_user_visible function"""
    print("Testing python_user_visible function...")
    
    try:
        # This will display the chart but we can't test the display directly
        data, chart = python_user_visible()
        
        # Verify return values
        assert data is not None, "No data returned"
        assert chart is not None, "No chart returned"
        
        print("✓ python_user_visible function tests passed")
        
    except Exception as e:
        print(f"✗ python_user_visible function failed: {e}")
        raise

def run_all_tests():
    """Run all tests"""
    print("Running Google Trends chart tests...\n")
    
    try:
        test_data_generation()
        test_chart_creation()
        test_python_user_visible()
        
        print("\n🎉 All tests passed successfully!")
        return True
        
    except Exception as e:
        print(f"\n❌ Tests failed: {e}")
        return False

if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)