DECODE(expr, search, result, default)

-- exprと各searchの値を1つずつ比較します。
-- exprがsearchと等しい場合、Oracle Databaseは対応するresultを戻します。
-- 一致する値が見つからない場合は、defaultを戻します。defaultが省略されている場合は、NULLを戻します。
-- 引数は、任意の数値型(NUMBER、BINARY_FLOAT、BINARY_DOUBLE)または文字列型 →　比較演算子ダメ


SELECT 
TO_CHAR(payment_date, 'RR-MM-DD HH24:MI:SS') "決済日時", 
COALEASE(TO_CHAR(payment_date, 'L99,999,999'), '-1') "金額"
FROM payments
WHERE TO_CHAR(payment_date, 'HH24') < 15;

SELECT
TO_CHAR(payment_date, 'RR-MM-DD HH24:MI:SS') "決済日時", 
NVL(TO_CHAR(payment_date, 'L99,999,999'), -1) "金額"
FROM payments
WHERE TO_CHAR(payment_date, 'HH24') < 15;



NULLIF(expr1, expr2)

-- NULLIFは、expr1とexpr2を比較します。
-- 同じである場合は、NULLを戻します。異なる場合は、expr1を戻します。expr1には、リテラルNULLを指定できません。



-- データ型の比較規則
-- https://docs.oracle.com/cd/E16338_01/server.112/b56299/sql_elements002.htm#i46862
-- 日付書式にあっていない日付リテラルを指定することはできない