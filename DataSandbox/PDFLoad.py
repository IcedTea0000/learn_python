from PyPDF2 import PdfFileReader
import json
import xml.etree.ElementTree as ElementTree
import xmltodict


def extract_metadata(pdf_path):
    """
    extract metadata from pdf file
    :param pdf_path: file pdf path
    :return: dictionary of pdf metadata
    """
    with open(pdf_path, 'rb') as file:
        pdf = PdfFileReader(file)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

    metadata_dict = {
        'pdf_path': pdf_path,
        'author': information.author,
        'creator': information.creator,
        'producer': information.producer,
        'subject': information.subject,
        'title': information.title,
        'number_of_pages': number_of_pages
    }

    return metadata_dict


def extract_xml(xml_path):
    tree = ElementTree.parse(xml_path)
    root = tree.getroot()
    for element in root:
        print(element.attrib)
    # print(root)
    pass


def get_dictionary(xml_path):
    tree = ElementTree.parse(xml_path)
    root = tree.getroot()
    xml_string = ElementTree.tostring(root, encoding='utf8', method='xml')
    result_dictionary = xmltodict.parse(xml_string)
    return result_dictionary


if __name__ == '__main__':
    # pdf_path = 'C:\\workspace\\learn-python\\DataSandbox\\docs\\business-analyst.pdf'
    # result_dict = extract_metadata(pdf_path)
    # print(json.dumps(result_dict, indent=2))

    xml_path = 'C:\\workspace\\learn-python\\DataSandbox\\docs\\country_data.xml'
    # extract_xml(xml_path)
    get_dictionary(xml_path)
