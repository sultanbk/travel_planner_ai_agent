#!/usr/bin/env python
import sys
import warnings
from datetime import datetime
from travel_planner.crew import TravelPlanner

# Suppress warnings
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    """
    Run the TravelPlanner crew.
    """
    # Collect user inputs
    print("Welcome to YatraSathi Free!")
    destination = input("Enter your destination (e.g., Rajasthan): ")
    budget = input("Enter your budget (e.g., ₹20,000): ")
    duration = input("Enter trip duration (e.g., 5 days): ")
    interests = input("Enter your interests (e.g., culture, food, adventure): ")
    travel_style = input("Enter your preferred travel style (e.g., relaxed, adventurous): ")
    travel_dates = input("Enter your travel dates (e.g., YYYY-MM-DD to YYYY-MM-DD): ")
    num_travelers = input("Enter the number of travelers (e.g., solo, couple, family, group): ")

    # Prepare inputs for the crew
    inputs = {
        'destination': destination,
        'budget': budget,
        'duration': duration,
        'interests': interests,
        'travel_style': travel_style,
        'travel_dates': travel_dates,
        'num_travelers': num_travelers,
        'current_year': str(datetime.now().year)
    }

    try:
        # Run the TravelPlanner crew
        print("\nPlanning your trip... Please wait.\n")
        TravelPlanner().crew().kickoff(inputs=inputs)
    except Exception as e:
        print(f"An error occurred while running the crew: {e}")
        sys.exit(1)


if __name__ == "__main__":
    run()