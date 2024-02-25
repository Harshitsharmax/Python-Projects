import PyPDF2

# List of PDF files to merge
pdfiles = ["1.pdf", "2.pdf", "3.pdf"]

# Create a PdfMerger object
merger = PyPDF2.PdfMerger()

# Loop through each PDF file in the list
for filename in pdfiles:
    # Open the PDF file in read-binary mode
    pdfFile = open(filename, 'rb')
    # Create a PdfReader object for the PDF file
    pdfReader = PyPDF2.PdfReader(pdfFile)
    # Append the pages of the PDF file to the merger
    merger.append(pdfReader)
    # Close the PDF file
    pdfFile.close()

# Write the merged PDF to a new file
mergedFile = open('merged.pdf', 'wb')
merger.write(mergedFile)
# Close the merged PDF file
mergedFile.close()
