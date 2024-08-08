# Social_Media_Platform(Bazinga.Com)

Bazinga.Com is a social media platform where we all can share memes and pretend we're working. Let's connect and keep the procrastination game strong!

## Features

- User registration and authentication
- Post creation and management
- Responsive design
- Attractive UI with fun and engaging styles

## Installation

### Prerequisites

- Python 3.x
- Flask
- Git

### Setup Instructions

1. **Clone the repository:**

    ```sh
    git clone https://github.com/TarunChegondi/Social_media_platform.git
    cd Social_media_platform
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    # For Windows
    .\venv\Scripts\activate
    # For macOS and Linux
    source venv/bin/activate
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the database:**

    ```sh
    flask db init
    flask db migrate -m "Initial migration"
    flask db upgrade
    ```

5. **Run the application:**

    ```sh
    flask run
    ```

6. **Access the application:**

    Open your web browser and go to `http://127.0.0.1:5000`.

## Large File Handling

This project uses Git Large File Storage (LFS) to manage large files.

### Installing Git LFS

- **Windows:** Download and install Git LFS from [Git LFS](https://git-lfs.github.com/).
- **macOS:** Use Homebrew:
  
  ```sh
  brew install git-lfs
