# Write HTML content to a file
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive Platform</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div id="app">
        <h1>Welcome to the Interactive Platform</h1>
        <div id="viewer-response"></div>
        <button id="startButton">Start Interaction</button>
    </div>

    <script src="script.js"></script>
</body>
</html>
"""

with open("index.html", "w") as file:
    file.write(html_content)
