"# git-course" 

Mkdir -p <local-path-to-repo>
cd <local-path-to-repo>
git init
echo "# git course demo" >> README.md
git add .

# optional commands:
# 1. If the folder owner is different from the user, add this:
git config --global --add safe.directory <local-path-to-folder>

# 2. If you test Git commands for the first time, also add this:
git config --global user.email "you@example.com"
git config --global user.name "Your Name"

git commit -m "first commit"
git branch -M main
Generating ssh_key to have a connection between local and remote repo:
Mkdir -p <local-path-to-.ssh floder>
cd <local-path-to-.ssh floder>
ssh-keygen -o 
Then id_rsa.pub is created in .ssh folder which we created open the .pub file to have key which begin with ssh_rsa and ends with email id copy this and go to the 
-> Github  Profile -> Settings -> SSH and GPG keys -> New SSH key -> Give title_name -> paste the key in Key_filed -> Add SSH key 

git remote add origin git@github.com:HARIKANCHANI/git-course.git
git push -u origin main
