import pymssql
import openpyxl


def main():
    conn = pymssql.connect(
        server="localhost",
        database="Northwind",
    )

    cursor = conn.cursor(as_dict=True)
    cursor.execute("SELECT * FROM Customers")
    rows = cursor.fetchall()
    conn.close()

    wb = openpyxl.Workbook()
    ws = wb.active or wb.create_sheet()
    ws.title = "Customers"

    if rows:
        ws.append(list(rows[0].keys()))
        for row in rows:
            ws.append(list(row.values()))

    wb.save("customers.xlsx")
    print(f"Saved {len(rows)} rows to customers.xlsx")


if __name__ == "__main__":
    main()
