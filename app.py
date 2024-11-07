import pandas as pd

# Function to generate HTML, CSS, and JS files
def generate_website_from_excel(file_path, output_folder='output_website'):
    # Read the Excel file
    try:
        df = pd.read_excel(file_path)
        if 'School Name' not in df.columns or 'Phone Number' not in df.columns:
            raise ValueError('The Excel file must have "School Name" and "Phone Number" columns')
    except Exception as e:
        print(f"Error reading Excel file: {e}")
        return
    
    # Ensure output directory exists
    import os
    os.makedirs(output_folder, exist_ok=True)

    # Generate HTML content
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>School Contact List</title>
        <link rel="stylesheet" href="styles.css">
    </head>
    <body>
        <div class="container">
            <h1>School Contact List</h1>
            <div class="school-list">
    """
    
    # Add each school name and phone number as a clickable link
    for _, row in df.iterrows():
        school_name = row['School Name']
        phone_number = row['Phone Number']
        html_content += f'<a href="tel:{phone_number}">{school_name}</a>\n'
    
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
    body {
        font-family: Arial, sans-serif;
        background-color: #f9f9f9;
        margin: 20px;
        padding: 0;
    }
    .container {
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
        background-color: #ffffff;
        border-radius: 8px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }
    h1 {
        text-align: center;
        color: #333;
    }
    .school-list a {
        display: block;
        margin: 10px 0;
        padding: 10px;
        background-color: #007BFF;
        color: white;
        text-decoration: none;
        border-radius: 5px;
        text-align: center;
    }
    .school-list a:hover {
        background-color: #0056b3;
    }
    """
    
    # Write CSS file
    with open(os.path.join(output_folder, 'styles.css'), 'w', encoding='utf-8') as file:
        file.write(css_content)

    print(f"Website files generated successfully in the '{output_folder}' directory.")

# Replace 'schools.xlsx' with the path to your Excel file
generate_website_from_excel('schools.xlsx')
