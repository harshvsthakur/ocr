# ocr : Optical Character Recognition for scanned documents

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


Note: Accuracy is not the best and results have to be compared. But using some if else statements can help to correct the confusion with say 'O', 'o' and '0'.

Alternate methods :
  1. Google Vision API : found the set up complicated. Accuracy seems higher though.
    Documentation : https://cloud.google.com/vision/docs/pdf
  
  2. Using ocr APIs from popular website : OCR space (code available in ocr_api.py)
    https://ocr.space/ocrapi

  
Code works with Images only ! To convert from PDF to images, 3rd party program - Poppler / imagemagick is required (google this)
  
The alternate methods stated above can be used for direct PDF conversion.
