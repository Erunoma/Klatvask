# Make variables that sets the source, dir, repo and git 
$SourceDir = "Den IP vi bruger eller path"
$BackUpDir = "C:\Path\til\dir\"
$RepoPath = "https://github.com/Erunoma/Klatvask/tree/main/BackUpDev"
$RepoName = "Klatvask"
$GitUserName = "Det username vi bruger " #Måske det her skal ændres til Olivers eller den der har VM'en??? 
$GitToken = "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" #Samme med det her. Lige nu er det min token

# Create backup folder 
$TimeStamp = Get-Date -Format "yyyyMMdd" #Get the date + time for the timestamp 
$BackUpFolder = Join-Path -Path $BackUpDir -ChildPath "Backup_$TimeStamp" #

# Create backup folder cmd
New-Item -ItemType Directory -Path $BackUpFolder | Out-Null

# Copy WebSite files to BackUpFolder
Copy-Item -Path $SourceDir -Destination $BackUpFolder -Recurse -Force

# Copy DB files 
$DBpath = Join-Path -Path $Source -ChildPath "path-to-database.db" #Husk at vi skal indsætte den rigtige DB
$DBbackupPath = Join-Path -Path $BackUpFolder -ChildPath "path-to-database.db" #Igen husk vi skal indsætte den rigtige DB med navn 
Copy-Item -Path $DBpath -Destination $DBbackupPath

# Init new git-repo 
Set-Location $RepoPath
git init

# Add the backup folder to the Git repository set in the location above 
git add .

# Commit the changes
git commit -m "Backup Commmited"

# Push changes to GitHub
$GitRepoURL = "https://github.com/Erunoma/Klatvask/tree/main/BackUpDev.git"
git remote add origin $GitRepoURL
git push -u origin master

# Guide for afterwards:
# 1. Navigate to scheduled task
# 2. Navigate to "Create task"
# 3. Make a "Trigger" for a specific time
# 4. Make a new "Action" and select the script
# 5. Set conditions so it matches whatever
# 5. Set settings so it matches whatever 