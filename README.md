# AUGSD Time Table Project

- Make the fork (one time)
	- Press **Fork** button from [this](https://github.com/AdarshNandanwar/AUGSD-Project) account and select your account.
	- In your GitHub fork, press **Clone or Download** and copy the url.
	- Open the terminal and: `git clone <copied_url>`
	- `git remote add origin <copied_url>`
	- **IMPORTANT**: Create a branch development where you can do the changes , accepted changes will get merged with master branch
	- `git remote add upstream https://github.com/AdarshNandanwar/AUGSD-Project`
	- **IMPORTANT**: Do the following to disable push on upstream handle `git remote set-url --push upstream no_push`

- Submiting PR
	- `git add <filename>` or to add everything `git add .`
	- `git commit -m "<Commit msg>"`
	- Resolve merge conflicts (if any) 
	- `git push origin master`
	- On your GitHub development branch, press **Compare & pull request** and then **Create Pull Request** on next page
