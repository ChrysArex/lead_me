from pdfminer.high_level import extract_text

text = extract_text(
        'guide-orientation-2022-2023_final_1.pdf.pdf',
        page_numbers = [19],
        maxpages = 1
        )

print(text)
