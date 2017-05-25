# FuzzySearchFilesInCurrentFolder

This is a plugin to locate files and folders starting with the current folders in [fman](https://fman.io/).

IMHO this plugin makes [fman](https://fman.io/) an even faster file exploration tool yet. Dare I say finally even faster then Total Commander? I say this because it has fuzzy search like Sublime and on top of that it works cross platform on Mac, Windows and Linux.

PS: If you are looking for these features in a terminal, check this out [fzf](https://github.com/junegunn/fzf)

![Fuzzy search files and folders in all subfolders from current folder](https://raw.githubusercontent.com/kszcode/FuzzySearchFilesInCurrentFolder/master/resources/FuzzySearchInSubFolder.png)

## Features

- Search file in current folder: pressing CMD+F or CMD+E will popup the quick search and you can fuzzy find the file or folder you need, pressing enter will place the cursor on it.
- Search file in current sub folders: pressing SHIFT+CMD+F or SHIFT+CMD+E will popup the quick search and you can fuzzy find the file or folder looking into all the subfolders. For performance reasons only 5000 files are loaded, this is also signaled in the status bar.

## Installation

You can copy the contents of this folder to:

```~/Library/Application Support/fman/Plugins/User/FuzzySearchFilesInCurrentFolder```

Soon probably you will be able to install it via the command pallete: SHIFT+CMD+P > Install Plugin >FuzzySearchFilesInCurrentFolder

## Further development

- comment code
- the loading of the subfolders should be done in a flat mode instead of recursive mode (see explanation below)
- stop after 100 matches are found, signal in status bar
- on every key stroke load more fiels from under the matched folder, this way we can explore the subdirectory quite deep without having performance problems
- consider the toggle of the hidden files (see explanation below)

Pull requests are welcome :)


### Flat loading vs. recursive loading

```
D1
    D11
        D111
    D12
D2
```
- Recursive mode loads D1, D11, D111, D12, D2 (basically if first loads the .git folder with all it's cryptic files, you can think of this as a deep first approach which exhaust the file limit very fast)
- Flat mode loads D1, D2, D11, D12, D111 (this mode is prefered when we explore a file system)
    - This can be achieved by putting all non traversed folders at the end of a FIFO list and then cycling through all of them with a while loop until the list is either empty or the file count limit is reached.

Pull requests are welcome :)


### Toggle the hidden files

See below code from [Michael Herrmann](https://fman.io/contact)

```
That is possible. You can get the setting for the current pane via:

settings = load_json('Panes.json', default=[], save_on_quit=True)
default = {'show_hidden_files': False}
pane_index = self.pane.window.get_panes().index(self.pane)
pane_info = settings[pane_index] if pane_index < len(settings) else default
show_hidden_files = pane_info['show_hidden_files']

- see the code of ToggleHiddenFiles in the Core plugin.
```

## Thank you!

I must thank [Michael Herrmann](https://fman.io/contact) who was extremely responsive and very helpful and enabled me to solve this issue, considering that I'm very much a beginner in python.

## Activism

- You have my thanks if you take a minute to sign this petition: http://www.dafoh.org/petition-to-the-united-nations/
- This is one of the biggest human rights violations of our time, see here: http://www.stoporganharvesting.org/
