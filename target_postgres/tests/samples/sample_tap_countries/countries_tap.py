"""Sample tap test for tap-countries.

This uses a free "Countries API" which does not require authentication.

See the online explorer and query builder here:
  - https://countries.trevorblades.com/
"""

from typing import List

from singer_sdk import Stream, Tap
from singer_sdk.typing import PropertiesList

from target_postgres.tests.samples.sample_tap_countries.countries_streams import (
    ContinentsStream,
    CountriesStream,
)


class SampleTapCountries(Tap):
    """Sample tap for Countries GraphQL API."""

    name: str = "sample-tap-countries"
    config_jsonschema = PropertiesList().to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [
            CountriesStream(tap=self),
            ContinentsStream(tap=self),
        ]
