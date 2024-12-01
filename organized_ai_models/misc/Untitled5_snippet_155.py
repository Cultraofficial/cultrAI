# Write CSS content to a file
css_content = """
body {
    font-family: Arial, sans-serif;
    text-align: center;
    background-color: #f4f4f9;
}

#app {
    max-width: 600px;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ddd;
    border-radius: 8px;
    background-color: white;
}

button {
    padding: 10px 20px;
    font-size: 16px;
    margin-top: 20px;
    cursor: pointer;
}
"""

with open("style.css", "w") as file:
    file.write(css_content)
