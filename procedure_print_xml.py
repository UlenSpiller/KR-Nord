import xml.etree.ElementTree as ET

# Путь к вашему XML-файлу
xml_file_path = 'C:\\Users\\Сергей\\Documents\\KR_Nord\\23060_uus.xml'

# Путь к файлу, в который будем записывать результаты
output_file_path = 'C:\\Users\\Сергей\\Documents\\KR_Nord\\23060_s.txt'

# Открываем файл для записи
with open(output_file_path, 'w', encoding='utf-8') as output_file:

    # Загрузка XML-данных из файла
    root_node = ET.parse(xml_file_path).getroot()

    # Итерация по всем элементам PDAT
    output_file.write("*****- Шапка файла. Содержит общее колличество материала -*****\n")
    for pdat_element in root_node.findall(".//PDAT"):

        """Шапка файла."""
        code_pdat = pdat_element.find("CODE").text.strip()
        desc_pdat = pdat_element.find("DESC").text.strip()
        dicl_pdat = pdat_element.find("DICL").text.strip()
        docl_pdat = pdat_element.find("DOCL").text.strip()
        bqty_pdat = pdat_element.find("BQTY").text.strip()

        # Запись информации в файл
        output_file.write("*" * 10 + "\n")
        output_file.write(f"CODE: {code_pdat}\n")
        output_file.write(f"DESC: {desc_pdat}\n")
        output_file.write(f"DICL: {dicl_pdat}\n")
        output_file.write(f"DOCL: {docl_pdat}\n")
        output_file.write(f"BQTY: {bqty_pdat}\n")

        # Вывод информации
        print('*' * 10)
        print("CODE:", code_pdat)
        print("DESC:", desc_pdat)
        print("DICL:", dicl_pdat)
        print("DOCL:", docl_pdat)
        print("BQTY:", bqty_pdat)

    output_file.write("************/Конец шапки/************\n")
    # Итерация по всем элементам BAR
    for bar_element in root_node.findall(".//BAR"):

        # Извлечение информации из элемента BAR
        bran = bar_element.find("BRAN").text.strip()
        syst = bar_element.find("SYST").text.strip()
        code = bar_element.find("CODE").text.strip()
        desc = bar_element.find("DESC").text.strip()
        dicl = bar_element.find("DICL").text.strip()
        docl = bar_element.find("DOCL").text.strip()
        len  = bar_element.find("LEN").text.strip()
        pos  = bar_element.find("POS").text.strip()
        lenr = bar_element.find("LENR").text.strip()
        h    = bar_element.find("H").text.strip()
        mlt  = bar_element.find("MLT").text.strip()

        output_file.write("    *****- Описание палки -*****\n")
        output_file.write(f"    BRAN: {bran}\n")
        output_file.write(f"    SYST: {syst}\n")
        output_file.write(f"    CODE: {code}\n")
        output_file.write(f"    DESC: {desc}\n")
        output_file.write(f"    DICL: {dicl}\n")
        output_file.write(f"    DOCL: {docl}\n")
        output_file.write(f"     LEN: {len}\n")
        output_file.write(f"     POS: {pos}\n")
        output_file.write(f"    LENR: {lenr}\n")
        output_file.write(f"       H: {h}\n")
        output_file.write(f"     MLT: {mlt}\n")

        print("    ""*" * 5)
        print("    BRAN:", bran)
        print("    SYST:", syst)
        print("    CODE:", code)
        print("    DESC:", desc)
        print("    DICL:", dicl)
        print("    DOCL:", docl)
        print("    LEN:", len)
        print("    POS:", pos)
        print("    LENR:", lenr)
        print("    H:", h)
        print("    MLT:", mlt)

        # Извлекаем элементы CUT расположенные внутри BAR.
        for cut_element in bar_element.findall(".//CUT"):


            angl = cut_element.find("ANGL").text.strip()
            angr = cut_element.find("ANGR").text.strip()
            il = cut_element.find("IL").text.strip()
            ol = cut_element.find("OL").text.strip()
            bcod = cut_element.find("BCOD").text.strip()
            tina = cut_element.find("TINA").text.strip()

            cut_data = {
                'ANGL': cut_element.find("ANGL").text.strip(),
                'ANGR': cut_element.find("ANGR").text.strip(),
                'IL': cut_element.find("IL").text.strip(),
                'OL': cut_element.find("OL").text.strip(),
                'BCOD': cut_element.find("BCOD").text.strip(),
                'TINA': cut_element.find("TINA").text.strip(),
            }
            bar_data['CUT'].append(cut_data)




            output_file.write("        *****- Описание куска -*****\n")
            output_file.write(f"        ANGL: {angl}\n")
            output_file.write(f"        ANGR: {angr}\n")
            output_file.write(f"        IL: {il}\n")
            output_file.write(f"        OL: {ol}\n")
            output_file.write(f"        BCOD: {bcod}\n")
            output_file.write(f"        TINA: {tina}\n")

            # Вывод информации
            print("-" * 5 + "-" * 40)  # Разделитель между элементами CUT
            print("        " * 5 + "ANGL:", angl)
            print("        " * 5 + "ANGR:", angr)
            print("        " * 5 + "IL:", il)
            print("        " * 5 + "OL:", ol)
            print("        " * 5 + "BCOD:", bcod)
            print("        " * 5 + "TINA:", tina)
            # print("-" * 5 + "-" * 21)  # Разделитель между элементами CUT

        print("-**" * 21)  # Разделитель между элементами BAR

