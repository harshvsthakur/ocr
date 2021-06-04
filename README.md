# ocr
Optical Character Recognition for scanned documents

Problem : Renaming scanned documents manually as per content in the scanned document.

Approvals on Purchase Orders required signed approvals of Director. 

After approvals, a copy was made after scanning the signed document and saved in a specific folder with the name of the document formatted as : 
<PO number> <Vendor Name> - <Project ID>

Manual process meant opening each scanned document, renaming it and moving to the folder. 

Solution : This code automates the process.

1. Using cv2, image is converted to grey scale
2. Skew correction done to correct axis of scan
3. Tesseract is used for ocr functionality
4. Regex is applied on returned text from ocr based on required details from document
5. Vendor Name is returned from vendor ID in document from an existing excel sheet
6. Document is renamed as per required format
