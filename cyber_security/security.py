import xml.etree.ElementTree as ET
import os
import pandas as pd

# 1. 수정할 파일이 있는 폴더의 path 저장 ("앞에 있는 r은 python UnicodeError때문에 넣은 것)
path = r'C:\Users\gksql\PycharmProjects\algorithms_practice\cyber_security\VMray Dataset'
# path의 모든 파일 이름이 저장됨
file_list = os.listdir(path)
# xml파일의 이름을 저장할 리스트
xml_list = []

# 2. 폴더안에 있는 모든 xml 파일 이름 가져오기
# for문을 이용해 file_list의 파일 이름을 하나하나씩 접근
# 파일이름에 '.xml'이 포함되어 있으면 xml_list에 추가
for file in file_list:
    if 'xml' in file:
        xml_list.append(file)

for i, file in enumerate(xml_list):
  if i>5:
    break

prefix_map = {"stix":"http://stix.mitre.org/stix-1",
              "cybox":"http://cybox.mitre.org/cybox-2",
              "ProcessObj":"http://cybox.mitre.org/objects#ProcessObject-2",
              "AddressObj":"http://cybox.mitre.org/objects#AddressObject-2"}

rows = []
cols = ["title","file_name", "pid", "name", "parent_pid","file_path"]

# 3. 모든 .xml파일에 대해 수정
# xml_list 의 모든 xml 파일에 반복
# target_path: xml 파일의 절대 경로
# root: xml 의 최상위 루트 태그
# test = xml_list[0]
# target_path = path + "\\" + test
# print(target_path)
# targetXML = open(target_path, 'r', encoding='UTF8')
# try:
#     tree = ET.parse(targetXML)
#     root = tree.getroot()
# except:
#     pass
#
# stix_observable = root.find("stix:Observables", prefix_map)
# # print(stix_observable, sep=" ")
# cybox_observs = stix_observable.findall("cybox:Observable", prefix_map)
# # print(len(cybox_observs))
#
# for cb_obs in cybox_observs:
#     cybox_title = cb_obs.find("cybox:Title", prefix_map)
#     # print(cybox_title.text)
#     cybox_obj = cb_obs.find("cybox:Object", prefix_map)
#     # print(cybox_obj.attrib, sep=" ")
#
#     cybox_property = cybox_obj.find("cybox:Properties", prefix_map)
#     # print(cybox_property.attrib, sep=" ")
#     addr = cybox_property.find("AddressObj:Address_Value", prefix_map)
#     add_val = ""
#     if addr != None:
#         add_val = addr.text
#         print(add_val)
#     cybox_image_info = cybox_property.find("ProcessObj:Image_Info", prefix_map)
#
#     pid = cybox_property.find("ProcessObj:PID", prefix_map)
#
#
#     # print(pid)
#     if not pid == None:
#         name = cybox_property.find("ProcessObj:Name", prefix_map)
#         parent_pid = cybox_property.find("ProcessObj:Parent_PID", prefix_map)
#         file_path = cybox_image_info.find("ProcessObj:Path", prefix_map)
#
#         rows.append({
#             "title": cybox_title.text,
#             "file_name": test,
#             "pid": pid.text,
#             "name": name.text,
#             "parent_pid": parent_pid.text,
#             "file_path": file_path.text,
#             "IP_address": add_val
#         })
#         # print(file_path.text)
#         # print(rows[0]['file_path'])
#         # print(test, pid.text, name.text, parent_pid.text, file_path, sep=" ")
#
# df = pd.DataFrame(rows, columns=cols)
# df.to_csv(r"C:\Users\gksql\PycharmProjects\algorithms_practice\cyber_security\output.csv")


# 3. 모든 .xml파일에 대해 수정
# xml_list 의 모든 xml 파일에 반복
# target_path: xml 파일의 절대 경로
# root: xml 의 최상위 루트 태그
for xml_file in xml_list:
    target_path = path + "\\" + xml_file
    print(target_path)
    targetXML = open(target_path, 'r', encoding='UTF8')
    try:
        tree = ET.parse(targetXML)
        root = tree.getroot()
    except:
        pass

    stix_observable = root.find("stix:Observables", prefix_map)
    # print(stix_observable, sep=" ")
    cybox_observs = stix_observable.findall("cybox:Observable", prefix_map)

    for cb_obs in cybox_observs:
        cybox_title = cb_obs.find("cybox:Title", prefix_map)
        # print(cybox_title.text)
        cybox_obj = cb_obs.find("cybox:Object", prefix_map)
        # print(cybox_obj.attrib, sep=" ")
        cybox_property = cybox_obj.find("cybox:Properties", prefix_map)
        # print(cybox_property.attrib, sep=" ")
        cybox_image_info = cybox_property.find("ProcessObj:Image_Info", prefix_map)

        pid = cybox_property.find("ProcessObj:PID", prefix_map)


        # print(pid)
        if not pid == None:
            name = cybox_property.find("ProcessObj:Name", prefix_map)
            parent_pid = cybox_property.find("ProcessObj:Parent_PID", prefix_map)
            file_path = cybox_image_info.find("ProcessObj:Path", prefix_map)
            rows.append({
                "title": cybox_title.text,
                "file_name": xml_file,
                "pid": pid.text,
                "name": name.text,
                "parent_pid": parent_pid.text,
                "file_path": file_path.text,
            })
            print(xml_file, pid.text, name.text, parent_pid.text, file_path, sep=" ")

df = pd.DataFrame(rows, columns=cols)
df.to_csv(r"C:\Users\gksql\PycharmProjects\algorithms_practice\cyber_security\output.csv")

