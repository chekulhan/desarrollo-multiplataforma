# Comandos útiles de Linux para trabajar con datos

## 1️⃣ Core Unix tools (work everywhere)

🔹 head / tail — peek at data
head data.csv
tail -n 20 data.csv

🔹 wc — count rows
wc -l data.csv
(Subtract 1 if there’s a header.)

🔹 cut — extract columns (simple CSVs)
cut -d, -f1,3 data.csv
⚠️ Breaks if fields contain commas inside quotes.


ejemplo de archivo de css:
```csv
id,name,age,score
1,Alice,23,88.5
2,Bob,30,92.0
3,Charlie,27,79.5
4,Diana,25,85.0
5,Evan,31,90.2
6,Fiona,22,76.8
7,George,28,81.4
8,Hannah,26,89.9
9,Ian,34,73.6
10,Jenna,24,91.1
11,Kevin,29,84.3
12,Laura,27,87.0
13,Michael,35,78.9
14,Nina,21,93.5
15,Oscar,32,80.0
16,Paula,28,86.7
17,Quinn,26,82.1
18,Rachel,33,88.0
19,Sam,24,75.4
20,Tina,29,90.8
21,Umar,31,83.6
22,Vera,27,89.2
23,Will,34,77.9
```

```bash
cut -d, -f2,3 datos.csv
```

-d use a delimiter
-f1,2  - use fields


🔹 sort — sort rows
sort -t, -k3,3 data.csv
🔹 uniq — find unique values
cut -d, -f2 data.csv | sort | uniq
🔹 grep — filter rows
grep "ERROR" data.csv

## 2️⃣ awk — the Swiss army knife
Print selected columns
awk -F, '{ print $1, $3 }' data.csv
Filter rows
awk -F, '$4 > 100' data.csv
Skip header
awk -F, 'NR > 1 { print }' data.csv
⚠️ Like cut, basic awk struggles with quoted commas.

## 3️⃣ sed — quick text edits
Replace values
sed 's/old_value/new_value/g' data.csv
Delete rows
sed '/inactive/d' data.csv
Best for simple, predictable edits.

## 4️⃣ CSV-aware tools (recommended)
⭐ csvkit (Python-based, very popular)
Handles quotes, headers, encodings correctly.

Install:

pip install csvkit
Inspect columns
csvcut -n data.csv
Select columns by name
csvcut -c name,price data.csv
Filter rows
csvgrep -c status -m active data.csv
Convert to JSON
csvjson data.csv
⭐ xsv (Rust-based, extremely fast)
Install:

sudo apt install xsv
Inspect schema
xsv headers data.csv
xsv stats data.csv
Filter
xsv search ERROR data.csv
Select columns
xsv select name,price data.csv

## 5️⃣ SQL on CSV (DuckDB CLI)
duckdb
SELECT category, SUM(amount)
FROM 'data.csv'
GROUP BY category;
✔ No import
✔ Handles large files
✔ Very fast

## 6️⃣ Pipelining tools (real Linux power)
csvcut -c country,amount data.csv \
| csvgrep -c country -m US \
| xsv stats