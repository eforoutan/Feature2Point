cwlVersion: v1.2
class: CommandLineTool
hints:
  DockerRequirement:
    dockerPull: eforoutan/feature2point:latest
  NetworkAccess:
    networkAccess: true

inputs:
  input_file:
    type:
      - File
      - Directory
    inputBinding:
      position: 1

outputs:
  output_geojson:
    type: File
    outputBinding:
      glob: "centroid.geojson"
 
  # output_shp:
  #   type: Directory
  #   outputBinding:
  #     glob: "centroid/*"
