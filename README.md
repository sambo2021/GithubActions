# GithubActions
## if you did changes on branch for ex feature/anything and opened pr to main
### if you want to modify last commit only
#### locally on branch feature/anything do (git commit --amend -m "right modified commit") then (git push -f) this will rerun the orkflow of pr
### if you want to modify commit before before the last one
#### locally on branch feature/anything do (git rebase -i HEAD~3) then it opens vim and before the commit you want to modify replace the word "pick" with "reword" then save it the it opens again vim for you to modify the message itself then sve it then (git push -f)
