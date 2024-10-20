from pathlib import Path

from bssir.metadata_reader import config, _Years
from bssir.api import API
from bssir.maintainer import Maintainer


defaults, metadata = config.set_package_config(Path(__file__).parent)
api = API(defaults=defaults, metadata=metadata)
maintainer = Maintainer(lib_defaults=defaults, lib_metadata=metadata)

def create_and_upload(years: _Years, table_names: list[str]) -> None:
    api.setup(
        years,
        table_names=table_names,
        method="create_from_raw",
        download_source="original",
    )
    maintainer.upload_raw_files()
    maintainer.upload_cleaned_files()
