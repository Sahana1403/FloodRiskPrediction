import geopandas as gpd
import pandas as pd

def compute_upstream_rainfall(basin_shp, rainfall_csv, hours=24):
    basins = gpd.read_file(basin_shp)
    rain = pd.read_csv(rainfall_csv)
    pts = gpd.GeoDataFrame(
        rain, geometry=gpd.points_from_xy(rain.lon, rain.lat), crs="EPSG:4326"
    )
    basin_poly = basins.iloc[0].geometry
    recent = pts[pts.timestamp >= pd.Timestamp.now() - pd.Timedelta(hours=hours)]
    subset = recent[recent.within(basin_poly)]
    agg = subset.groupby("timestamp")["rainfall"].sum().resample("1H").sum().fillna(0)
    return agg
