from pathlib import Path
from box import Box
from injecta.package.path_resolver import resolve_path
from pyfonybundles.Bundle import Bundle
from daipecore.detector import is_cli


class DaipeCore(Bundle):
    def modify_raw_config(self, raw_config: dict) -> dict:
        if "daipe" in raw_config["parameters"]:
            raise Exception("parameters.daipe must not be explicitly defined")

        from daipecore.bootstrap.config import bootstrap_config

        root_module_name = bootstrap_config.root_module_name
        root_module_path = resolve_path(bootstrap_config.root_module_name).replace("\\", "/")
        project_root_path = Path(root_module_path).parent.parent.as_posix()

        raw_config["parameters"]["daipe"] = {
            "project_root": project_root_path,
            "root_module": {
                "name": root_module_name,
                "path": root_module_path,
            },
        }

        return raw_config

    def modify_parameters(self, parameters: Box) -> Box:
        if is_cli():
            parameters.daipecore.pandas.dataframe.show_method = "pandas_show"
        return parameters
