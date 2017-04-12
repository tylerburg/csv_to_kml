"need to add a new function to ezKML: find_coordinate_fields"
import re



class ezKML:

  def __init__(self, name):

    self.header = headerXML.format(name, name)
    self.content, self.doc = "", ""
    self.title = name
    self.footer = footerXML

  def add_point(self, name, latlng, i=''):

    info_table = self.create_info_table(i)

    self.content += pointXML.format(
      name,
      info_table,
      latlng[1],
      latlng[0]
    )

  def create_info_table(self, info):

    #if we don't want extended data, don't do anything
    if not info:
      return ""

    str2r = ""
    i = 0
    for data in info:
      data = data.replace("&", "and")
      str2r += "<Data name='{}'>\n<value>{}</value>\n</Data>\n".format(
      info_table_headers[i], data)
      i+=1
    return str2r

  def create_kml(self):

    self.doc = self.header + self.content + self.footer
    return self.doc

  def save(self):

    kml = open(self.title, "w")
    kml.write(self.create_kml())
    kml.close()






class ParseCSV:

  def __init__(self, csv_path):

    self.headers, self.data = self.create_csv_array(csv_path)
    self.lat_index, self.lng_index = self.find_coordinate_fields(self.headers, self.data)

  def create_csv_array(path):

    data = []
    headers = []
    csv = open(path, "r")
    x = 0
    for row in csv.readlines():
      row = row.strip().split(',')
      if not x > 0:
        for i in row:
          headers.append(i)
      else:
        data.append(row)

    return (headers,data)

  def find_coordinate_fields(headers, data):

    strs = ["lat","latitude","lng","lon","long","longitude"]
    for h in headers:
      h = h.lower()
      if h in strs:
        hi = headers.index(h)
        si = strs.index(h)
      if i > 1:
        lng = hi
      else: lat = hi

    if not lat or not lng:


    return [lat,lng]








def run():
  global info_table_headers
  csv = open(r"\\srvcol\VOL1\GIS\data\KMZ\kmz_4_dan.txt", "r")

  d = ezKML("dans_geo.kml")
  x = 0
  for i in csv.readlines():
          data = i.strip().split(",")
          if x == 0:
                  for head in data:
                    info_table_headers.append(head)
          if x > 0:
                  data = i.strip().split(",")
                  d.add_point(data[0], (data[11], data[12]), data)
          x+=1

  d.save()


"=======================TEMPLATE XML STRINGS======================="


info_table_headers = []
headerXML = """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://earth.google.com/kml/2.2">
  <Document id="{}">
  <name>{}</name>
  <snippet></snippet>"""

pointXML = """<Placemark>
      <name>{}</name>
      <styleUrl>#IconStyle00</styleUrl>
      <Snippet></Snippet>
      <ExtendedData>{}</ExtendedData>
      <Point>
        <extrude>0</extrude>
        <altitudeMode>relativeToGround</altitudeMode>
        <coordinates> {},{},0.000000</coordinates>
      </Point>
    </Placemark>"""

footerXML = "</Document></kml>"



"=======================start======================="

if __name__ == "__main__":
  run()



