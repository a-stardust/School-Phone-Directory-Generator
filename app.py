import pandas as pd
import os

# Function to generate HTML, CSS, and JS files with checkboxes and rearranging functionality
def generate_website_from_csv(file_path, output_folder='output_website'):
    # Read the CSV file
    try:
        df = pd.read_csv(file_path)
        if 'School Name' not in df.columns or 'Phone Number' not in df.columns:
            raise ValueError('The CSV file must have "School Name" and "Phone Number" columns')
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return
    
    # Ensure output directory exists
    os.makedirs(output_folder, exist_ok=True)

    # Generate HTML content with checkboxes and rearranging functionality
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>School Contact List</title>
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">
        <link rel="stylesheet" href="styles.css">
        <script src="script.js" defer></script>
    </head>
    <body>
        <div class="container">
            <h1>Schools Phone Directory</h1>
            <div class="school-list">
    """
    
    # Add each school name, phone number, and checkbox
    for i, row in df.iterrows():
        school_name = row['School Name']
        phone_number = row['Phone Number']
        html_content += f"""
        <div class="school-item" id="school-{i}">
            <input type="checkbox" id="checkbox-{i}" class="call-checkbox" data-index="{i}">
            <label for="checkbox-{i}" class="school-label">
                <a href="tel:{phone_number}">{school_name}</a>
            </label>
        </div>
        """
    
    html_content += """
            </div>
        </div>
    </body>
    </html>
    """
    
    # Write HTML file
    with open(os.path.join(output_folder, 'index.html'), 'w', encoding='utf-8') as file:
        file.write(html_content)

    # Generate CSS content
    css_content = """
    /* General Body and Layout */
    body {
        font-family: 'Poppins', sans-serif;
        background-color: #a8d0e6; /* Mild background color */
        margin: 0;
        padding: 0;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
    }

    .container {
        max-width: 1000px;
        width: 100%;
        margin: 20px;
        padding: 30px;
        background-color: rgba(255, 255, 255, 0.85); /* Glass effect */
        backdrop-filter: blur(10px); /* Glass blur effect */
        border-radius: 12px;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    }

    h1 {
        text-align: center;
        font-size: 35px;
        color: #333;
        margin-bottom: 30px;
        font-weight: 700;
        letter-spacing: 1px;
    }

    /* Title for the list */
    .list-title {
        font-size: 30px;
        font-weight: bold;
        color: #007bff;
        text-align: center;
        margin-bottom: 20px;
    }

    /* Styling for the school list */
    .school-list {
        display: flex;
        flex-direction: column;
        gap: 15px;
    }

    /* School item styling */
    .school-item {
        display: flex;
        align-items: center;
        justify-content: space-between;
        background-color: rgba(255, 255, 255, 0.5); /* Mild background color */
        padding: 15px 20px;
        border-radius: 8px;
        border: 1px solid #e0e0e0;
        transition: background-color 0.3s ease, transform 0.2s ease;
        backdrop-filter: blur(5px); /* Frosted effect for each item */
    }

    .school-item:hover {
        background-color: rgba(0, 123, 255, 0.1);
        transform: translateY(-2px);
    }

    .school-item input[type="checkbox"] {
        width: 25px;
        height: 25px;
        margin-right: 20px;
        cursor: pointer;
        accent-color: #007BFF; /* Blue checkbox color */
        border-radius: 5px;
        transition: background-color 0.3s ease;
    }

    .school-item input[type="checkbox"]:checked {
        background-color: #007BFF;
    }

    /* School label and link styling */
    .school-label {
        flex-grow: 1;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .school-label a {
        text-decoration: none;
        color: #007BFF;
        font-size: 18px;
        font-weight: 600;
        transition: color 0.3s ease;
    }

    .school-label a:hover {
        color: #0056b3;
    }

    /* Add styling for a completed call */
    .completed .school-label a {
        color: #6c757d;
        text-decoration: line-through;
    }

    .completed {
        background-color: #d1e7dd;
    }

    /* Responsive styling */
    @media (max-width: 768px) {
        .container {
            padding: 20px;
            max-width: 100%;
        }
        
        h1 {
            font-size: 28px;
        }
        
        .school-item {
            flex-direction: column;
            align-items: flex-start;
        }
        
        .school-item input[type="checkbox"] {
            margin-right: 10px;
        }
        
        .school-label a {
            font-size: 16px;
        }
    }
    """
    
    # Write CSS file
    with open(os.path.join(output_folder, 'styles.css'), 'w', encoding='utf-8') as file:
        file.write(css_content)

    # Generate JavaScript content to handle checkbox and move completed calls
    js_content = """
    document.addEventListener('DOMContentLoaded', function () {
        const checkboxes = document.querySelectorAll('.call-checkbox');

        checkboxes.forEach(checkbox => {
            checkbox.addEventListener('change', function () {
                const schoolItem = document.getElementById('school-' + this.dataset.index);
                const schoolList = document.querySelector('.school-list');

                if (this.checked) {
                    // Move completed item to the end of the list
                    schoolItem.classList.add('completed');
                    schoolList.appendChild(schoolItem);
                } else {
                    // Move unchecked item back to the top
                    schoolItem.classList.remove('completed');
                    schoolList.insertBefore(schoolItem, schoolList.firstChild);
                }
            });
        });
    });
    """
    
    # Write JavaScript file
    with open(os.path.join(output_folder, 'script.js'), 'w', encoding='utf-8') as file:
        file.write(js_content)

    print(f"Website files generated successfully in the '{output_folder}' directory.")

# Replace 'schools.csv' with the path to your CSV file
generate_website_from_csv('schools.csv')
