from xml.dom import minidom
import argparse


def parser_xml(xmlfile):
    #ret_dict contains dict info,ans_dict contans answer info
    doc = minidom.parse(xmlfile)
    root = doc.documentElement
    obj1 = root.getElementsByTagName('ExamInfo')
    ret_dict={}
    ret_dict['encodeno'] = get_ExamInfo(obj1[0],"StudentID")
    ret_dict['paperid'] = get_ExamInfo(obj1[0], 'PaperNo')
    ret_dict['pcid'] = int(get_ExamInfo(obj1[0],'ExamTimeID'))
    return ret_dict

def get_ExamInfo(obj,name):
	nameNode = obj.getElementsByTagName(name)[0]
	name =  nameNode.childNodes[0].nodeValue
	return name


if __name__ == "__main__":
    xmlfile = "Answer.xml"
    results = parser_xml(xmlfile)
    print(results)
    
