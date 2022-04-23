# function creates an HTML table with the stock data created by the get_market_data() function
def create_stock_table(stock_data):
    table = ["""
<html>
<body>

<h2>Market Data</h2>

<table style="border: 1px solid black; border-style: collapse;">
<tr>
    <th>Symbol</th>
    <th>Price</th>
    <th>Percent Change</th>
</tr>\n"""]

    for key,value in stock_data.items():
        table.append(f"  <tr>\n")
        table.append(f"    <td style='text-align:center;border: 1px solid #000000;'>{key}</td>\n")
        table.append(f"    <td style='text-align:center;border: 1px solid #000000;'>{value[0]}</td>\n")
        table.append(f"    <td style='text-align:center;border: 1px solid #000000;'>{value[1]}</td>\n")
        table.append(f"  </tr>\n")

    table.append("</table>\n")
    table.append("</body>\n")
    table.append("</html>")

    return("".join(table))
