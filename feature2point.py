import geopandas as gpd
import sys
import os

def feature2point(input_file):

    # Load the input file into a GeoDataFrame
    gdf = gpd.read_file(input_file)

    # # Check if CRS is defined
    # if gdf.crs is None:
    #     print("Warning: Input file has no CRS. Assuming WGS84 (EPSG:4326).")
    #     gdf.set_crs(epsg=4326, inplace=True)

    # # If the CRS is geographic (lat/lon), reproject to a projected CRS
    # if gdf.crs.is_geographic:
    #     print("Reprojecting to EPSG:3857 (Web Mercator) for accurate centroid calculations...")
    #     gdf = gdf.to_crs(epsg=3857)  # Web Mercator for better centroid accuracy

    # Calculate centroids
    centroids_gdf = gdf.copy()
    centroids_gdf['geometry'] = gdf['geometry'].centroid

    # # Reproject centroids back to the original CRS (if changed)
    # centroids_gdf = centroids_gdf.to_crs(gdf.crs)

    # Define output file paths
    output_shapefile = os.path.join(os.getcwd(), "centroid.shp")
    output_geojson = os.path.join(os.getcwd(), "centroid.geojson")

    # Save the centroid shapefile
    centroids_gdf.to_file(output_shapefile)

    # Save the centroid GeoJSON
    centroids_gdf.to_file(output_geojson, driver='GeoJSON')

    return output_shapefile, output_geojson  # Return the paths to the output files

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python feature2point.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]

    # Compute centroids and get output file paths
    output_shp, output_geojson = feature2point(input_file)

    print(f"The centroid shapefile has been saved at: {output_shp}")
    print(f"The centroid GeoJSON file has been saved at: {output_geojson}")