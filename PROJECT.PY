print("GST Calculator")

amount = float(input("Enter amount: "))
rate = float(input("Enter GST rate (%): "))
type = input("Enter type (intrastate/interstate): ").lower()

gst = (amount * rate) / 100
total = amount + gst

if type == "interstate":
    igst = gst
    print(f"IGST: {igst}")
else:
    cgst = gst / 2
    sgst = gst / 2
    print(f"CGST: {cgst}")
    print(f"SGST: {sgst}")

print(f"Total GST: {gst}")
print(f"Total Price: {total}")
