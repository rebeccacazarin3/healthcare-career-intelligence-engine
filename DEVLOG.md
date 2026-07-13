# Healthcare Career Intelligence Engine

# Phase 1 
- Python environment
- Git & GitHub
- Streamlit
- Data loading
- Data cleaning
- Search
- Sidebar filters
- Dashboard metrics
- UI organization

## Sprint 1 – Foundation

### Date
July 2, 2026

### Objective
Set up the development environment and create the first working version of the application.

### Completed
- Installed Python
- Configured VS Code
- Created a virtual environment
- Installed Streamlit and required libraries
- Created the project structure
- Connected the project to GitHub
- Built the initial homepage
- Loaded healthcare career data from a CSV

### Challenges
- Python was not recognized in PowerShell.
- Git was installed but not added to the PATH environment variable.

### How I Solved Them
- Used the Python launcher (`py`) instead of `python`.
- Added Git to the Windows PATH and verified the installation.

### What I Learned
- How virtual environments work.
- Why Git configuration is important.
- How Streamlit reads and displays data from a CSV.

### Next Sprint
Create a better Career Explorer with search, filters, and interactive career cards.

### Design Decisions

I chose Streamlit because it allows me to build interactive data applications quickly while focusing on Python instead of frontend frameworks.

I chose CSV files for version 1 because they were simple to manage during development. As the project grows, I plan to migrate the data to a relational database.

### Overall Confidence
So far things are going well but I suspect there will be many a coffee pot consummed before this project is finished to my liking. 
Things I need to work on - Remembering to add items to the PATH or to switch over to the correct version for what I am using. 

## Sprint 1 - Complete


## Sprint 2 - Project Orgainzation

### Date
July 2, 2026

### Objective
Improve the project's structure and prepare it for future growth.

### Completed
- Organized project folders
- Added a data loading utility
- Implemented Streamlit caching
- Added a navigation sidebar
- Improved the homepage layout

### Challenges
Learning how to separate application logic into reusable modules and getting the wording correct. 

### What I Learned
Keeping data loading separate from the user interface makes the project easier to maintain as it grows. Make sure to keep everything organized so that there is little confusion later on. 

### Next Sprint
Replace the data table with interactive career cards.

# Development Log

## Sprint 2.1 – Building the Foundation

### Objective
Improve the project structure and prepare the application for future features.

### Completed
- Organized the project folders
- Created a reusable data loader
- Implemented Streamlit caching
- Added a navigation sidebar
- Improved the homepage

### Next Sprint
Replace the data table with interactive career cards.

## July 5, 2026

### Sprint 2 – Dashboard Improvements

### Accomplished
- Added four dashboard metric cards
- Implemented sidebar filtering
- Added category, education, and AI relevance filters
- Connected filters to the career explorer
- Improved career table layout
- Continued cleaning and organizing app structure

### Challenges
- Resolved salary data type issues caused by CSV formatting
- Learned how to progressively filter a Pandas DataFrame

### Lessons Learned
Building one feature at a time made debugging much easier. I also learned the importance of cleaning data before performing calculations. Make sure that the structure is clear and concise.

## Sprint 2 Complete

### Accomplishments
- Added dashboard summary cards
- Implemented sidebar filtering
- Added career search
- Formatted salary values for readability
- Reorganized application structure
- Cleaned and validated dataset
- Improved overall user interface

### Challenges
- Resolved CSV formatting issues
- Corrected column naming inconsistencies
- Converted salary values from strings to numeric types
- Learned how Streamlit processes data and reruns the application

### Lessons Learned
Today reinforced the importance of data cleaning before analysis. I also gained a much better understanding of how Streamlit applications are structured and how to build interactive dashboards using Pandas filtering.

### Next Sprint
- Interactive analytics charts
- Career detail pages
- AI Career Coach integration

## July 6, 2026

### Sprint 3 – UI & UX Improvements

### Completed
- Redesigned hero section
- Improved information hierarchy
- Added contextual descriptions
- Enhanced sidebar organization
- Improved search section
- Reformatted career explorer
- Improved dashboard readability

### Lessons Learned
Today's focus shifted from functionality to user experience. I learned how layout, spacing, headings, and contextual text help guide users through an application without adding new features.

### Next Sprint
- Interactive charts
- Plotly visualizations
- Career insights dashboard

### Sprint 3 - Complete 

# Phase 1 - Complete

# Phase 2 - 
- Interactive graphics 
- Improvement of UI and UX
- Interactive Analytics Dashboard

---

## Sprint 4 – Analytics Dashboard Foundation

### Sprint Goal
Begin transforming the Healthcare Career Intelligence Engine from a searchable database into an interactive analytics dashboard.

### Completed
- Installed Plotly for interactive data visualization.
- Created a new `components` folder to improve project organization.
- Added `analytics.py` to separate visualization logic from the main application.
- Built the first reusable visualization component:
  - Average Salary by Career Category
