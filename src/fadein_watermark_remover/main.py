import sys, pymupdf

def main():
    if len(sys.argv) > 1:
        doc = pymupdf.open(sys.argv[1])
    else:
        print('No file path found :(')
        exit(1)
    
    for page in doc:
        text_instances = page.search_for('(Printed with the demonstration version of Fade In)')
        for instance in text_instances:
            page.draw_rect(instance, color=(1, 1, 1), fill=(1, 1, 1))
    
    doc.save(doc.name, incremental=True, encryption=pymupdf.PDF_ENCRYPT_KEEP)
    doc.close()
    exit(0)