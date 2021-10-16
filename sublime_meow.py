import sublime
import sublime_plugin

class InsertModeCommand(sublime_plugin.TextCommand):
    """
    Switch to INSERT mode, put carets at the start of each selection.
    """
    def run(self, edit):
        buf = self.view
        if buf.is_read_only():
            sublime.status_message('Buffer is read only')
            return

        buf.settings().set(key='block_caret', value=False)
        buf.settings().set(key='command_mode', value=False)

class InsertModeAppendCommand(sublime_plugin.TextCommand):
    """
    Switch to INSERT mode, put carets at the end of each selection.
    """
    def run(self, edit):
        buf = self.view
        if buf.is_read_only():
            sublime.status_message('Buffer is read only')
            return

        self.view.run_command("move", {"by": "characters", "forward": True})

        buf.settings().set(key='block_caret', value=False)
        buf.settings().set(key='command_mode', value=False)

class CommandModeCommand(sublime_plugin.TextCommand):
    """
    Switch to COMMAND mode.
    """
    def run(self, edit):
        buf = self.view
        buf.settings().set(key='block_caret', value=True)
        buf.settings().set(key='command_mode', value=True)
