from flask import Blueprint, render_template, request, jsonify
from datetime import datetime
import markdown
import os
from app.travel_planner.src.travel_planner.crew import TravelPlanner

# Create a Blueprint for routes
bp = Blueprint('main', __name__)

# File paths for reports
REPORT_FILES = {
    "weather": "weather_report.md",
    "accommodation": "accommodation_report.md",
    "transportation": "transportation_report.md"
}

def read_markdown_file(file_path):
    """Reads a Markdown file and converts it to HTML."""
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            return markdown.markdown(file.read())  # Convert Markdown to HTML
    return "<p>Report not available</p>"

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/plan_trip', methods=['POST'])
def plan_trip():
    data = request.form.to_dict()

    # Prepare inputs for the crew
    inputs = {
        'destination': data.get('destination'),
        'budget': data.get('budget'),
        'duration': data.get('duration'),
        'interests': data.get('interests'),
        'travel_style': data.get('travel_style'),
        'travel_dates': data.get('travel_dates'),
        'num_travelers': data.get('num_travelers'),
        'current_year': str(datetime.now().year)
    }

    try:
        print("\nPlanning your trip... Please wait.\n")
        TravelPlanner().crew().kickoff(inputs=inputs)
        result = {"message": "Trip planned successfully!", "data": inputs}
    except Exception as e:
        result = {"message": f"An error occurred while running the crew: {e}"}

    return jsonify(result)

@bp.route('/get_reports')
def get_reports():
    """Fetch the generated travel reports."""
    reports = {name: read_markdown_file(path) for name, path in REPORT_FILES.items()}
    return jsonify(reports)
