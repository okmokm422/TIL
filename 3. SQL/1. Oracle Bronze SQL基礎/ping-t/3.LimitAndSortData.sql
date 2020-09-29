
-- 参考：ping-t Oracle Bronze 12c 問題集


/* 日付で行を制限、ソート */

SELECT employee_id, employee_name, hiredate 
FROM employees 
WHERE hiredate 
BETWEEN '03-04-01' AND '12-04-01' 
ORDER BY  hiredate DESC, employee_id;


SELECT employee_id, employee_name, hiredate 
FROM  employees
WHERE hiredate >= '03-04-01' AND hiredate <= '12-04-01' 
ORDER BY 3 DESC, 1;


/*
WHERE 項目 LIKE '文字パターン' ESCAPE 'エスケープ文字'

_　任意の一文字
%　0文字以上の任意の文字列
W　エスケープ文字
*/

WHERE prod_name LIKE '_i%LEDW_%ライト%' ESCAPE 'W'


/*
✗　ORDER BY句はFROM句の直後に記述しなければならない
○　ORDER BY句はSELECT文の最後に記述する
*/

/* ORDER BY句には、SELECT句で指定されていない項目を指定することもできる。 */

SELECT employee_id, employee_name 
FROM employees 
WHERE salary >= 300000 
ORDER BY  department_id ASC;

/*
WHERE句
- 列別名を指定できない
- FROM句の後に記述
- 複数の条件を記述できる
*/

/* 列別名は算術式に指定できる */


/* 否定演算子 */
WHERE department_id != 1
WHERE department_id ^= 1
WHERE department_id <> 1

/* WHERE句に指定した条件が成立する(条件が真である)行のみ検索結果として表示される */
WHERE 1 = 5;
-- >　1件も表示されない

/*
row_limiting_clause 

　SELECT 列名[, 列名 ...]
　FROM 表名
　[WHERE 条件]
　[ORDER BY 列名[, 列名 ...]]
　[OFFSET ...]
　[FETCH ...]

row_limiting_clauseはORDER BY句の後に記述

*/
SELECT prod_name, list_price FROM new_products 
ORDER BY list_price 
OFFSET 3 ROWS
FETCH NEXT 5 ROWS WITH TIES;



-- データベースに登録されている文字データは大文字/小文字が区別される


