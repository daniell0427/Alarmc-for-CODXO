# Alarm Clock Application

This is a custom alarm clock application built using `CustomTkinter`, a modern, customizable version of the `Tkinter` library. The application allows users to set, view, and manage alarms with options to repeat alarms on specific days of the week.

## Features

- **Add Alarms**: Set alarms with specific times and repeat options.
- **View Alarms**: Display all set alarms in a scrollable list.
- **Manage Alarms**: Enable, disable, or delete alarms.
- **Customizable UI**: The application uses `CustomTkinter` for a modern look and feel, with a dark mode theme.

## Project Structure

- `main.py`: The main entry point for the application.
- `pages/alarmPage.py`: Contains the `AlarmPage` class, which is the main interface for viewing and managing alarms.
- `pages/addPage.py`: Contains the `AddPage` class, which provides the interface for adding new alarms.
- `database.py`: Contains functions to interact with the SQLite database, including retrieving and adding alarms.
- `functions.py`: Contains utility functions, such as generating UUIDs and playing alarm sounds.

## Getting Started

### Prerequisites

- Python 3.x
- `CustomTkinter`
- `sqlite3` (comes pre-installed with Python)

### Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com/your-username/alarm-clock-app.git
    cd alarm-clock-app
    ```

2. **Install the required packages**:
    ```sh
    pip install customtkinter
    ```

3. **Set up the database**:
    Ensure that the SQLite database is set up correctly. If not, you can create the necessary tables using the following schema:

    ```sql
    CREATE TABLE alarms (
        user_uuid TEXT,
        hour INTEGER,
        minutes INTEGER,
        repeat TEXT,
        active INTEGER
    );
    ```

4. **Run the application**:
    ```sh
    python main.py
    ```

### Usage

- **Adding an Alarm**: Click the `+` button to open the `AddPage`. Set the time and repeat days for the alarm, then click `Submit`.
- **Managing Alarms**: In the `AlarmPage`, you can toggle alarms on or off and delete them using the provided buttons.
- **Viewing Alarms**: All set alarms are displayed in a scrollable list. Each alarm shows its time, repeat days, and status (active/inactive).
