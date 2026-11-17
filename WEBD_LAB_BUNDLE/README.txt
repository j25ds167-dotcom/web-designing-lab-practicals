WEB DESIGNING LAB - Aniket Chaudhary (J250212025)

1. PUSH TO GITHUB (one time)
   - Install Git, Node.js and GitHub CLI (gh).
   - In a terminal:  gh auth login      (log in as j25ds167-dotcom)
   - From this folder:  bash push.sh
   This creates Webd-exp-1 ... Webd-exp-12 under your account, pushes the code,
   does the branch + merge for Experiment 1, and turns on GitHub Pages.
   Sites go live 1-2 minutes later at https://j25ds167-dotcom.github.io/Webd-exp-N/
   (Experiments 8, 9, 12 are Node/MongoDB apps, so they have no GitHub Pages site.)

2. TAKE SCREENSHOTS
   Save them in the "screenshots" folder as exp<N>_<k>.png, e.g. exp1_1.png, exp1_2.png.
   The slot order for each experiment is the order of the placeholders in the PDF.

3. REBUILD THE PDF
   pip install reportlab pillow
   python3 make_pdf.py
   Screenshots found in the folder replace the placeholder boxes automatically.

4. Experiments 10 and 12: after you deploy (Netlify / Render / etc.), paste the URLs
   into content2.py (extra_links) and rebuild the PDF.
