# UniSA_ICT_2024_SP4_P3_ Project

## Repository Structure and Process Guide

Welcome to the UniSA_ICT_2024_SP4_P3_ project repository. This document provides guidelines for organising and maintaining the repository. It includes the folder structure, commit process, and naming conventions.

### Folder Structure

Our repository is organised as follows:

- root
  - .github/
    - workflows/ # GitHub Actions workflows
- Final Submission/
  - [files required to load KNIME pipeline]
    - 200k_blitz_rapid_classical_bullet.zip
    - Knime Pipeline final for Assessment 1c.knwf
    - opening_moves.csv
- Sprint 1/
  - [subfolders and files specific to Sprint 1]
  - Chess Pattern Recognition/
    - [subfolders and files related to chess pattern recognition]
- Sprint 2/
  - [subfolders and files specific to Sprint 2]
- Sprint 3/
  - [subfolders and files specific to Sprint 3]
- Sprint 4/
  - [subfolders and files specific to Sprint 4]
- .gitignore # Git ignore file
- README.md # Repository guide and structure

### Commit Process via VS Code

1. **Stage the Changes:**
   1. Go to the Source Control view by clicking the Source Control icon in the Activity Bar on the side of the window or by pressing Ctrl+Shift+G.
   2. You will see the list of files that have been changed under the "Changes" section.
   3. Hover over the file you want to stage and click the + icon to stage the changes. Alternatively, you can click the + icon next to the "Changes" header to stage all changes.
  
2. **Commit the Changes:**
   1. In the Source Control view, you will see a text box at the top where you can enter a commit message.
   2. Type a descriptive commit message that explains what changes you made.
   3. Click the checkmark icon (✔️) above the commit message box to commit the staged changes.

3. **Push the Changes to GitHub:**
   1. After committing, you need to push the changes to the remote repository.
   2. Click the ellipsis (...) in the Source Control view, then select Push.
      - Alternatively, open the Command Palette (Ctrl+Shift+P), type Git: Push, and select it.
   3. If this is the first time you are pushing to the repository, you might be prompted to authenticate with GitHub.

### Commit Process via Terminal

To ensure consistency and clarity in our repository, follow these steps when committing code:

1. **Navigate to the Correct Directory:**

   Ensure you are in the correct directory where your repository is located.

   ```bash
   cd path/to/your/repository

2. **Create/Move Files to the Appropriate Folder:**

   Organise your files into the correct folders based on the folder structure above.

   ```bash
   mkdir -p path/to/appropriate_folder
   mv your_file.ext path/to/appropriate_folder

3. **Stage the Changes:**
   Use the **'git add'** command to stage the files you want to commit.

   ```bash
   git add path/to/appropriate_folder/your_file.ext

4. **Commit the Changes:**
   Commit your changes with a clear and descriptive message.

   ```bash
   git commit -m "Add your_file.ext to appropriate_folder"

5. **Push the Changes:**
   Push the committed changes to the remote repository on GitHub.
   
   ```bash
   git push origin main

### Naming Conventions
- Folders: Use descriptive names for folders that indicate their content or purpose.
- Files: Use lowercase letters and hyphens to separate words (e.g., data-dictionary.ipynb).
