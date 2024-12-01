from nbformat import NotebookNode

# Create a consolidated notebook
consolidated_nb = NotebookNode(cells=[], metadata={}, nbformat=4, nbformat_minor=4)

# Add cells from each executed notebook
for filename in os.listdir(local_directory):
    if filename.endswith('.ipynb'):
        file_path = os.path.join(local_directory, filename)
        with open(file_path) as f:
            nb = nbformat.read(f, as_version=4)
            consolidated_nb.cells.extend(nb.cells)

# Save the consolidated notebook
consolidated_path = os.path.join(local_directory, "Consolidated_Notebook.ipynb")
with open(consolidated_path, 'w') as f:
    nbformat.write(consolidated_nb, f)
print(f"Consolidated notebook saved to {consolidated_path}")
