from pathlib import Path
from typing import Optional

from bssir.metadata_reader import config, _Years
from bssir.api import API
from bssir.maintainer import Maintainer


defaults, metadata = config.set_package_config(Path(__file__).parent)
api = API(defaults=defaults, metadata=metadata)

def create_and_upload(
    years: _Years = "all",
    table_names: Optional[list[str]] = None,
    mirror_name: Optional[str] = None,
    recreate_files: bool = True
) -> None:
    if recreate_files:
        api.setup(
            years,
            table_names=table_names,
            method="create_from_raw",
            download_source="original",
        )
    maintainer = Maintainer(
        lib_defaults=defaults,
        lib_metadata=metadata,
        mirror_name=mirror_name,
    )
    years = api.utils.parse_years(years)
    maintainer.upload_raw_files(years=years)
    maintainer.upload_cleaned_files(years=years, table_names=table_names)
