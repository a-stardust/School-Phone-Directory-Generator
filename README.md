# School Phone Directory Generator

## 📌 Overview  
The **School Phone Directory Generator** is a Python-based tool that creates employee-specific phone directory webpages from CSV files. It allows users to upload CSV files containing school names and phone numbers, generating an HTML directory that enables easy dialing.

## 🚀 Features  
- **Automatic Webpage Generation**: Creates individual HTML pages for each uploaded CSV file.  
- **Central Index Page**: Generates a homepage with links to all employee-specific directories.  
- **Simple UI for Uploading CSV Files**: Uses a Tkinter-based file dialog to select CSV files.  
- **Direct Calling Feature**: Clickable phone numbers allow direct dialing from mobile devices.  

## 🛠️ Requirements  
Ensure you have the following installed:  
- Python 3.x  
- Required Python libraries:
  pip install pandas tkinter


## 📂 Folder Structure  
/School-Phone-Directory-Generator │-- webpages/ # Generated HTML files
│-- styles.css # CSS file for styling
│-- script.js # JavaScript for interactivity
│-- index.html # Homepage listing all directories
│-- generator.py # Main script for generating webpages


## 🔧 How to Use  
1. **Run the Script**  
python generator.py

2. **Select CSV Files**  
- A file dialog will appear; select one or more CSV files.  
- Ensure the CSV files contain columns:  
  ```
  School Name, Phone Number
  ```
3. **View the Generated Pages**  
- The script generates HTML pages in the `webpages/` folder.  
- Open `index.html` in a browser to access all directories.  

## 📝 CSV Format Example  
School Name,Phone Number
Green Valley High,9876543210
Sunrise Academy,8765432109
Blue Ridge School,7654321098


## 🖼️ Sample Output  
- **Homepage (`index.html`)**: Lists all generated directories.  
- **Employee-Specific Pages**: Show a list of schools with clickable phone numbers.  

## 🔗 License  
This project is open-source under the **MIT License**.  


