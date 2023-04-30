# natural-language-to-Linux-command

Original goal
* convert natual language requests into Linux command

Additional request
* Chat with GPT within a terminal , help finish complex jobs in multiple rounds, with debugging support.



# Deployment

 alias askgpt='/home/liao6/workspace/nl2cmd/.venv/bin/python3 /home/liao6/workspace/nl2cmd/nl2cmd.py'

[liao6@tux439 nl2cmd]$ askgpt how to list files with year info.?
You can use the `ls` command with the `-l` and `--time-style` options to list files with year information. Here's an example command:

```
ls -l --time-style="+%Y" 
```

This will display the file list in long format with the year information.