from core.quicksearch_matchers import contains_chars
from fman import DirectoryPaneCommand, show_quicksearch, QuicksearchItem, show_status_message, show_alert
from os import listdir
from os.path import join, isdir, dirname


class SearchFilesInThisFolder(DirectoryPaneCommand):
    def __call__(self):
        result = show_quicksearch(self._suggest_my_files_and_folders)
        if result:
            query, file_path = result
            self.pane.place_cursor_at(file_path)

    def _suggest_my_files_and_folders(self, query):
        dir_ = self.pane.get_path()
        for file_name in listdir(dir_):
            file_path = join(dir_, file_name)
            if isdir(file_path):
                file_name = '[' + file_name + ']'
            match = contains_chars(file_name.lower(), query.lower())
            if match or not query:
                yield QuicksearchItem(file_path, file_name, highlight=match)


class SearchFilesInSubFolders(DirectoryPaneCommand):
    def __call__(self):
        self.current_dir = self.pane.get_path()
        result = show_quicksearch(self._suggest_my_subfolders_and_files)
        if result:
            query, file_path = result
            new_path = dirname(file_path)
            # show_alert(new_path)
            # show_alert('path: ' + new_path + ' file_path: ' + file_path)
            self.pane.set_path(new_path)
            self.pane.place_cursor_at(file_path)

    def _suggest_my_subfolders_and_files(self, query):
        self.limit_file_count = 13000
        self.folders_found = 0
        self.files_found = 0
        lst_search_items = self.load_files_for_dir(query, self.current_dir, '')

        # show status message only when limit is reached
        is_full_message = ''
        if self.limit_file_count <= 0:
            is_full_message = "reached load limit"

        show_status_message('folders/files found: ' + str(self.folders_found) + '/' + str(self.files_found) + ' ' + is_full_message, 5)

        return lst_search_items

    def load_files_for_dir(self, query, parse_dir, base_path):
        lst_search_items = []
        for file_name in listdir(parse_dir):
            self.limit_file_count -= 1
            self.files_found += 1
            file_path = join(parse_dir, file_name)
            # show_status_message("_suggest_my_subfolders_and_files: " + file_path)
            file_name_clean = file_name
            file_name = join(base_path, file_name)

            if isdir(file_path):
                self.folders_found += 1
                file_name = '[' + file_name + ']'
            match = contains_chars(file_name.lower(), query.lower())

            if match or not query:
                lst_search_items.append(QuicksearchItem(file_path, file_name, highlight=match))

            if isdir(file_path):
                new_base_path = join(base_path, file_name_clean)
                if self.limit_file_count > 0:
                    lst_search_items += self.load_files_for_dir(query, file_path, new_base_path)

        return lst_search_items
