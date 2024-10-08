from LSP.plugin.core.typing import Dict
from lsp_utils.pip_client_handler import PipClientHandler
import os
import sublime


class Jedilsp(PipClientHandler):
    package_name = __package__
    requirements_txt_path = "requirements.txt"
    server_filename = "jedi-language-server"

    # --- PipClientHandler handlers ------------------------------------------------------------------------------------

    @classmethod
    def get_python_binary(cls) -> str:
        settings = sublime.load_settings("{}.sublime-settings".format(cls.package_name))
        python_binary = settings.get("python_binary")
        if python_binary and isinstance(python_binary, str):
            return python_binary
        return super().get_python_binary()

    @classmethod
    def get_additional_variables(cls) -> Dict[str, str]:
        variables = super().get_additional_variables()
        variables.update(
            {
                "sublime_py_files_dir": os.path.dirname(sublime.__file__),
            }
        )
        return variables


def plugin_loaded() -> None:
    Jedilsp.setup()


def plugin_unloaded() -> None:
    Jedilsp.cleanup()
