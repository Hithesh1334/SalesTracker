create table TotalStock(stockAmt int, date date);
create table TotalCash(cashAmt int, date date);
create table dueAmount(dueAmt int, date date);
create table expRelatedToHome(reason varchar(20),givenTo varchar(20), amountgiven int,date date);
create table paymentTo(amountgivenTo varchar(20), amountgiven int, date date);
create table phonePayCash(totalamount int, date date);
create table totalSales(saleAmt int, date date);

INSERT INTO TotalStock (stockAmt, date)
VALUES
    (100, '2024-04-01'),
    (150, '2024-04-02'),
    (200, '2024-04-03'),
    (180, '2024-04-04'),
    (220, '2024-04-05'),
    (250, '2024-04-06'),
    (210, '2024-04-07'),
    (190, '2024-04-08'),
    (230, '2024-04-09'),
    (270, '2024-04-10');

INSERT INTO TotalCash (cashAmt, date)
VALUES
    (500, '2024-04-01'),
    (600, '2024-04-02'),
    (700, '2024-04-03'),
    (550, '2024-04-04'),
    (800, '2024-04-05'),
    (900, '2024-04-06'),
    (750, '2024-04-07'),
    (650, '2024-04-08'),
    (850, '2024-04-09'),
    (950, '2024-04-10');

INSERT INTO dueAmount (dueAmt, date)
VALUES
    (200, '2024-04-01'),
    (300, '2024-04-02'),
    (400, '2024-04-03'),
    (250, '2024-04-04'),
    (350, '2024-04-05'),
    (450, '2024-04-06'),
    (275, '2024-04-07'),
    (375, '2024-04-08'),
    (475, '2024-04-09'),
    (550, '2024-04-10');

INSERT INTO expRelatedToHome (reason, givenTo, amountgiven, date)
VALUES
    ('Electricity', 'Utility Company', 150, '2024-04-01'),
    ('Groceries', 'Local Store', 100, '2024-04-02'),
    ('Rent', 'Landlord', 800, '2024-04-03'),
    ('Internet', 'Service Provider', 70, '2024-04-04'),
    ('Home Repairs', 'Contractor', 200, '2024-04-05'),
    ('Gas', 'Gas Station', 50, '2024-04-06'),
    ('Water Bill', 'Utility Company', 80, '2024-04-07'),
    ('Maintenance', 'Maintenance Company', 120, '2024-04-08'),
    ('Insurance', 'Insurance Company', 180, '2024-04-09'),
    ('Property Tax', 'Government', 300, '2024-04-10');

INSERT INTO paymentTo (amountgivenTo, amountgiven, date)
VALUES
    ('Supplier A', 500, '2024-04-01'),
    ('Supplier B', 600, '2024-04-02'),
    ('Supplier C', 700, '2024-04-03'),
    ('Supplier D', 550, '2024-04-04'),
    ('Supplier E', 800, '2024-04-05'),
    ('Supplier F', 900, '2024-04-06'),
    ('Supplier G', 750, '2024-04-07'),
    ('Supplier H', 650, '2024-04-08'),
    ('Supplier I', 850, '2024-04-09'),
    ('Supplier J', 950, '2024-04-10');

INSERT INTO phonePayCash (totalamount, date)
VALUES
    (200, '2024-04-01'),
    (300, '2024-04-02'),
    (400, '2024-04-03'),
    (250, '2024-04-04'),
    (350, '2024-04-05'),
    (450, '2024-04-06'),
    (275, '2024-04-07'),
    (375, '2024-04-08'),
    (475, '2024-04-09'),
    (550, '2024-04-10');

INSERT INTO totalSales (saleAmt, date)
VALUES
    (15000, '2024-04-01'),
    (20000, '2024-04-02'),
    (25000, '2024-04-03'),
    (30000, '2024-04-04'),
    (35000, '2024-04-05'),
    (18000, '2024-04-06'),
    (22000, '2024-04-07'),
    (26000, '2024-04-08'),
    (32000, '2024-04-09'),
    (39000, '2024-04-10');

INSERT INTO netProfit (profitAmt, date)
SELECT 
    ts.saleAmt - COALESCE(tsc.totalamount, 0) - COALESCE(te.totalExpenses, 0) AS netProfit,
    ts.date
FROM 
    totalSales ts
LEFT JOIN 
    (
        SELECT 
            SUM(totalamount) AS totalamount,
            date
        FROM 
            phonePayCash
        GROUP BY 
            date
    ) tsc ON ts.date = tsc.date
LEFT JOIN 
    (
        SELECT 
            SUM(amountgiven) AS totalExpenses,
            date
        FROM 
            expRelatedToHome
        GROUP BY 
            date
    ) te ON ts.date = te.date
LEFT JOIN 
    (
        SELECT 
            SUM(amountgiven) AS totalExpenses,
            date
        FROM 
            paymentTo
        GROUP BY 
            date
        UNION ALL
        SELECT 
            SUM(dueAmt) AS totalExpenses,
            date
        FROM 
            dueAmount
        GROUP BY 
            date
    ) te2 ON ts.date = te2.date;
