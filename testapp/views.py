from django.shortcuts import render
from django.http import HttpResponse
import win32print

def print_prn_file(prn_file_path, printer_name):
    try:
        with open(prn_file_path, 'rb') as prn_file:
            prn_content = prn_file.read()

        # Open the printer and start a print job
        printer_handle = win32print.OpenPrinter(printer_name)
        print_info = win32print.GetPrinter(printer_handle, 2)
        doc_info = ("PRN Print Job", None, None)
        job_handle = win32print.StartDocPrinter(printer_handle, 1, doc_info)
        win32print.StartPagePrinter(printer_handle)

        # Write the PRN content to the printer
        win32print.WritePrinter(printer_handle, prn_content)

        # End the print job
        win32print.EndPagePrinter(printer_handle)
        win32print.EndDocPrinter(printer_handle)

        # Clean up
        win32print.ClosePrinter(printer_handle)

        print("PRN file sent to the printer.")

    except Exception as e:
        print("An error occurred:", e)
   

def print_prn(request):
    if request.method == 'POST':
        try:
            prn_file_path = "file\\Asset-100x50-Hirakud-ZPL-09082023.prn"  # Replace with the path to your PRN file
            printer_name = "Honeywell PD45S (300 dpi)"  # Replace with the name of your printer

            # Open the PRN file and print it
            print_prn_file(prn_file_path, printer_name)

            return HttpResponse("PRN file sent to the printer.")

        except Exception as e:
            return HttpResponse(f"An error occurred: {e}")

    return render(request, 'printer_plugin/print.html')
