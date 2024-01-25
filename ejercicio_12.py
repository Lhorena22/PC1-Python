nombreArchivo = input('Ingrese el nombre del archivo: ')
indice = nombreArchivo.index('.')
tipoArchivo = nombreArchivo[indice:].lower()
MIME = {
        '.gif': 'image/gif',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.png': 'image/png',
        '.pdf': 'application/pdf',
        '.txt': 'text/plain',
        '.zip': 'application/zip'
    }
if tipoArchivo in MIME:
    print(f"El tipo MIME del archivo {nombreArchivo} es: {MIME[tipoArchivo]}")
else:
    print(f"El tipo MIME del archivo {nombreArchivo} es: application/octet-stream")