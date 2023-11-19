# Git基本操作

## 学习网站

[Git学习](https://oschina.gitee.io/learn-git-branching/)

## Linux基本命令

```
# pwd	# 打印当前目录路径

# ls	# 展示当前目录列表
ls -a 	# 展示全部内容，包括隐藏文件
ls -l	# 以列表的形式展示内容

# clear	# 清除屏幕内容，保留了历史
# reset	# 重置，历史记录没了

# mkdir	# 创建一个文件夹
# rmdir	# 删除一个空的文件夹

# touch	# 创建文件
touch index.html

# rm	# 删除一个文件，获取文件夹
rm index.html	# 删除文件
rm js	# 删除空的js文件夹
rm -r css	# 递归删除一个文件夹

# mv	# 移动文件
mv index.html js	# 将文件移动到文件夹中
mv index1.html index2.html	# 将文件进行重命名

# cp 复制文件（cp）
cp index.html index2.html	# 复制index.html文件，命名为index2.html
cp -r css css02	# 如果复制的是文件夹，需要使用-r参数

# cat 	# 查看文件全部内容
cat index.html
# less	# 查看文件部分内容
less index.html
# :q	# 退出查看
```

## 基本初始化操作

1. 初始化git仓库 `git init`
2. 查看当前git仓库的状态 `git status`
3. 将当前文件添加到git的暂存区 `git add 文件名`
4. 将文件由暂存区提交到仓库区 `git commit -m '提交说明'`
5. 查看提交日志 `git log`

## 配置邮箱和用户名

如果是第一次使用git，会要求设置用户名和邮箱

1. 配置你的目标用户名 `git config user.name`
2. 配置你的目标邮箱名 `git config user.email`
3. 可以使用 `--global`参数，配置全局的用户名和邮箱名
4. 查看配置信息 `git config --list`

## 操作命令说明

### git add

* `git add --all`或 `git add -A`或 `git add .`添加所有文件
* `git add a.txt b.txt`同时添加两个文件
* `git add *.js`添加当前目录下所有的js文件

### git stash

`git stash` 是一个用于保存和恢复工作目录和暂存区中的修改的命令。它允许你将当前的工作状态保存起来，以便在稍后的时候重新应用这些修改。

#### 基本用法

1. **保存当前修改到堆栈：**

   ```bash
   git stash
   ```

   这会将工作目录和暂存区中的修改保存到一个新的 stash 记录中，并将你的工作目录重置为上一个提交的状态。
2. **查看保存的 stash 列表：**

   ```bash
   git stash list
   ```

   这会列出所有保存的 stash 记录。
3. **应用最新的 stash：**

   ```bash
   git stash apply
   ```

   这会重新应用最新的 stash 记录，并保留 stash 记录。
4. **应用指定的 stash：**

   ```bash
   git stash apply stash@{n}
   ```

   这会应用指定编号为 `n` 的 stash 记录。
5. **删除 stash 记录：**

   ```bash
   git stash drop
   ```

   这会删除最新的 stash 记录。

#### 示例

```bash
# 假设你正在进行一些修改，但需要切换到其他分支进行紧急修复

# 保存当前修改到 stash
git stash

# 切换到其他分支进行紧急修复

# 切回原分支

# 恢复之前保存的修改
git stash apply

# 或者，如果你希望删除 stash 记录
git stash drop

# 如果我想把未暂存的内容移动另一个已存在的分支
# 就需要先把内容暂存，切到新分支，释放暂存的内容
# 当你在当前分支上有未提交的修改，但需要切换到另一个分支时，可以使用 git stash 将当前的修改保存起来，以免影响分支切换
# 在另一个分支上完成一些工作后，你可能希望将之前保存的修改应用到当前分支上。这时就可以使用 git stash pop
git stash
git checkout my-branch
git stash pop
```

#### 注意事项

- `git stash` 是一个灵活的工具，允许你保存和应用工作目录和暂存区中的修改。它对于在进行切换分支或者处理其他任务时保存现场非常有用。
- 可以通过 `git stash save "message"` 来为 stash 记录添加一个描述性的消息。
- `git stash apply` 默认会应用最新的 stash 记录。如果你希望应用其他 stash 记录，需要提供相应的 stash 编号。

总的来说，`git stash` 是在处理多个任务时，暂时保存和恢复修改的有用工具。

### git commit

`git commit --amend` 是一个用于修改最近一次提交的 Git 命令。它允许你将暂存区中的修改添加到最近的提交中，或者修改提交的提交信息。

#### 基本用法

```bash
git commit --amend
```

这会打开一个文本编辑器，让你编辑最近一次提交的提交信息。你也可以使用 `-m` 选项直接在命令行中提供新的提交信息。

```bash
git commit --amend -m "New commit message"
```

#### 示例

1. **添加暂存区的修改到最近的提交：**

   ```bash
   # 先将修改添加到暂存区
   git add .

   # 然后执行 --amend
   git commit --amend
   ```

   这将打开文本编辑器，让你编辑提交信息或者直接保存关闭，添加的修改将会包含在最近一次提交中。
2. **直接修改最近一次提交的提交信息：**

   ```bash
   git commit --amend -m "New commit message"
   ```

   这将直接修改最近一次提交的提交信息，不需要打开文本编辑器。

#### 注意事项

- 使用 `git commit --amend` 时，确保你了解它的影响，因为这将修改最近的提交历史。不要在已经推送到共享仓库的提交上使用 `--amend`。
- 如果在提交中添加了暂存区的修改，新的提交将替代原来的提交，包括相同的提交哈希。
- 如果仅仅是修改提交信息，提交哈希值不会改变。

总体而言，`git commit --amend` 提供了一个方便的方法来调整最近一次提交的内容或提交信息。

**但如果已经 `push`了，需要 `-f`强行推送，但不建议这么做**

### git show

```bash
git show [commit_hash]
```

- `commit_hash` 是你要查看的提交的哈希值，可以是完整的哈希值或者是提交的前几个字符。

#### 示例

```bash
# 查看最新提交的详细信息
git show

# 查看特定提交的详细信息
git show abc123  # 其中 abc123 是提交的哈希值的前几个字符
```

#### 显示的信息包括

- **提交信息：** 包括作者、提交时间、提交的哈希值等。
- **修改的文件：** 显示哪些文件在该提交中发生了变化，以及具体的修改内容。

#### 注意事项

- 如果省略 `commit_hash`，`git show` 将显示最新提交的详细信息。
- `git show` 还可以用于显示标签、树对象等的详细信息，只需提供相应的对象的哈希值。

这个命令对于查看提交的详细内容很有用，特别是当你想要了解某个提交的具体变化时。

### git branch

`git branch` 命令用于列出、创建或删除分支。以下是一些常见的用法：

#### 列出本地分支

```bash
git branch
```

这会列出本地仓库中所有的分支，当前分支前会有一个星号(`*`)。

#### 创建新分支

```bash
git branch new_branch_name
```

这会在当前分支上创建一个名为 `new_branch_name` 的新分支，但并不会切换到这个新分支。

#### 切换到已存在的分支

```bash
git checkout existing_branch_name
```

或者，使用 `git switch`：

```bash
git switch existing_branch_name
```

这会将 HEAD 移动到 `existing_branch_name` 指定的分支。

#### 创建新分支并切换到该分支

```bash
git checkout -b new_branch_name
```

或者，使用 `git switch`：

```bash
git switch -c new_branch_name
```

这会创建一个名为 `new_branch_name` 的新分支，并将 HEAD 切换到这个新分支。

#### 删除分支

```bash
git branch -d branch_name
```

这会删除名为 `branch_name` 的本地分支。如果分支未合并到当前分支，使用 `-d` 会报错，此时可以使用 `-D` 强制删除。

#### 删除一个远程分支

```
git push origin --delete my-branch
```

你也可以：

```
git push origin: my-branch
```

### git checkout

作用：暂存区内容恢复到工作区

* `git checkout 1.txt`将暂存区中文件恢复到工作区

### git status

* `git status -s`简化日志输出格式

### git log

* `git log`只能查看当前head以及以前的日志
* `git log --oneline`简洁的日志信息
* `git reflog`查看所有的提交变更日志

### git reset

版本回退，将代码恢复到已经提交的某一个版本中

* `git reset --hard 版本号`将代码回退到一个指定版本
* `git reset --soft` 是一个用于回退提交并保留工作目录和暂存区中的修改的 Git 命令。这个命令允许你撤销最近的提交，但保留对这些更改的跟踪，以便你可以在进行调整后重新提交。
* 如果你想完全丢弃最近的提交，包括工作目录和暂存区中的修改，可以使用 `--hard` 选项，但在使用时要小心，因为它会丢失未保存的更改。
* ```
  # 我想用远程分支覆盖掉我本地的分支
  git fetch	# 从远程仓库获取最新的变更，但不会自动合并到当前分支。这确保了你获取了远程仓库的最新状态。
  git checkout master	# 切换到本地的 master 分支。确保你在要重置的目标分支上。
  git reset --hard origin/master	# 使用 --hard 选项重置本地分支到与远程分支 (origin/master) 一致的状态，包括工作目录和暂存区都会被覆盖。这样，你的本地分支就与远程分支一致了。
  # 如果你的本地分支与远程分支有不同的提交历史，执行 git reset --hard 会使得本地分支与远程分支完全一致，可能会导致冲突。
  # 如果你只是想将本地分支更新到最新，而不想删除本地分支上的所有未提交的修改，你可以使用 git pull 或者 git merge origin/master。这样可以合并远程分支的变更，而不会覆盖本地未提交的修改。
  ```
* ```
  # 我想丢弃本地未提交的变化
  # 如果你只是想重置源（origin）和本地（local）之间的一些提交
  # one commit
  git reset --hard HEAD^
  # two commits
  git reset --hard HEAD^^
  # four commits
  git reset --hard HEAD~4
  # or
  git checkout -f

  # 重置某个特殊的文件
  git reset filename
  ```

### git fetch

`git fetch` 是一个用于从远程仓库获取更新的命令。它会将远程仓库的新提交、分支和标签信息下载到本地仓库，但不会自动合并或修改你的工作目录。

使用 `git fetch` 的目的是将远程仓库的变更同步到本地，以便你可以查看它们并决定是否合并到你的本地分支。与 `git pull` 不同，`git fetch` 不会自动合并远程变更，而是将其保存在一个称为 "origin/master"（或其他远程名称和分支名的组合）的引用中。

#### 使用方式

```bash
git fetch [remote_name]
```

- `remote_name`：远程仓库的名称，通常为 `origin`。如果省略，则默认使用配置中的默认远程仓库。

#### 示例

```bash
git fetch
```

这会从默认远程仓库（通常是 `origin`）获取所有分支的更新。

```bash
git fetch origin
```

这会从名为 `origin` 的远程仓库获取所有分支的更新。

#### 注意事项

1. `git fetch` 不会修改你的工作目录，它只是获取远程仓库的信息。
2. 使用 `git fetch` 后，你可以通过 `git log origin/master` 查看远程分支的提交历史，或者通过 `git diff master..origin/master` 查看本地和远程分支之间的差异。
3. 如果你想要将远程变更合并到你的本地分支，可以使用 `git merge` 或者 `git rebase`。

总的来说，`git fetch` 是一个安全的获取远程仓库变更的方式，它使你能够在决定合并之前审查远程仓库的更新。

`git fetch` 不会直接影响你的本地分支或工作目录。它的主要作用是从远程仓库中获取最新的提交、分支和标签信息，但不会修改你的工作目录或当前分支。它将远程仓库的变更保存在一个特殊的引用中，通常是 `origin/master`（如果默认远程仓库是 `origin`）。

理解 `origin/master` 需要考虑两个方面：`origin` 和 `master`。

1. **`origin`：** 是默认的远程仓库的名称。在 Git 中，远程仓库的别名通常被称为 `origin`，但实际上，它只是一个名称，你可以根据需要选择不同的名称。当你克隆一个远程仓库时，默认情况下会创建一个指向该远程仓库的别名为 `origin` 的远程仓库。你可以通过 `git remote -v` 命令查看远程仓库的别名。
2. **`master`：** 是远程仓库的分支名。在 `origin/master` 中，`master` 是远程仓库中的一个分支。它表示了 `origin` 远程仓库的 `master` 分支。

所以，`origin/master` 表示你本地仓库中对 `origin` 远程仓库的 `master` 分支的引用。这个引用保存了远程仓库的 `master` 分支的当前状态，但它并不是一个本地分支，不能被直接修改。

当你执行 `git fetch` 时，Git 会更新 `origin/master` 的引用，以反映远程仓库的最新状态。你可以使用这个引用来查看远程仓库的 `master` 分支的提交历史，进行比较，或者进行其他与远程仓库相关的操作。

**示例：**

```bash
# 执行 git fetch 以更新远程仓库的信息
git fetch

# 查看远程仓库的分支信息，包括 origin/master
git branch -r
```

总的来说，`origin/master` 是一个本地引用，用于跟踪 `origin` 远程仓库的 `master` 分支的状态。这样的引用使得你可以在本地查看和比较远程仓库的分支信息，而不必立即合并这些变更。

在执行 `git fetch` 之后，你可以查看远程分支的更新，但这些更新并不会自动合并到你的本地分支。如果想要将远程仓库的变更合并到本地分支，你需要使用 `git merge` 或者 `git rebase`。

**示例**

```bash
# 获取远程仓库（默认为origin）的最新信息
git fetch

# 查看远程分支的更新，不会影响本地分支
git log origin/master
```

`git fetch` 的安全性在于，它允许你在决定是否合并远程变更之前，先查看和审查这些变更。**相比之下，`git pull` 会自动将远程变更合并到当前分支，可能会导致冲突或其他问题。**

如果你确定要将远程仓库的变更合并到本地分支，可以使用 `git merge` 或者 `git rebase`：

```bash
# 将远程分支合并到当前分支
git merge origin/master

# 或者使用 rebase
git rebase origin/master
```

总体来说，`git fetch` 是一个相对安全的操作，它使你有机会审查远程仓库的变更，并决定何时以及如何将这些变更合并到你的本地分支。

### git merge

`git merge` 是一个用于合并分支的 Git 命令。合并是将两个分支的历史和更改集成到一个新的提交中的过程。以下是一些 `git merge` 的基本用法和示例：

#### 基本用法

1. **合并分支到当前分支：**

   ```bash
   git merge branch_name
   ```

   这会将名为 `branch_name` 的分支合并到当前所在的分支。
2. **合并分支并创建合并提交：**

   ```bash
   git merge --no-ff branch_name
   ```

   这会执行合并并创建一个新的合并提交，即使可以进行快进合并（Fast-forward merge）。

#### 示例

1. **合并分支到当前分支：**

   ```bash
   # 切换到目标分支
   git checkout main

   # 合并 feature 分支到 main 分支
   git merge feature
   ```

   这将把 `feature` 分支的更改合并到 `main` 分支。
2. **合并分支并创建合并提交：**

   ```bash
   # 切换到目标分支
   git checkout main

   # 合并 feature 分支并创建合并提交
   git merge --no-ff feature
   ```

   这会创建一个新的合并提交，即使可以进行快进合并。

#### 注意事项

- 如果两个分支的更改没有冲突，Git 将尝试使用快进合并（Fast-forward merge）。这种情况下，分支指针会直接移动到目标分支，而不会创建新的合并提交。
- 如果两个分支的更改有冲突，Git 会提示解决冲突，并要求手动解决。解决冲突后，可以使用 `git add` 和 `git commit` 完成合并。
- 使用 `--no-ff` 选项创建合并提交时，会保留合并的历史，即使可以进行快进合并。
- 在执行合并之前，建议使用 `git fetch` 确保你的本地仓库和远程仓库的信息是最新的。

总的来说，`git merge` 是将两个分支的更改合并到一个分支的常见操作。在进行合并时，请确保你理解并确认将哪个分支合并到哪个分支，并时刻注意潜在的冲突。

### git rebase

`git rebase` 是一个用于将一个分支的提交移至另一个分支上的命令。它与 `git merge` 有所不同，`git rebase` 的主要优势在于创建一个线性的提交历史，避免了合并提交所带来的额外的合并提交节点。

#### 基本用法

1. **将当前分支变基到目标分支：**

   ```bash
   git rebase target_branch
   ```

   这会将当前分支的提交逐个应用到目标分支上，创建一个新的提交历史。
2. **交互式变基（Interactive Rebase）：**

   ```bash
   git rebase -i target_branch
   ```

   这会打开一个交互式的编辑器，允许你在变基过程中编辑、删除、合并提交。
3. 合并多个提交：即将之后的提交全部合并到第一个提交里

   ```
   git rebase -i HEAD~3
   git rebase -i [committed version]
   ```

#### 示例

1. **将当前分支变基到目标分支：**

   ```bash
   # 切换到目标分支
   git checkout target_branch

   # 执行变基
   git rebase target_branch
   ```

   这将把当前分支的提交逐个应用到 `target_branch` 上。
2. **交互式变基：**

   ```bash
   # 切换到目标分支
   git checkout target_branch

   # 执行交互式变基
   git rebase -i target_branch
   ```

   这会打开一个编辑器，你可以在编辑器中选择要保留、修改或删除的提交。

#### 注意事项

- `git rebase` 可能会导致提交历史的改变，因此不建议对已经推送到共享仓库的提交进行变基，以避免对他人的工作产生负面影响。
- 如果在变基的过程中发生冲突，你需要解决这些冲突，并使用 `git rebase --continue` 继续变基。
- 使用交互式变基时，谨慎编辑提交。在编辑器中可以选择 "reword"、"edit"、"squash" 等选项，具体操作会根据你的选择产生不同的效果。

总体而言，`git rebase` 是一个强大的工具，可以用于创建更整洁的提交历史，但在使用时需要谨慎，避免对已共享的提交历史造成混乱。

## 操作步骤

### 创建项目

在系统中创建一个文件夹，并在这个文件夹中，创建一个简单的程序或项目

### 忽略文件

在 `.gitignore`文件中，你可以指定哪些文件或目录应该被Git忽略，不纳入版本控制。`.gitignore`文件使用简单的模式匹配规则来描述要忽略的文件或目录。以下是一些常见的 `.gitignore`规则：

1. 忽略特定文件：

   ```
   filename.txt
   ```
2. 忽略所有文件以及某个目录：

   ```
   # 忽略所有文件
   *
   # 但不要忽略目录
   !directory/
   ```
3. 使用通配符：

   ```
   # 忽略所有以.log结尾的文件
   *.log

   # 忽略所有名为temp的文件夹及其内容
   temp/
   ```
4. 忽略特定目录下的特定文件：

   ```
   # 忽略assets目录下的所有.mp3文件
   assets/*.mp3
   ```
5. 忽略所有文件夹下的特定文件：

   ```
   # 忽略所有的node_modules文件夹及其内容
   node_modules/
   ```
6. 忽略文件或目录中的特定字符：

   ```
   # 忽略所有带有test的文件或目录
   *test*
   ```

注意：

- `.gitignore`文件中的每一行都描述一个要忽略的规则。
- 你可以使用 `#`来添加注释。
- 你可以在 `.gitignore`文件中使用相对路径或者绝对路径。

请根据你的项目需求调整 `.gitignore`文件，确保忽略不必要的文件和目录。如果你的 `.gitignore`文件更改后不生效，可以尝试清除Git缓存，然后再次提交：

```bash
git rm -r --cached . # 清楚Git缓存
git add .
git commit -m "Updated .gitignore"
```

### 初始化仓库

在Git中，要初始化一个新的仓库，你可以使用 `git init`命令。以下是在命令行中初始化一个新仓库的基本步骤：

1. 打开命令行终端。
2. 进入到你想要初始化为Git仓库的目录。可以使用 `cd`命令切换目录，例如：

   ```bash
   cd /path/to/your/directory
   ```
3. 使用以下命令初始化一个新的Git仓库：

   ```bash
   git init
   ```

   这会在当前目录下创建一个名为 `.git`的子目录，这个子目录包含了Git仓库的所有必要文件。
4. 如果一切顺利，你将看到一条消息，表示Git仓库已成功初始化。

   ```bash
   Initialized empty Git repository in /path/to/your/directory/.git/
   ```

   这就完成了仓库的初始化过程。**仓库是在程序中被Git主动追踪的一组文件，Git用来管理仓库的文件都存储在隐藏的.git/中，你根本不需要与这个目录打交道，但千万别删除这个目录，否则将丢弃项目的所有历史记录**

此时，你可以开始将文件添加到仓库并进行提交。例如：

```bash
git add .
git commit -m "Initial commit"
```

以上步骤将所有文件添加到Git仓库并创建了一个初始的提交。从这一点开始，你可以在项目中进行更多的修改、添加、提交等操作。

需要注意的是，如果你想要克隆一个已存在的远程仓库，可以使用 `git clone`命令，而不是 `git init`。`git clone`会复制整个远程仓库到本地。

### 克隆一个远程仓库

要克隆一个已存在的远程仓库，可以使用 `git clone`命令。以下是基本的克隆操作步骤：

1. 打开命令行终端。
2. 使用以下命令进行克隆，其中 `<repository-url>`是远程仓库的URL，可以在远程仓库的页面上找到：

   ```bash
   git clone <repository-url>
   ```

   例如，如果你要克隆GitHub上的一个仓库，命令可能类似于：

   ```bash
   git clone https://github.com/example/repository.git
   ```

   如果你使用SSH密钥进行认证，你可以使用SSH URL：

   ```bash
   git clone git@github.com:example/repository.git
   ```
3. 执行克隆命令后，Git会自动将远程仓库的内容复制到本地，并在当前目录下创建一个与远程仓库同名的文件夹。
4. 进入克隆下来的目录：

   ```bash
   cd repository
   ```

   如果你的远程仓库是私有的并使用SSH进行认证，你可能需要在克隆时提供SSH密钥。

这样，你就成功克隆了一个已存在的远程仓库。在克隆后，你可以开始在本地进行开发，并使用Git进行版本控制。**克隆操作会自动将远程仓库的所有分支和历史记录复制到本地。**

在执行 `git clone`命令时，Git会将远程仓库的整个历史记录、所有分支和文件都复制到本地计算机。这确保了你在本地拥有远程仓库的完整副本，包括所有的提交记录、分支、标签等信息。

具体来说，克隆操作会做以下几个主要的事情：

1. **复制历史记录：** Git会将远程仓库的所有提交历史记录（包括每个提交的更改）复制到本地。这样，你就能在本地查看整个项目的演变历程。
2. **复制分支：** 如果远程仓库有多个分支，`git clone`会在本地创建与远程仓库相同的分支，并将这些分支的状态和历史记录一并复制过来。
3. **设置远程：** Git会自动为你的本地仓库设置一个名为"origin"的远程，指向克隆时指定的远程仓库地址。这使得你可以方便地与远程仓库进行交互，例如推送变更或者拉取最新的更改。

总之，通过克隆操作，你可以在本地获得一个与远程仓库一样的完整副本，这使得你可以在本地进行开发、修改，然后通过Git进行版本控制和与其他开发者共享你的变更。

### 检查状态

在Git中，你可以使用 `git status`命令来检查当前工作目录的状态。`git status`会显示已修改（或未跟踪）的文件，以及这些文件与之前提交的状态之间的差异。

要检查Git仓库的状态，按照以下步骤执行：

1. 打开命令行终端。
2. 进入你的Git仓库所在的目录，例如：

   ```bash
   cd /path/to/your/repository
   ```
3. 运行以下命令：

   ```bash
   git status
   ```

   这将显示有关你的工作目录和暂存区的状态信息，包括已修改的文件、已暂存的文件以及未跟踪的文件等。

示例输出可能如下：

```bash
On branch master
Your branch is up to date with 'origin/master'.

Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

    modified:   myfile.txt

no changes added to commit (use "git add" and/or "git commit -a")
```

这个示例告诉你当前所在的分支（`master`），并显示了一个已修改的文件（`myfile.txt`）。此外，还提供了一些建议，如何将修改的文件添加到暂存区或者放弃工作目录中的修改。

通过定期运行 `git status`，你可以随时了解你的工作目录和仓库的状态，以便在需要时执行适当的Git命令。

### 将文件加入仓库

将文件加入Git仓库的过程通常包括两个步骤：

1. **将文件添加到暂存区：** 使用 `git add`命令将修改的文件或新文件添加到Git的暂存区。暂存区是一个缓冲区，用于存储即将提交的更改。

   ```bash
   git add filename
   ```

   如果你想要添加所有修改过的文件，可以使用以下命令：

   ```bash
   git add .
   ```

   这将添加所有当前目录及其子目录下的修改文件。
2. **提交更改到仓库：** 使用 `git commit`命令提交暂存区的更改到仓库。提交时，你需要提供一个简短的提交消息，描述这次提交的目的。

   ```bash
   git commit -m "Your commit message"
   ```

   这将创建一个新的提交，包含了你在暂存区中添加的文件。提交是Git仓库中的一个快照，用于记录文件的状态。

综合起来，如果你有一个新的文件或者对已有文件进行了修改，你可以按照以下步骤将文件加入仓库：

```bash
# 将文件添加到暂存区
git add filename

# 或者添加所有修改的文件
git add .

# 提交更改到仓库
git commit -m "Your commit message"
```

这样，你的更改就被记录到Git仓库中了。注意，提交是本地的操作，如果你想将更改推送到远程仓库，还需要使用 `git push`命令。

### 查看提交历史

要查看Git仓库的提交历史，你可以使用 `git log`命令。`git log`会显示按时间顺序列出的每个提交的详细信息，包括提交哈希、作者、日期、提交消息等。

以下是基本的 `git log`命令：

```bash
git log
```

这将显示整个提交历史，最新的提交会显示在最上面。你可能需要按下空格键来向下滚动，按 `q`键退出查看。

`git log`还有一些常用的选项，以便你可以按照自己的需求定制查看：

- `-n` 或 `--max-count`: 限制显示的提交数量，例如，`git log -n 5`只显示最近的5个提交。
- `--oneline`: 以一行的方式显示每个提交，只显示提交哈希和提交消息。
- `--graph`: 以图形方式显示分支和合并历史。
- `--author`: 通过作者过滤提交历史，例如，`git log --author="John"` 只显示由"John"提交的历史。
- `--since` 和 `--until`: 通过时间过滤提交历史，例如，`git log --since="2022-01-01"` 只显示从2022年1月1日以后的提交。

以下是一些示例：

```bash
# 显示简短的提交历史
git log --oneline

# 限制显示最近的3个提交
git log -n 3

# 显示图形化的提交历史
git log --graph

# 显示指定作者的提交历史
git log --author="John"

# 显示从某个日期以来的提交历史
git log --since="2022-01-01"
```

`git log`的选项很多，可以根据你的需求选择适当的选项来查看提交历史。

### 第二次提交

如果我们在文件中加入了新的修改，我们此时再用 `git status`查看项目的状态，将发现GIt注意到了这个文件发生的变化。

可以使用 `git commit -am` 这个快捷方式，它允许你在一次命令中完成两个步骤：将所有已经跟踪的文件的修改加入暂存区，并提交这些更改。

具体而言，这个命令包括以下两个操作：

1. `-a` 选项：告诉 Git 将所有已经跟踪的文件的修改都加入到暂存区。这样，你不需要使用 `git add` 命令分别添加修改的文件。
2. `-m` 选项：后接一个提交消息，用于描述这次提交的目的。

示例：

```bash
git commit -am "Your commit message"
```

需要注意的是，这个命令只对已经被 Git 跟踪（已经被添加到版本控制的）的文件有效。如果有新建的文件没有被跟踪，或者有删除的文件，需要使用 `git add` 命令将它们加入到暂存区。

使用 `-am` 可以简化一些简单的提交过程，但请注意仍然要注意提交的内容是否符合你的意图，以免出现不必要的提交。

然后再使用 `git status`会发现已被提交到仓库，工作目录是干净的。

当你使用 `git commit -am` 提交后，你可以使用 `git log --oneline` 查看简短的提交历史。以下是一个示例：

假设你有两个文件：`file1.txt` 和 `file2.txt`，并且进行了一次提交：

```bash
# 提交文件修改
git commit -am "Add file1.txt and file2.txt"
```

然后运行 `git log --oneline`：

```
abcdef1 (HEAD -> main) Add file1.txt and file2.txt
```

这里的 `abcdef1` 是提交的哈希值（实际的哈希值可能不同），`HEAD -> main` 表示当前所在的分支为 `main` 分支。提交消息是 "Add file1.txt and file2.txt"。

如果你之前已经有过其他提交，`git log --oneline` 的输出可能会显示多个提交记录，每个记录占据一行，最新的提交在最上面。

### 撤销更改

`git checkout` 命令在Git中有不同的用途，具体取决于你想要执行的操作。以下是几种常见的用法：

1. **切换分支：**

   ```bash
   git checkout branch_name
   ```

   这会将你的工作目录和暂存区切换到指定分支，使你能够开始在该分支上工作。在较新版本的Git中，建议使用 `git switch`命令来切换分支。
2. **创建新分支并切换到该分支：**

   ```bash
   git checkout -b new_branch_name
   ```

   这会创建一个新分支 `new_branch_name` 并将工作目录切换到这个新分支。在较新版本的Git中，建议使用 `git switch -c new_branch_name`来创建并切换分支。
3. **撤销工作目录中的修改（撤销未暂存的更改）：**

   ```bash
   git checkout -- filename
   ```

   这将丢弃工作目录中对指定文件的更改，恢复到最后一次提交的状态。这个命令会覆盖工作目录中的更改，请谨慎使用。
4. **切换到特定提交（分离头状态）：**

   ```bash
   git checkout commit_hash
   ```

   这会将你的HEAD指向指定的提交，使你处于“分离头”状态，这意味着你不处于任何分支上。在这种状态下，你可以查看特定提交的内容，但不应该进行更改。在需要时，可以创建新分支以保存这个状态。

需要注意的是，随着Git版本的更新，`git switch` 和 `git restore` 等命令逐渐替代了 `git checkout` 的一些用法，因此在新项目或更新的Git环境中，可能更推荐使用新的命令。

其中，撤销工作目录中的修改通常涉及到两个Git命令：`git checkout` 和 `git restore`。在较新版本的Git中，`git restore`被认为是更安全的替代品，特别是在撤销未暂存的更改方面。以下是详细说明如何使用这两个命令来撤销工作目录中的修改：

### 撤销未暂存的更改

如果你对某个文件做了修改但尚未将其添加到暂存区，可以使用以下命令来撤销这些未暂存的更改：

使用 `git restore`：

```bash
git restore filename
```

或者，使用 `git checkout`：

```bash
git checkout -- filename
```

这两个命令的效果相似，都会将文件恢复到最后一次提交的状态。

#### 撤销已暂存的更改

如果你已经使用 `git add` 将文件添加到了暂存区，但又希望将其撤销，可以使用 `git restore`：

```bash
git restore --staged filename
```

这会将文件从暂存区移除，但保留在工作目录中的更改。

#### 撤销所有未暂存的更改

如果你希望撤销所有未暂存的更改，可以使用 `git restore`：

```bash
git restore --source=HEAD --staged --worktree --recursive .
```

这会将所有未暂存的更改恢复到最后一次提交的状态。

请注意，以上命令都需要小心使用，确保你真的想要丢弃这些更改，因为它们会永久性地删除工作目录中的更改。在执行这些命令之前，最好先使用 `git status` 检查一下当前的工作目录状态，确保你不会丢失任何重要的更改。

#### 撤销已暂存的更改后，是否还需要再用一次git restore来讲工作目录中的更改恢复到最后一次的提交状态？

不需要再用一次 `git restore` 来将工作目录中的更改恢复到最后一次提交的状态。当你使用 `git restore --staged filename` 来撤销已暂存的更改时，Git会将该文件从暂存区移除，但工作目录中的修改并不受影响，仍然保留在那里。

如果你想同时撤销暂存区和工作目录中的更改，可以使用以下命令：

```bash
git restore --source=HEAD --staged --worktree --recursive .
```

这个命令会将所有未暂存的更改都撤销，包括从暂存区移除的更改，将工作目录中的文件恢复到最后一次提交的状态。

总结：

- `git restore --staged filename` 撤销已暂存的更改，将文件从暂存区移除。
- `git restore --source=HEAD --staged --worktree --recursive .` 同时撤销暂存区和工作目录中的未暂存更改，将所有文件恢复到最后一次提交的状态。

### 检出以前的提交

在Git中，你可以使用 `git checkout` 或者 `git switch` 命令来检出（checkout）以前的提交，以查看或者回滚到过去的状态。但请注意，`git checkout` 在较新版本的Git中已经逐渐被 `git switch` 和 `git restore` 替代，尤其在处理分支切换时。

以下是一些例子，演示如何检出以前的提交：

#### 使用 `git switch` 检出以前的提交

1. 查看提交历史，获取你想要检出的提交的哈希值（commit hash）：

   ```bash
   git log --oneline
   ```
2. 使用 `git switch` 切换到特定的提交：

   ```bash
   git switch commit_hash	# hash的前6位
   ```

   或者，如果你使用较老版本的Git，你可以使用 `git checkout`：

   ```bash
   git checkout commit_hash	# hash的前6位
   ```
3. 如果你只是想查看过去的状态，可以创建一个临时分支，以免影响当前分支：

   ```bash
   git switch -c temp_branch commit_hash
   ```

#### 使用 `git restore` 恢复到过去的状态

如果你只是想查看以前的状态而不需要创建分支，可以使用 `git restore` 恢复文件到特定提交的状态：

```bash
git restore --source=commit_hash --worktree --recursive .
```

这将工作目录中的所有文件恢复到指定提交的状态。

请注意，这些操作都是只读的，不会对当前分支的状态产生影响，但如果你想要在过去的状态上继续工作，最好创建一个新分支。如果需要回滚到以前的状态并提交这个更改，你可以使用 `git revert` 或者 `git reset` 命令，但要小心，因为它们会改变提交历史。

#### git reset

`git reset` 是一个用于移动 HEAD 和分支引用的命令，它可以用于回滚提交、取消已暂存的更改，或者移动分支引用。下面是一些常见的 `git reset` 用法和案例：

##### 1. 回滚到过去的提交

```bash
# 回滚到某个提交，保留本地修改但将它们标记为未暂存状态
git reset commit_hash
```

这会将 HEAD 移动到指定的提交，但保留工作目录中的修改。

```bash
# 回滚到某个提交，并且丢弃本地修改
git reset --hard commit_hash
```

这会将 HEAD 和工作目录都回滚到指定的提交，本地的修改将被丢弃。

##### 2. 取消已暂存的更改

```bash
# 取消所有已暂存的更改，但保留工作目录中的修改
git reset
```

这会将已暂存的更改移回工作目录，并保留在工作目录中。

```bash
# 取消对某个文件的已暂存更改
git reset filename
```

##### 3. 移动分支引用

```bash
# 移动分支引用到某个提交，但保留工作目录中的修改
git reset commit_hash
```

这会将分支引用（例如，`main` 分支）移动到指定的提交，但保留工作目录中的修改。

```bash
# 移动分支引用到某个提交，并且丢弃本地修改
git reset --hard commit_hash
```

这会将分支引用移动到指定的提交，并且丢弃工作目录中的修改。

##### 注意事项

- `git reset` 会改变提交历史，因此在公共分支上使用时需要小心。
- 如果你已经将某个提交推送到远程仓库，不要在该提交之后使用 `git reset --hard`，因为这会导致分支历史不一致。
- 如果你只是想撤销最新的提交，而不修改提交历史，可以使用 `git revert`。

请确保在使用 `git reset` 之前，仔细考虑其影响，并确保备份重要的更改。

### 删除仓库

要删除Git仓库，你可以通过直接删除与仓库关联的本地目录来实现。以下是删除Git仓库的步骤：

#### 1. 删除本地仓库目录

找到你的本地仓库目录，然后使用操作系统的文件管理工具（如文件资源管理器或终端）删除整个目录。

在终端中，可以使用 `rm` 命令（Unix/Linux/macOS）或 `rmdir` 或 `rd` 命令（Windows）：

```bash
# Unix/Linux/macOS
rm -rf /path/to/your/repository

# Windows
rmdir /s /q C:\path\to\your\repository
```

#### 2. 删除远程仓库（可选）

如果你的仓库是托管在远程仓库服务上（如GitHub、GitLab、Bitbucket等），你可能还想要删除远程仓库。但请注意，删除远程仓库可能需要管理员权限，具体步骤取决于你使用的远程仓库服务。

例如，在GitHub上，你可以进入仓库的设置（Settings），然后在底部找到"Delete this repository"选项。

#### 注意事项

1. 删除仓库是不可逆的操作，请确保你真的想要删除仓库，并且已经备份了重要的数据。
2. 如果仓库是一个共享的仓库，确保通知其他协作者在仓库删除之前拉取最新的更改。
3. 如果你删除了远程仓库，请确保你有足够的权限进行此操作，以免造成不必要的问题。

请根据实际情况慎重操作。如果你只是想删除本地仓库的提交历史而保留文件，你可以考虑使用 `git rm` 和提交一个新的初始提交，以创建一个全新的仓库。

#### 删除仓库提交记录

```
git status	# 查看仓库状态
rm -f .git	# 如果仓库的历史记录被你搞乱了，且无法恢复，参与项目开发的只有你一个人，可继续使用这些文件，但是要将项目的历史记录删除，也就是删除.git，这不会影响任何文件的当前状态，只会删除所有的提交
git status	# 再次查看仓库的状态
git init
git status
git add .
git commit -m ''
git status
```

### 与远程仓库同步

当你修改了本地文件，并希望将这些修改同步到远程仓库时，可以按照以下详细步骤操作：

#### 步骤 1: 查看本地修改状态

```bash
git status
```

这会显示工作目录中已修改但未暂存的文件，以及已暂存但未提交的文件。

#### 步骤 2: 添加修改到暂存区

```bash
git add .
```

这将把所有修改的文件添加到Git的暂存区。你也可以使用 `git add filename` 来添加指定文件。

#### 步骤 3: 提交本地修改

```bash
git commit -m "Your commit message"
```

这会创建一个新的提交，包含了你刚刚添加到暂存区的文件。

#### 步骤 4: 拉取远程仓库的最新更改

```bash
git pull origin branch_name
```

这会拉取远程仓库指定分支（`branch_name`）的最新更改到本地。如果有冲突，需要解决冲突。

#### 步骤 5: 推送本地修改到远程仓库

```bash
git push origin branch_name
```

这会将你的本地修改推送到远程仓库的指定分支。

如果是首次推送，你可能需要设置上游分支：

```bash
git push -u origin branch_name
```

这将把本地分支与远程分支关联，之后你可以使用 `git push` 和 `git pull` 进行更方便的同步。

#### 注意事项：

- 在整个过程中，确保你处于正确的分支上（使用 `git branch` 查看分支）。
- 如果在 `git pull` 时遇到冲突，需要解决冲突后再次执行 `git add` 和 `git commit`。
- 在执行 `git push` 之前，确保你有推送到远程仓库的权限。
- 请定期使用 `git pull` 以确保你的本地分支是最新的。

通过以上步骤，你可以将本地修改同步到远程仓库。

### 多人任务

1. 分配任务
2. `git checkout`	切换分支
3. 写代码
4. `git add`	将文件添加到暂存区
5. `git commit`	将文件进行提交
6. `git fetch`	拉取远程仓库的更新到本地，不会修改工作区
   1. ```git
      git checkout your_feature_branch
      git fetch origin master
      git merge origin/master
      ```
7. `git rebase origin/master`	变基，将 `master`分支的更新并入当前分支，不会留下记录
   1. 如果存在冲突，解决冲突
8. 如果是第一次提交，`git push --set-upstream origin <分支名>`
   1. 这个命令的目的是将当前分支推送到远程仓库，并将远程分支设置为当前分支的上游分支（upstream）。这样一来，在以后的 `git pull` 或者 `git push` 操作时，Git 将自动使用正确的远程分支。
   2. `git push --set-upstream` 也可以简写为 `git push -u`：`git push -u origin your_branch`
9. 如果不是第一次提交，`git push -f`
   1. 对于普通的提交来说，是不需要进行强制推送的
   2. 但因为如果我们采用了 `rebase`的方法去合并 `master`上的更新，会改变当前分支的历史记录，从而与远程仓库的历史记录不一致，直接push会报错，因此需要用 `git push -f`强制推送，让本地副本覆盖远程副本
   3. 首先，为了保护项目代码以及提交历史的完整性，主仓库主分支一般会设置为保护分支，禁止直接往里面 `push`内容。所有更新都要通过 `pull request`从程序员个人的开发分支合进去。很显然，连普通推送都不允许，更不用说强制推送了，这个功能在主分支绝对是禁掉的。但是对于个人的开发分支来说，`rebase `结合 `push-f`是一个很有用的工具
   4. 当你想让自己的分支合入 `master`上的最新代码，而不留下难看的 `merge`记录，或者想合并自己分支上的多个 `commit`，让記彔更干浄一些，都可以用 `git rebase`。因为 `rebase`会无痕修改本地仓库的历史记录，只能通过强制推送的方式去覆盖远程仓库。从規范性的角度来洴，一般会在 `pull request`之前用 `rebase`把一个 `feature`的多个 `commit`合并成一个，不然主仓库主分支的提交记录会特别乱
10. `pull request`	准备将自己的分支合入 `master`分支，并要求其他开发者审阅代码并批准 `pr`
11. `merge`	得到批准后，将自己分支上的代码合入 `master`分支
