# natural-language-to-Linux-command

Original goal
* converting natual language requests into Linux commands

Additional request: TODO
* Chat with GPT within a terminal , help finish complex jobs in multiple rounds, with debugging support.


# Installation

Obtain the script:

```
git clone https://github.com/chunhualiao/natural-language-to-Linux-command nl2cmd
cd nl2cmd
```

We recommend to use Python virtual environment to install this script

```
python3 -m venv .venv
source .venv/bin/activate
pip3 install -r requirements.txt
```

Create a file named .env with your OpenAI API KEY in it:
```
OPENAI_API_KEY="sk-*****"
```

We recommend to set an alias
```
export NL2CMD_HOME=/home/liao6/workspace/nl2cmd
alias askgpt='$NL2CMD_HOME/.venv/bin/python3 $NL2CMD_HOME/nl2cmd.py'
```

# Testing

```
$ askgpt what is your name?
I am an AI language model and do not have a name. You can call me "Chat Assistant" or "AI Assistant". How can I assist you today?
```

[liao6@tux439 nl2cmd]$ askgpt how to list files with year info.?

You can use the `ls` command with the `-l` and `--time-style` options to list files with year information. Here's an example command:

```
ls -l --time-style="+%Y" 
```

This will display the file list in long format with the year information.
