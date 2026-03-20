$git = "C:\Program Files\Git\cmd\git.exe"
$repo = "https://github.com/saowanlakn-droid/resume.git"

Write-Host "Using Git at: $git"

# Config
& $git config user.email "deploy@example.com"
& $git config user.name "Resume Deployer"

# Init
& $git init
& $git branch -M main

# Add
& $git add index.html style.css script.js "รูปบัณฑิต.jpg"
& $git commit -m "Deploy vibrant resume website"

# Remote
& $git remote remove origin 2>$null
& $git remote add origin $repo

# Push
Write-Host "Pushing to $repo..."
& $git push -u origin main
