'''
echo "# Firstgitcommand" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Barracudakun/Firstgitcommand.git
git push -u origin main
'''

git = "first git command"
print(git)

'''
(venv) seashore@Seas-MacBook-Air HW1 git_command % git status
On branch main
Your branch is up to date with 'origin/main'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   HW1_firstgitcommand.py

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .idea/

no changes added to commit (use "git add" and/or "git commit -a")
(venv) seashore@Seas-MacBook-Air HW1 git_command % git add  HW1_firstgitcommand.py
(venv) seashore@Seas-MacBook-Air HW1 git_command % git commit -m'update first git command'
[main b58be96] update first git command
 1 file changed, 4 insertions(+), 1 deletion(-)
(venv) seashore@Seas-MacBook-Air HW1 git_command % git push
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 8 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 367 bytes | 367.00 KiB/s, done.
Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (1/1), completed with 1 local object.
To https://github.com/Barracudakun/Firstgitcommand.git
   1d20526..b58be96  main -> main

'''