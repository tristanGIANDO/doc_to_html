import os, ast

def doc_to_web(file_path:str, delivery_path:str):
    """
    file_path (str): the source file
    delivery_path (str): the destination folder where to write HTML file.
    """
    html_content = """
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>DOCUMENTATION</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #f2f2f2;
            padding: 10px;
            text-align: center;
        }
        nav {
            background-color: #333;
            color: #fff;
            padding: 10px;
            text-align: center;
        }
        nav a {
            color: #fff;
            text-decoration: none;
            margin: 0 10px;
        }
        section {
            padding: 20px;
            max-width: 800px;
            margin: 0 auto;
        }
        footer {
            background-color: #f2f2f2;
            padding: 10px;
            text-align: center;
        }
    </style>
</head>
<body>
    <header>
        <h1>your tool</h1>
    </header>
    <nav>
        <a href="#">Home</a>
        <a href="#">Contact</a>
    </nav>
"""
    with open(file_path, 'r') as file:
        source_code = file.read()

    tree = ast.parse(source_code)

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            html_content += (f"<h2>DEF {node.name}</h2>")
            html_content += (f"<p>{eval(node.name).__doc__}</p>")

    html_content += """
<footer>
        <p>All rights reserved &copy; 2023 your tool</p>
    </footer>
</body>
</html>
"""

    # Chemin du fichier HTML à créer
    fichier_html = os.path.join(delivery_path, "index.html")

    # Écrire le contenu HTML dans le fichier
    with open(fichier_html, "w") as f:
        f.write(html_content)

    print(f"Le fichier '{fichier_html}' a été créé avec succès.")

if __name__=="__main__":
    doc_to_web(__file__, r"C:\Users\giand\OneDrive\Documents\packages\doc_to_web\dev\doc_to_web")
    # print(eval("doc_to_web").__doc__)