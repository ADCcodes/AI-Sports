import nfl_data_py as nfl
nfl.import_pbp_data(2023, 1, downcast=True, cache=False, alt_path=None)

# Fetch the PBP data for the first game of the 2023 season
pbp = nfl.games[2023][1]