- Integrated the Plotly chart into the Streamlit application.
- Verified that sidebar filters continue to work with the dashboard.
- Organized `app.py` into clearly labeled sections for improved readability and maintainability.

### Challenges
- Investigated why custom chart colors were not appearing.
- Learned that Plotly's continuous color scale overrides `color_discrete_sequence` when the `color` parameter is mapped to a numeric column.
- Decided to postpone UI theming until the application's core functionality is complete.

### Lessons Learned
This sprint introduced reusable visualization components and reinforced the importance of separating business logic from presentation logic. I learned how to aggregate data using Pandas, create interactive charts with Plotly Express, and organize visualizations into modular functions that can be reused throughout the application.

### Reflection
This sprint marked an important milestone in the project. The Healthcare Career Intelligence Engine evolved from displaying data in a table to presenting meaningful analytical insights through interactive visualizations. Seeing the first analytics dashboard working reinforced the value of building software incrementally while maintaining clean project organization.

### Next Sprint
- Build three additional analytics visualizations.
- Arrange the dashboard into a responsive two-column layout.
- Expand KPI cards with additional insights.
- Add an automated "Key Insights" section summarizing important findings from the data.


## Sprint 5 – Career Intelligence Dashboard

### Goal
Transform the HCIE into an interactive analytics dashboard.

### Completed
- Added four Plotly visualizations
- Connected charts to sidebar filters
- Expanded KPI metrics
- Created dashboard grid layout
- Added key insights section

### Lessons Learned
This sprint focused on communicating information visually rather than simply displaying raw data. I learned how different chart types support different analytical questions and how dashboard organization influences the user experience.

### Next Sprint
Integrate Google's Gemini API to create an AI Career Coach that provides personalized recommendations based on user interests. Maybe improve upon the graphs. 

## Sprint 6 - Interactive Career Dashboard

### Date
July 9, 2026

## Objective

Enhance the Healthcare Career Intelligence Engine by improving the user experience and transforming the application from a static dashboard into an interactive career exploration platform.

## Features Completed

### Career Profile

Implemented a new Career Profile section allowing users to:

- Select an individual healthcare career
- View detailed information for the selected career
- Display salary, education requirements, AI relevance, job outlook, Python requirements, and SQL requirements
- Dynamically update the profile based on sidebar filters

This provides users with an intuitive way to explore individual healthcare careers beyond the main data table.

### Improved User Experience

Enhanced application usability by:

- Adding a dedicated Career Profile section
- Organizing information into metric cards
- Improving visual hierarchy through section headers and captions
- Ensuring Career Profile selections respect all active sidebar filters

### Dashboard Improvements

Continued improving the Analytics Dashboard by:

- Displaying multiple interactive Plotly visualizations
- Showing Salary by Career Category
- Showing Education Distribution using a donut chart
- Organizing charts into a responsive two-column layout

## Challenges Encountered

### Metric Layout

Initially considered displaying career information inside a table.

After evaluating usability, switched to Streamlit metric cards because they allow users to scan important career information much faster.

### Information Architecture

Discussed which career attributes should receive the highest visual priority.

Current Version 1.0 focuses on:

- Salary
- Education
- AI Relevance
- Job Outlook
- Python
- SQL

Future versions will likely prioritize Certification Requirements and additional career planning information as the dataset expands. I might take away Python and SQL and exchange it for more relevant information. 

## Lessons Learned

This sprint reinforced several Streamlit concepts:

- Using `st.columns()` to create responsive layouts
- Filtering a DataFrame using user selections
- Displaying individual records using metric cards
- Building reusable UI sections
- Thinking about user experience before implementation

## Next Sprint Goals

- Build a Career Comparison feature
- Expand the dataset with certification information
- Continue improving dashboard visualizations
- Begin designing the AI Career Coach experience

## Current Project Status

Completed:

- Home Dashboard
- Sidebar Navigation
- Search
- Sidebar Filters
- Career Explorer
- Analytics Dashboard
- Interactive Career Profile

Need to Improve Later:

- Sidebar Apperance
- Career Profile Components
- 

# Sprint 7 - Career Comparison Feature

## Objective
Build an interactive comparison tool that allows users to evaluate two healthcare careers side by side.

## Completed

### Career Comparison
- Added two independent career selection dropdowns.
- Displayed two careers side by side.
- Added salary comparison with calculated salary difference.
- Added comparison insights for:
  - Education
  - Job Outlook
  - AI Relevance
  - Python
  - SQL

### Improvements
- Fixed selectbox indexing errors.
- Fixed DataFrame indexing using .iloc[0].
- Verified comparison logic works across filtered datasets.

## Lessons Learned
- Different data types require different comparison methods.
- Numeric values can be compared mathematically.
- Categorical values are best compared using equality or ordered rankings.
- Good UX explains the meaning of data rather than simply displaying it.

## Next Sprint
- Expand the Analytics Dashboard.
- Improve visualizations.
- Continue transforming HCIE into a professional analytics platform.
S