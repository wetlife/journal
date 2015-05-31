# Quckly Become Powerful with Linux

### Maximize the Usefulness of this Document
Here are ideas which present efficient ways to work with linux set up as a keyboard-driven vehicle to anywhere you please. A primary goal, which was kept in mind while building this environment, is efficiency. Command-line-tools are used frequently to allow the system to remain light(unbloated as in free of unnecessary software), which coincidentally points toward a system that is keyboard-driven.

### How to Read This Document
- Code is written within a code-block, as so: `foo`.
- Text which is to be written at the command-prompt is preceded by the traditional user-prompt-character, as so: `$ *foo*`.
- When using commands from here preceded by a prompt, do not enter the prompting character, `$`.

## Install
Arch is wonderful for AUR and maintaining a paradigm of allowing users to install only what they need within a system consisting of a custom kernel and a minimal set of utilities.
- Arch Installation

## From a Fresh Install

### Install All Software Used Here
If a package is unfamiliar after perusing , look it up when time permits.

### Edit Text
Vim supports efficient work. A couple good points about vim:
- homerow: the interface is homerow-centric
- availability: have a comfortable and efficient editor even when ssh-ing

### Sync and Backup Projects
Git allows one person or many collaborators to work from many different computers on a project. Setup, ideology, and workflow are all simply explained.
#### Ideology
Every *repo* is a complete copy of all files and their history. The name repo refers to all of the *tracked* files and their complete history of previous versions. A file is tracked when git is watching it for changes.
#### Setup
1. Check for ssh-keys so that current keys won't be overwritten by generating new ones.
```bash
    $ ls -al ~/.ssh
    # Lists the files in your .ssh directory, if they exist
    ```
2. If there are ssh-keys in `~/.ssh`, which is a common place to store these keys, then use these keys by copying the text within them just as one would after generating these keys. That is, proceed to the step for copying the localmachine's keys to github.
3.
```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
# Creates a new ssh key, using the provided email as a label
# Generating public/private rsa key pair.```
- A more complete instruction set, if needed, is located [here](https://help.github.com/articles/generating-ssh-keys/).

#### Workflow

### Writing Technical Documents

### Sound
Amixer is commandline interfacing to volume:
- `$ amixer set Master 50` sets the volume to 50%
- `$ man amixer` to read the manpage for further info

### General Shell Use
- testing base-level item
 - testing itm w/ 1 space
  - testing level item with two spaces
   - testing itm w/ 3 spaces
    - testing itm w/ 4 spaces
     - testing itm w/ 5 spaces
      - testing itm w/ 6 spaces
       - testing itm w/ 7 spaces
	- testing itm w/ tab

ALL ENUM. ITEMS STARTED W/ '1.' IN SRC:

1. testing base-level item
 1. testing itm w/ 1 space
  1. testing itm w/ 2 spaces
   1. testing itm w/ 3 spaces
    1. testing itm w/ 4 spaces
     1. testing itm w/ 5 spaces
	1. testing preceded by a tab
1. testing scnd base-lvl itm

###TODO###
things to do in this doc
- copy style from [github ssh-keygen howto page](https://help.github.com/articles/generating-ssh-keys/)
- finish testing enumeration of GFM
- finish writing github section
